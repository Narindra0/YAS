import os
import json
import random
from datetime import datetime, timedelta

AGENTS_FICTIFS = ["EPICERIE MAMA", "TELMA SHOP IVATO", "QUINCAILLERIE BEMA", "MVOLA POINT ALPHA", "SUPERETTE TSARA"]
PROFILE_FILE = os.path.join(os.path.dirname(__file__), "..", "storage", "user_profile.json")

# ========== GESTION DU PROFIL UTILISATEUR ==========

def load_user_profile():
    """Charge le profil utilisateur depuis le fichier JSON."""
    if not os.path.exists(PROFILE_FILE):
        # Créer un profil par défaut si le fichier n'existe pas
        default_profile = {
            "utilisateur": {
                "nom": "JEAN PIERRE",
                "numero": "0340000000",
                "numero_cin": "101234567890",
                "email": "jean.pierre@telma.mg",
                "code_secret_mvola": "1234"
            },
            "soldes": {
                "mvola": 50000,
                "compte_principal": 5000,
                "epargne": 150000
            },
            "parametres": {
                "internet_active": True,
                "offre_actuelle": "TOKANA",
                "langue": "FR"
            },
            "historique": []
        }
        save_user_profile(default_profile)
        return default_profile
    
    with open(PROFILE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_user_profile(profile):
    """Sauvegarde le profil utilisateur dans le fichier JSON."""
    with open(PROFILE_FILE, 'w', encoding='utf-8') as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)

def verify_pin(profile, pin_entered):
    """Vérifie si le code secret entré correspond au code MVola."""
    return pin_entered == profile["utilisateur"]["code_secret_mvola"]

def update_solde(profile, compte, montant, operation="debit"):
    """Met à jour le solde d'un compte (debit ou credit)."""
    if operation == "debit":
        profile["soldes"][compte] -= montant
    else:  # credit
        profile["soldes"][compte] += montant
    save_user_profile(profile)

def add_to_history(profile, transaction_type, details, montant):
    """Ajoute une transaction à l'historique."""
    transaction = {
        "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "type": transaction_type,
        "details": details,
        "montant": montant
    }
    profile["historique"].append(transaction)
    # Garder uniquement les 20 dernières transactions
    if len(profile["historique"]) > 20:
        profile["historique"] = profile["historique"][-20:]
    save_user_profile(profile)

def add_offre_to_profile(profile, nom_offre, categorie, prix_str, details_tarif):
    """Ajoute une offre au profil avec gestion intelligente des dates."""
    validite_str = details_tarif.get("validite", "1 jour").lower()
    now = datetime.now()
    expiration_dt = now
    
    # Règle 1: Validité horaire (ex: 24h) -> Date à date
    if "heure" in validite_str:
        hours = 24 # Par défaut
        try:
            hours = int(validite_str.split()[0])
        except:
            pass
        expiration_dt = now + timedelta(hours=hours)
        expiration = expiration_dt.strftime("%d/%m/%Y %H:%M")
        
    # Règle 2: Validité journalière (ex: 1 jour) -> Expire à 23:59 du dernier jour
    else:
        days = 1
        try:
            days = int(validite_str.split()[0])
        except:
            days = 1
        # L'offre est valable pour 'days' jours INCLUANT aujourd'hui si achat tôt ? 
        # Généralement J+days-1 si on compte aujourd'hui, ou J+days. 
        # Pour simplifier et être généreux : J + days - 1 à 23:59:59
        # Si 1 jour -> Expire ce soir 23:59
        target_date = now + timedelta(days=(days - 1))
        expiration_dt = target_date.replace(hour=23, minute=59, second=59)
        expiration = expiration_dt.strftime("%d/%m/%Y %H:%M")
    
    # Structure de l'offre
    offre = {
        "nom": nom_offre,
        "categorie": categorie,
        "expiration": expiration,
        "consommables": {}
    }
    
    # Configuration selon catégorie
    if categorie == "YELLOW":
        offre["is_shared_balance"] = True
        offre["consommables"]["data"] = details_tarif.get("data", "0 Mo")
        offre["consommables"]["sms"] = details_tarif.get("sms", "0")
        offre["consommables"]["appels"] = None
    else: # MORA, FIRST, NET, etc.
        offre["is_shared_balance"] = False
        offre["consommables"]["data"] = details_tarif.get("data", "0 Mo")
        offre["consommables"]["sms"] = details_tarif.get("sms", "0")
        offre["consommables"]["appels"] = details_tarif.get("appels", "0 Ar")
        
    if "offres" not in profile:
        profile["offres"] = []
    profile["offres"].append(offre)
    save_user_profile(profile)

def get_active_offres(profile):
    """Récupère les offres non expirées et NETTOIE les expirées définitivement."""
    if "offres" not in profile:
        return []
        
    active = []
    has_changes = False
    now = datetime.now()
    
    updated_offres = []
    for offre in profile["offres"]:
        try:
            exp_date = datetime.strptime(offre["expiration"], "%d/%m/%Y %H:%M")
            if exp_date > now:
                active.append(offre)
                updated_offres.append(offre) # On garde
            else:
                has_changes = True # On supprime (ne pas ajouter à updated)
        except:
            # Si date invalide, on garde par sécurité ou on supprime ? 
            # Supprimons pour nettoyer les données corrompues
            has_changes = True 
            
    # Si nettoyage effectué, on sauvegarde le profil nettoyé
    if has_changes:
        profile["offres"] = updated_offres
        save_user_profile(profile)
        
    return active

def format_offre_details(offre):
    """Formate le texte de l'offre pour l'affichage avec gestion intelligente de la date."""
    cons = offre["consommables"]
    nom = offre["nom"]
    expiration_str = offre["expiration"]
    
    # Formatage date expiration
    exp_date = datetime.strptime(expiration_str, "%d/%m/%Y %H:%M")
    now = datetime.now()
    
    # Si expire aujourd'hui à 23:59 -> "jusqu'à minuit"
    if exp_date.date() == now.date() and exp_date.hour == 23 and exp_date.minute == 59:
        date_msg = "jusqu'à minuit"
    else:
        date_msg = f"jusqu'au {expiration_str}"
    
    details_str = ""
    
    # Affichage TYPE 1: M'ORA / FIRST (Tout afficher même si 0)
    if offre.get("categorie") in ["MORA", "FIRST"]:
        appels = cons.get("appels", "0")
        sms = cons.get("sms", "0")
        data = cons.get("data", "0")
        details_str = f"Bonus {nom} restants : {appels} + {sms} SMS et {data}"
        
    # Affichage TYPE 2: YELLOW (Masquer appels, afficher shared, masquer si 0)
    elif offre.get("categorie") == "YELLOW":
        parts = []
        s = cons.get("sms", "0")
        d = cons.get("data", "0")
        if s and s != "0": parts.append(f"{s} SMS")
        if d and d not in ["0", "0 Mo", "0 Go"]: parts.append(f"{d}")
        joined = " et ".join(parts)
        details_str = f"Bonus {nom} restants : {joined}"
        
    # Par défaut
    else:
        parts = []
        for k, v in cons.items():
            if v and v != "0" and v != "0 Ar" and v != "0 Mo":
                parts.append(f"{v} {k}")
        details_str = f"Bonus {nom} restants : {' + '.join(parts)}"
        
    return f"{details_str} valable {date_msg}"

# ========== FONCTIONS UTILITAIRES ==========

def clear_screen():
    """Nettoie l'écran du terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_frais(montant, grille):
    """Calcule les frais basés sur une grille tarifaire."""
    for palier in grille:
        if montant <= palier["max"]:
            return palier["frais"]
    return grille[-1]["frais"]

def is_valid_phone(phone):
    """Valide le format et l'opérateur du numéro."""
    if len(phone) != 10 or not phone.isdigit():
        return False
    prefix = phone[:3]
    # MVola/Telma: 034, 038 | Airtel: 033 | Orange: 032 | Autres: 037, 036
    valid_prefixes = ["034", "038", "033", "032", "037", "036"]
    return prefix in valid_prefixes

def get_operator(phone):
    """Retourne l'opérateur du numéro."""
    prefix = phone[:3]
    if prefix in ["034", "038"]:
        return "MVOLA"
    return "AUTRE"
