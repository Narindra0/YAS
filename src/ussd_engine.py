import random
import sys
from data.ussd_menus import USSD_DATA
import data.tarifs as tarif
from . import utils as backend

class USSDSession:
    """Gère une session USSD (navigation, calculs, transactions)."""
    
    def __init__(self, profile=None):
        """Initialise la session USSD."""
        self.profile = profile if profile else backend.load_user_profile()
        self.reset()
        
    def reset(self):
        """Réinitialise la session à son état initial."""
        self.current_state = "MAIN_MENU"
        self.current_page = 0
        self.session_data = {
            "nom": self.profile["utilisateur"]["nom"],
            "numero": self.profile["utilisateur"]["numero"],
            "numero_cin": self.profile["utilisateur"]["numero_cin"],
            "internet_active": self.profile["parametres"]["internet_active"],
            "solde_mvola": self.profile["soldes"]["mvola"],
            "solde_principal": self.profile["soldes"]["compte_principal"],
            "solde_epargne": self.profile["soldes"]["epargne"],
            "user_profile": self.profile
        }
        self.history = []
        
    def refresh_data(self):
        """Rafraîchit les données de la session depuis le profil."""
        # Recharger le profil depuis le disque pour capturer les changements manuels ou externes
        self.profile = backend.load_user_profile()
        
        # Mettre à jour TOUTES les données dynamiques pour correspondre à main.py
        p = self.profile
        sd = self.session_data
        
        sd["nom"] = p["utilisateur"]["nom"]
        sd["numero"] = p["utilisateur"]["numero"]
        sd["numero_cin"] = p["utilisateur"]["numero_cin"]
        sd["internet_active"] = p["parametres"]["internet_active"]
        
        sd["solde_principal"] = p["soldes"]["compte_principal"]
        sd["solde_mvola"] = p["soldes"]["mvola"]
        sd["solde_epargne"] = p["soldes"]["epargne"]
        sd["validite_credit"] = p["soldes"].get("validite_credit", "Inconnue")
        
        self.active_offres = backend.get_active_offres(p)
        sd["user_profile"] = p
        
    def get_menu_data(self, state):
        """Récupère les données d'un menu (statique ou dynamique)."""
        self.refresh_data()
        
        # 1. Check if in data.py
        if state in USSD_DATA and state not in ["MVOLA_HISTORIQUE", "ACC_HISTO_RESULT", "MENU_359", "MENU_359_OFFRES"]:
            return USSD_DATA[state]
            
        # 2. Dynamic MVOLA_HISTORIQUE & ACC_HISTO_RESULT
        if state in ["MVOLA_HISTORIQUE", "ACC_HISTO_RESULT"]:
            hist = self.profile.get("historique", [])
            prefix = ""
            
            if state == "ACC_HISTO_RESULT":
                prefix = "Votre demande a été prise en compte. Vous allez recevoir vos 3 dernières transactions par SMS.\\n\\n"

            # Prepare history lines
            lines = []
            if hist:
                for trans in reversed(hist[-5:]): 
                    lines.append(f"{trans['date']} - {trans['type']}\\n{trans['montant']} Ar")
            else:
                lines = ["Aucune transaction enregistrée."]
            
            history_text = "\\n\\n".join(lines)

            # 1. Terminal Output (The "SMS")
            print("\\n" + "="*50)
            print("📜 HISTORIQUE (Envoyé par SMS)")
            print("="*50)
            print(history_text)
            print("="*50 + "\\n")
            sys.stdout.flush()

            # 2. Interface Output
            if state == "ACC_HISTO_RESULT":
                # Only show success message in interface
                final_text = "Votre demande a été prise en compte. Vous allez recevoir vos 3 dernières transactions par SMS."
            else:
                # MVOLA_HISTORIQUE: Show the history directly
                final_text = history_text
            
            return {
                "title": "HISTORIQUE" if state == "MVOLA_HISTORIQUE" else "MVOLA",
                "text": final_text,
                "type": "choice",
                "options": {"0": "MVOLA_MAIN"}
            }

        # 3. Dynamic MENU_359
        if state == "MENU_359":
            data = USSD_DATA["MENU_359"].copy()
            text = data["text"]
            options = data["options"].copy()
            if not self.active_offres:
                # Remove "1 - Mes offres"
                text = text.replace("1 - Mes offres\\n", "").replace("1 - Mes offres", "")
                options.pop("1", None)
            
            return {
                "title": data["title"],
                "text": text,
                "type": data["type"],
                "options": options
            }

        # 4. Dynamic MENU_359_OFFRES
        if state == "MENU_359_OFFRES":
            if not self.active_offres:
                return {"type": "message", "text": "Aucune offre active."}
            lines = [f"{i} - {off['nom']}" for i, off in enumerate(self.active_offres, 1)]
            return {
                "title": "MES OFFRES",
                "text": "\\n".join(lines),
                "type": "choice",
                "options": {str(i): f"MENU_359_DETAIL_{i}" for i in range(1, len(self.active_offres)+1)}
            }
            
        # 5. Dynamic MENU_359_DETAIL_X
        if state.startswith("MENU_359_DETAIL_"):
            try:
                idx = int(state.split("_")[-1]) - 1
                off = self.active_offres[idx]
                details = backend.format_offre_details(off)
                return {
                    "title": "INFORMATIONS",
                    "text": details,
                    "type": "choice",
                    "options": {"0": "MENU_359_OFFRES"}
                }
            except:
                return {"type": "message", "text": "Erreur offre."}
                
        return None

    def process_node(self):
        """Exécute la logique du nœud actuel (compute, logic) jusqu'à tomber sur un écran (choice, input, message)."""
        limit = 0
        while limit < 10: # Eviter boucles infinies
            limit += 1
            menu = self.get_menu_data(self.current_state)
            
            if not menu:
                return {"type": "error", "message": "Menu introuvable."}
                
            m_type = menu.get("type")
            
            # --- LOGIC ---
            if m_type == "logic":
                conditions = menu.get("conditions", [])
                found = False
                for cond in conditions:
                    if "if" in cond:
                        match = True
                        for k, v in cond["if"].items():
                            if self.session_data.get(k) != v:
                                match = False
                                break
                        if match:
                            self.current_state = cond["then"]
                            found = True
                            break
                    elif "else" in cond:
                        self.current_state = cond["else"]
                        found = True
                        break
                if not found:
                    self.current_state = "MAIN_MENU" # Fallback
                continue

            # --- COMPUTE ---
            if m_type == "compute":
                self.execute_compute(menu.get("action"))
                self.current_state = menu.get("next")
                continue
                
            # --- VIEW NODES (choice, input, message) ---
            return self.prepare_view(menu)
            
        return {"type": "error", "message": "Boucle de redirection."}

    def prepare_view(self, menu):
        """Prépare l'affichage d'un menu (formatage, pagination)."""
        # 1. Format Text
        text = menu.get("text", "")
        try:
            text = text.format(**self.session_data)
        except:
            pass
            
        m_type = menu.get("type")
        options = menu.get("options", {})
        
        # 2. Logic to remove the redundant "0 - Retour"
        if m_type == "choice" and "0" in options and self.current_page == 0:
            # Check if text contains "0 - Retour" or "0. Retour"
            import re
            text_lines = text.split('\\n')
            new_lines = []
            removed = False
            for line in text_lines:
                if re.search(r'^0\\s?[-.]\\s?Retour', line.strip()):
                    removed = True
                    continue
                new_lines.append(line)
            
            if removed:
                text = "\\n".join(new_lines)
                options = options.copy()
                options.pop("0", None)
        
        # 3. Pagination Logic (Max 7 items)
        if m_type == "choice" and len(options) > 7:
            lines = text.split('\\n')
            # Extract items (lines starting with digit or containing " - ")
            items = []
            header = []
            for line in lines:
                l_strip = line.strip()
                if l_strip and (l_strip[0].isdigit() or (len(l_strip) > 2 and l_strip[1] == ' ' and l_strip[2] == '-')):
                    items.append(line)
                else:
                    header.append(line)
            
            total_items = len(items)
            limit = 7
            start = self.current_page * limit
            end = start + limit
            
            paged_items = items[start:end]
            
            # Reconstruct Options for this page
            paged_options = {}
            for item in paged_items:
                # Extract key (e.g. "1" from "1. Option" or "1 - Option")
                key = item.strip().split('.')[0].split('-')[0].strip()
                if key in options:
                    paged_options[key] = options[key]
            
            # Add Navigation
            if end < total_items:
                paged_items.append("# - Suivant")
                paged_options["#"] = "NEXT_PAGE"
            
            if self.current_page > 0:
                paged_items.append("0 - Précédent")
                paged_options["0"] = "PREV_PAGE"
            elif "0" in options:
                # If page 0 and 0 exists in original options (usually Back), keep it
                back_line = next((l for l in items if l.strip().startswith("0")), "0 - Retour")
                if back_line not in paged_items:
                    paged_items.append(back_line)
                paged_options["0"] = options["0"]

            text = "\\n".join(header + paged_items)
            options = paged_options

        return {
            "type": m_type,
            "title": menu.get("title", "USSD"),
            "text": text,
            "options": options,
            "input_type": "text" if m_type == "input" else "choice"
        }

    def submit_input(self, user_input):
        """Traite l'entrée utilisateur (choix ou saisie)."""
        menu = self.get_menu_data(self.current_state)
        options = menu.get("options", {})
        m_type = menu.get("type")

        # 1. Handle Navigation Options (Choice)
        if m_type == "choice":
            # --- PAGINATION NAVIGATION ---
            if len(options) > 7:
                if user_input == "#":
                    total_items = len([l for l in menu.get("text", "").split('\\n') if l.strip() and (l.strip()[0].isdigit() or (len(l_strip := l.strip()) > 2 and l_strip[1] == ' ' and l_strip[2] == '-'))])
                    if (self.current_page + 1) * 7 < total_items:
                        self.current_page += 1
                        return self.process_node()
                
                if user_input == "0" and self.current_page > 0:
                    self.current_page -= 1
                    return self.process_node()

            # --- STANDARD CHOICE ---
            if user_input in options:
                # Reset pagination on state change
                self.current_page = 0
                
                target = options[user_input]
                if isinstance(target, dict): # Complex object
                    if "save" in target:
                        for k, v in target["save"].items():
                            val_to_save = v
                            # Format value if it contains brackets (e.g. "{amount}") using session_data
                            if isinstance(v, str) and "{" in v:
                                try:
                                    val_to_save = v.format(**self.session_data)
                                except:
                                    pass # Keep original if format fails
                            self.session_data[k] = val_to_save
                    self.current_state = target["next"]
                else:
                    self.current_state = target
                return self.process_node()
            
            # Special case for dynamic numeric menu (handled in get_menu_data technically but validation here)
            if self.current_state == "MENU_359_OFFRES" and user_input.isdigit():
                 pass # Let check pass, get_menu_data handles keys
            
            return {"type": "error", "message": "Option invalide."}

        # 2. Handle Data Entry (Input)
        if menu.get("type") == "input":
            save_key = menu.get("save_as", "temp")
            
            # Validation
            if menu.get("validate") == "phone" and not backend.is_valid_phone(user_input):
                 return {"type": "error", "message": "Numéro invalide."}
                 
            # PIN Check & Transaction Execution
            if save_key == "pin":
                if not backend.verify_pin(self.profile, user_input):
                    return {"type": "error", "message": "Code secret incorrect."}
                
                # EXECUTE TRANSACTION LOGIC HERE
                self.execute_transaction()
                
            # Save Input
            if menu.get("save_type") == "int":
                try:
                    self.session_data[save_key] = int(user_input)
                except:
                     return {"type": "error", "message": "Montant invalide."}
            else:
                self.session_data[save_key] = user_input
                
            self.current_state = menu.get("next")
            return self.process_node()
            
        # 3. Message (End)
        if menu.get("type") == "message":
            return {"type": "finish"}

        return {"type": "error", "message": "Action inconnue."}

    def execute_compute(self, action):
        """Exécute une action de calcul."""
        sd = self.session_data
        
        if action == "calc_transfer_fees":
            m = int(sd.get("montant_base", 0))
            num = sd.get("numero_dest", "")
            op = backend.get_operator(num)
            fr = backend.get_frais(m, tarif.FRAIS_RETRAIT)
            sd["fr"] = fr
            sd["m_plus_fr"] = m + fr
            ft = backend.get_frais(m, tarif.FRAIS_TRANSFERT_MVOLA if op == "MVOLA" else tarif.FRAIS_TRANSFERT_AUTRES)
            sd["ft"] = ft
            
        elif action == "calc_advance_fees":
            m = int(sd.get("montant_avance", 0))
            frais = int(m * 0.09)
            sd["frais_avance"] = frais
            sd["total_avance"] = m + frais
            sd["date_limite"] = "17/02/2026"
            
        elif action == "calc_withdraw_fees":
            m = int(sd.get("montant_retrait", 0))
            sd["frais_retrait"] = backend.get_frais(m, tarif.FRAIS_RETRAIT)
            sd["nom_agent"] = random.choice(backend.AGENTS_FICTIFS)
            
        elif action == "generate_otp":
            m = int(sd.get("montant_retrait", 0))
            sd["frais_retrait"] = backend.get_frais(m, tarif.FRAIS_RETRAIT)
            sd["otp"] = "".join([str(random.randint(0, 9)) for _ in range(6)])
            
        elif action == "get_promo_details":
            cat = sd.get("off_cat")
            name = sd.get("off_name")
            details = tarif.OFFRES.get(cat, {}).get(name, {})
            
            p = details.get("prix", "0 Ar")
            v = details.get("validite", "1 j")
            d = details.get("data", "0 Mo")
            s = details.get("sms", "0")
            a = details.get("appels", "0 Ar")
            
            msg = f"{name} à {p}"
            if cat in ["MORA", "FIRST"]:
                msg = f"{name} ! Bénéficiez de {a} de crédit d'appel + {s} SMS + {d} ({p} / {v})"
            elif cat == "YELLOW":
                if s != "0" and d != "0":
                    msg = f"{name} ! Bénéficiez de {s} SMS ou {d} pour le prix de {p} par {v}"
                elif s != "0":
                    msg = f"{name} ! Bénéficiez de {s} avec une validité de {v} pour le prix de {p}"
                else:
                    msg = f"Bénéficiez de {d} de DATA utilisable à toute heure pendant {v} pour seulement {p}"
            elif cat == "YAS_NET":
                 msg = f"{name} ! Bénéficiez de {d} de DATA utilisable à toute heure pendant {v} pour seulement {p}"
            
            
            sd["promo_msg"] = msg

        elif action == "buy_offer_main":
            # Action: Achat via Compte Principal (sans PIN pour l'instant dans le menu)
            try:
                p = self.profile
                sd = self.session_data
                
                # Parse price
                price_str = sd.get("off_price", "0 Ar")
                price = int(str(price_str).replace(" Ar", "").replace(" ", ""))
                
                # Check balance
                if sd["solde_principal"] >= price:
                    # Debit
                    backend.update_solde(p, "compte_principal", price, "debit")
                    
                    # Add offer
                    cat = sd.get("off_cat", "AUTRE")
                    name = sd.get("off_name", "Offre")
                    
                    # Retrieve details from tarifs
                    details = {}
                    for c, offs in tarif.OFFRES.items():
                        if name in offs:
                            details = offs[name]
                            break
                    
                    backend.add_offre_to_profile(p, name, cat, str(price), details)
                    backend.add_to_history(p, "ACHAT_MAIN", f"Offre {name}", -price)
                    
                    # Update session data
                    self.refresh_data()
                    sd["off_message"] = f"Vous avez activé {name}. Nouveau solde: {sd['solde_principal']} Ar"
                else:
                    sd["off_message"] = "Solde insuffisant pour cet achat."
            except Exception as e:
                sd["off_message"] = f"Erreur lors de l'achat: {str(e)}"

    def execute_transaction(self):
        """Exécute une transaction financière."""
        sd = self.session_data
        p = self.profile
        cs = self.current_state
        
        try:
            # RECHARGE
            if "montant" in sd and ("RECHARGE_DIRECT" in cs or "CONFIRM_SELF" in cs or "CONFIRM_OTHER" in cs):
                montant = int(sd["montant"])
                if p["soldes"]["mvola"] >= montant:
                    backend.update_solde(p, "mvola", montant, "debit")
                    backend.update_solde(p, "compte_principal", montant, "credit")
                    backend.add_to_history(p, "RECHARGE", f"Recharge {montant}", -montant)
            
            # TRANSFERT
            elif "montant_final" in sd:
                total = int(sd["montant_final"]) + sd.get("ft", 0)
                if p["soldes"]["mvola"] >= total:
                    backend.update_solde(p, "mvola", total, "debit")
                    backend.add_to_history(p, "TRANSFERT", f"Vers {sd.get('numero_dest')}", -total)
                    
            # RETRAIT
            elif "montant_retrait" in sd:
                 total = int(sd["montant_retrait"]) + sd.get("frais_retrait", 0)
                 if p["soldes"]["mvola"] >= total:
                    backend.update_solde(p, "mvola", total, "debit")
                    backend.add_to_history(p, "RETRAIT", f"Retrait {sd['montant_retrait']}", -total)

            # ACHAT OFFRE
            elif "off_price" in sd:
                 price = int(sd["off_price"].replace(" Ar", "").replace(" ", ""))
                 if p["soldes"]["mvola"] >= price:
                     backend.update_solde(p, "mvola", price, "debit")
                     cat = sd.get("off_cat", "AUTRE")
                     off_name = sd.get("off_name")
                     # Find details... simplified refetch
                     details = {} 
                     for c, offs in tarif.OFFRES.items():
                         if off_name in offs:
                             details = offs[off_name]; cat = c; break
                     backend.add_offre_to_profile(p, off_name, cat, str(price), details)
                     backend.add_to_history(p, "ACHAT", f"Offre {off_name}", -price)
        except Exception as e:
            print(f"Transaction Error: {e}")
