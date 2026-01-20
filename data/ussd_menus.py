"""
YAS USSD Simulator - USSD Menus Data
Copyright (c) 2026 Narindra Ranjalahy
All rights reserved.

This software is the property of Narindra Ranjalahy.
Educational/Personal use only.
"""

USSD_DATA = {
    "MAIN_MENU": {
        "title": "YAS et MOI",
        "text": "1 - MVOLA\n2 - Programme Eh'Wa\n3 - SOS Crédit\n4 - Services YAS\n5 - Promotion\n6 - Produits et Divertissements\n7 - Meilleurs Offre\n8 - Mon identité\n9 - Configurer mon mobile",
        "type": "choice",
        "options": {
            "1": "MVOLA_MAIN",
            "2": "EH_WA_MENU",
            "3": "SOS_CREDIT_MENU",
            "4": "SERVICES_YAS_MENU",
            "5": "PROMOTION_MENU",
            "6": "PRODUITS_DIV_MENU",
            "7": "BEST_OFFERS_MENU",
            "8": "IDENTITY_MENU",
            "9": "CONFIG_MOBILE"
        }
    },
    
    # --- MENU MVOLA ---
    "MVOLA_MAIN": {
        "title": "MVOLA",
        "text": "1 - Acheter Crédit ou Offre Yas\n2 - Transférer de l'argent\n3 - MVola Crédit ou Épargne\n4 - Retrait d'argent\n5 - Paiement Factures et Partenaires\n6 - Mon compte\n7 - Recevoir de l'argent\n8 - Banques et Micro-Finances\n9 - Consulter Solde\n# - Historique des transactions\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_BUY",
            "2": "MVOLA_TRANSFER",
            "3": "MVOLA_CREDIT",
            "4": "MVOLA_WITHDRAW",
            "5": "MVOLA_PAY",
            "6": "MVOLA_ACCOUNT",
            "7": "MVOLA_RECEIVE",
            "8": "MVOLA_BANK",
            "9": "MVOLA_CONSULTER_SOLDE",
            "#": "MVOLA_HISTORIQUE",
            "0": "MAIN_MENU"
        }
    },
    # --- MVOLA : ACHAT CREDIT ---
    "MVOLA_BUY": {
        "title": "ACHETER CREDIT OU OFFRE YAS",
        "text": "1. Crédit pour mon numéro\n2. Crédit pour un autre numéro\n4. Offre pour mon numéro\n5. Offre pour un autre numéro\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_CREDIT_TYPE_SELF",
            "2": "MVOLA_ENTER_PHONE",
            "4": "MVOLA_OFFER_SELF",
            "5": "MVOLA_OFFER_OTHER",
            "0": "MVOLA_MAIN"
        }
    },

    # Option 2 : Saisie du numéro
    "MVOLA_ENTER_PHONE": {
        "title": "MVOLA",
        "text": "Entrer numéro tel : (saisir 9 pour afficher le répertoire MVola)",
        "type": "input",
        "save_as": "numero",
        "next": "MVOLA_CREDIT_TYPE_OTHER"
    },

    # Choix du type de recharge (Recharge directe ou Code)
    "MVOLA_CREDIT_TYPE_SELF": {
        "title": "Crédit à envoyer",
        "text": "1. Recharge directe\n2. Code recharge\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_RECHARGE_DIRECT_SELF",
            "2": "MVOLA_CODE_RECHARGE",
            "0": "MVOLA_BUY"
        }
    },
    "MVOLA_CREDIT_TYPE_OTHER": {
        "title": "Crédit à envoyer",
        "text": "1. Recharge directe\n2. Code recharge\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_RECHARGE_DIRECT_OTHER",
            "2": "MVOLA_CODE_RECHARGE",
            "0": "MVOLA_BUY"
        }
    },

    # Recharge Directe : Saisie du montant
    "MVOLA_RECHARGE_DIRECT_SELF": {
        "title": "MVOLA",
        "text": "Entrer le montant",
        "type": "input",
        "save_as": "montant",
        "next": "MVOLA_CONFIRM_SELF"
    },
    "MVOLA_RECHARGE_DIRECT_OTHER": {
        "title": "MVOLA",
        "text": "Entrer le montant",
        "type": "input",
        "save_as": "montant",
        "next": "MVOLA_CONFIRM_OTHER"
    },

    # Confirmation
    "MVOLA_CONFIRM_SELF": {
        "title": "MVOLA",
        "text": "Pour accepter le recharge de {montant} sur votre compte prepayé depuis votre compte MVola, Entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },
    "MVOLA_CONFIRM_OTHER": {
        "title": "MVOLA",
        "text": "Pour accepter le recharge de {montant} Ar sur le numéro {numero} depuis votre compte MVola, Entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    "MVOLA_SUCCESS": {
        "title": "MVOLA",
        "text": "Transaction effectuée avec succès !",
        "type": "message"
    },

    # Code Recharge
    "MVOLA_CODE_RECHARGE": {
        "title": "MVOLA",
        "text": "1. Acheter code recharge\n2. Renvoyer dernier achat\n3. Renvoyer mes codes de recharges\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_BUY_CODE",
            "2": "MVOLA_RESEND_LAST",
            "3": "MVOLA_RESEND_ALL",
            "0": "MVOLA_BUY"
        }
    },
    "MVOLA_BUY_CODE": {"title": "MVOLA", "text": "Achat code recharge en cours...\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_MAIN"}},
    "MVOLA_RESEND_LAST": {"title": "MVOLA", "text": "Dernier code renvoyé par SMS.\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_MAIN"}},
    "MVOLA_RESEND_ALL": {"title": "MVOLA", "text": "Tous vos codes ont été renvoyés par SMS.\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_MAIN"}},

    # --- MVOLA : OFFRES ---
    "MVOLA_OFFER_SELF": {
        "title": "MVOLA",
        "text": "Votre offre tarifaire actuelle est : TOKANA\n1 - MORA (VOIX - SMS - INTERNET)\n2 - FIRST (VOIX - SMS - INTERNET)\n3 - YELOW (SMS - INTERNET)\n4 - YAS NET (INTERNET)\n5 - ROAMING (DATA - SMS - VOIX)\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MORA", "save": {"target": "self"}},
            "2": {"next": "OFFER_FIRST", "save": {"target": "self"}},
            "3": {"next": "OFFER_YELLOW", "save": {"target": "self"}},
            "4": {"next": "OFFER_NET", "save": {"target": "self"}},
            "5": {"next": "OFFER_ROAMING", "save": {"target": "self"}},
            "0": "MVOLA_BUY"
        }
    },
    "MVOLA_OFFER_OTHER": {
        "title": "MVOLA",
        "text": "Votre offre tarifaire actuelle est : TOKANA\n1 - MORA (VOIX - SMS - INTERNET)\n2 - FIRST (VOIX - SMS - INTERNET)\n3 - YELOW (SMS - INTERNET)\n4 - YAS NET (INTERNET)\n5 - ROAMING (DATA - SMS - VOIX)\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MORA", "save": {"target": "other"}},
            "2": {"next": "OFFER_FIRST", "save": {"target": "other"}},
            "3": {"next": "OFFER_YELLOW", "save": {"target": "other"}},
            "4": {"next": "OFFER_NET", "save": {"target": "other"}},
            "5": {"next": "OFFER_ROAMING", "save": {"target": "other"}},
            "0": "MVOLA_BUY"
        }
    },

    # Catégorie MORA
    "OFFER_MORA": {
        "title": "Les Offres Mora sont :",
        "text": "1. M'ora 500\n2. M'ora One\n3. M'ora +5000\n4. M'ora International\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "M'ora 500", "off_price": "500 Ar"}},
            "2": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "M'ora One", "off_price": "1 000 Ar"}},
            "3": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "M'ora +5000", "off_price": "5 000 Ar"}},
            "4": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "M'ora International", "off_price": "5 000 Ar"}},
            "0": "MVOLA_BUY"
        }
    },

    # Catégorie FIRST
    "OFFER_FIRST": {
        "title": "Les Offres First sont :",
        "text": "1. First Premium\n2. First Premium +\n3. First Prestige\n4. First Royal\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "First Premium", "off_price": "10 000 Ar"}},
            "2": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "First Premium +", "off_price": "15 000 Ar"}},
            "3": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "First Prestige", "off_price": "30 000 Ar"}},
            "4": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "First Royal", "off_price": "50 000 Ar"}},
            "0": "MVOLA_BUY"
        }
    },

    # Catégorie YELLOW
    "OFFER_YELLOW": {
        "title": "Les Offres Ye'low sont :",
        "text": "1. Ye'low 100\n2. Ye'low 200\n3. Ye'low SMS\n4. Ye'low 500\n5. Ye'low One\n6. Ye'low 1000\n7. Ye'low 2000\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low 100", "off_price": "100 Ar"}},
            "2": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low 200", "off_price": "200 Ar"}},
            "3": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low SMS", "off_price": "200 Ar"}},
            "4": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low 500", "off_price": "500 Ar"}},
            "5": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low One", "off_price": "1 000 Ar"}},
            "6": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low 1000", "off_price": "1 000 Ar"}},
            "7": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Ye'low 2000", "off_price": "2 000 Ar"}},
            "0": "MVOLA_BUY"
        }
    },

    # Catégorie NET
    "OFFER_NET": {
        "title": "Les Offres Net sont :",
        "text": "1. Net Week 3000\n2. Net Week 5000\n3. Net Week 10 000\n4. Net Month 15 000\n5. Net Month 25 000\n6. Net Month 75 000\n7. Net Month 125 000\n8. Net Month 175 000\n9. Net Month 200 000\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Week 3000", "off_price": "3 000 Ar"}},
            "2": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Week 5000", "off_price": "5 000 Ar"}},
            "3": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Week 10 000", "off_price": "10 000 Ar"}},
            "4": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 15 000", "off_price": "15 000 Ar"}},
            "5": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 25 000", "off_price": "25 000 Ar"}},
            "6": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 75 000", "off_price": "75 000 Ar"}},
            "7": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 125 000", "off_price": "125 000 Ar"}},
            "8": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 175 000", "off_price": "175 000 Ar"}},
            "9": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Net Month 200 000", "off_price": "200 000 Ar"}},
            "0": "MVOLA_BUY"
        }
    },

    # Catégorie ROAMING
    "OFFER_ROAMING": {
        "title": "Les Offres Roaming sont :",
        "text": "1. Roaming Run\n2. Roaming Jump\n3. Roaming Win\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Roaming Run", "off_price": "12 000 Ar"}},
            "2": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Roaming Jump", "off_price": "60 000 Ar"}},
            "3": {"next": "OFFER_CHECK_TARGET", "save": {"off_name": "Roaming Win", "off_price": "100 000 Ar"}},
            "0": "MVOLA_BUY"
        }
    },

    # Logique de redirection selon la cible (self/other)
    "OFFER_CHECK_TARGET": {
        "type": "logic",
        "conditions": [
            {"if": {"target": "other"}, "then": "OFFER_ENTER_PHONE"},
            {"else": "OFFER_CONFIRM"}
        ]
    },

    # Saisie du numéro pour un autre
    "OFFER_ENTER_PHONE": {
        "title": "MVOLA",
        "text": "Entrer numéro tel : (saisir 9 pour afficher le répertoire MVola)",
        "type": "input",
        "save_as": "numero",
        "next": "OFFER_CONFIRM"
    },

    # Confirmation de l'offre
    "OFFER_CONFIRM": {
        "title": "MVOLA",
        "text": "Pour Confirmer le paiement de l'offre {off_name} via MVola d'un montant de {off_price}, Entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },
    # --- MVOLA : TRANSFERT D'ARGENT ---
    "MVOLA_TRANSFER": {
        "title": "MVOLA",
        "text": "Entrer le numero de tel du destinataire ou :\n5 - MVola Epargne\n6 - Rembourser une avance\n9 - Répertoire Mvola\n0 - Retour",
        "type": "input",
        "validate": "phone",
        "save_as": "numero_dest",
        "next": "MVOLA_TRANSFER_AMOUNT",
        "options": {
            "5": "MVOLA_EPARGNE",
            "6": "MVOLA_REMBOURSER",
            "9": "MVOLA_REPERTOIRE",
            "0": "MVOLA_MAIN"
        }
    },
    "MVOLA_EPARGNE": {"title": "MVOLA", "text": "MVola Epargne\n(En construction...)\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_TRANSFER"}},
    "MVOLA_REMBOURSER": {"title": "MVOLA", "text": "Rembourser une avance\n(En construction...)\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_TRANSFER"}},
    "MVOLA_REPERTOIRE": {"title": "MVOLA", "text": "Répertoire MVola\n(En construction...)\n0 - Retour", "type": "choice", "options": {"0": "MVOLA_TRANSFER"}},
    
    "MVOLA_TRANSFER_AMOUNT": {
        "title": "MVOLA",
        "text": "Envoyer a {numero_dest} le montant de :",
        "type": "input",
        "save_type": "int",
        "save_as": "montant_base",
        "next": "MVOLA_TRANSFER_COMPUTE"
    },

    "MVOLA_TRANSFER_COMPUTE": {
        "type": "compute",
        "action": "calc_transfer_fees",
        "next": "MVOLA_TRANSFER_FEES_CHOICE"
    },

    "MVOLA_TRANSFER_FEES_CHOICE": {
        "title": "MVOLA",
        "text": "Prise en charge des frais de retrait du destinataire ?\n1 - Oui, soit un transfert de {m_plus_fr} Ar (frais de retrait : {fr})\n2 - Non, transferer {montant_base}",
        "type": "choice",
        "options": {
            "1": {"next": "MVOLA_TRANSFER_DESC", "save": {"montant_final": "{m_plus_fr}"}}, # Note: formatage géré par main.py
            "2": {"next": "MVOLA_TRANSFER_DESC", "save": {"montant_final": "{montant_base}"}}
        }
    },
    

    
    "MVOLA_TRANSFER_DESC": {
        "title": "MVOLA",
        "text": "Description du Transfert :",
        "type": "input",
        "save_as": "description",
        "next": "MVOLA_TRANSFER_CONFIRM"
    },

    "MVOLA_TRANSFER_CONFIRM": {
        "title": "MVOLA",
        "text": "Pour transférer {montant_final} vers {numero_dest}. Frais de transfert : {ft}. Description : {description}.\nEntrer code secret Mvola :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },
    # --- MVOLA : CREDIT OU EPARGNE ---
    "MVOLA_CREDIT": {
        "title": "MVOLA CREDIT OU EPARGNE",
        "text": "1. Mvola Epargne\n2. Mvola Avance\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_EPARGNE_MENU",
            "2": "MVOLA_AVANCE_MENU",
            "0": "MVOLA_MAIN"
        }
    },

    # --- BRANCHE 1 : EPARGNE ---
    "MVOLA_EPARGNE_MENU": {
        "title": "Mvola Epargne (8% l'an)",
        "text": "1. Depot sur Epargne\n2. Retrait vers Mvola\n3. Consulter Solde\n4. Historique (3 derniers)\n5. Simulateur / Info\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_EPARGNE_DEPOT",
            "2": "MVOLA_EPARGNE_RETRAIT",
            "3": "MVOLA_EPARGNE_SOLDE",
            "4": "MVOLA_EPARGNE_HISTO",
            "5": "MVOLA_EPARGNE_INFO",
            "0": "MVOLA_CREDIT"
        }
    },

    "MVOLA_EPARGNE_DEPOT": {
        "title": "MVOLA",
        "text": "Entrer le montant a epargner :",
        "type": "input",
        "save_as": "montant_epargne",
        "next": "MVOLA_EPARGNE_DEPOT_CONFIRM"
    },
    "MVOLA_EPARGNE_DEPOT_CONFIRM": {
        "title": "MVOLA",
        "text": "Depot de {montant_epargne} Ar vers Epargne. Entrer code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_EPARGNE_DEPOT_SUCCESS"
    },
    "MVOLA_EPARGNE_DEPOT_SUCCESS": {
        "title": "MVOLA",
        "text": "Vous avez epargne {montant_epargne} Ar. Nouveau solde Epargne : 150 000 Ar.",
        "type": "message"
    },

    "MVOLA_EPARGNE_RETRAIT": {
        "title": "MVOLA",
        "text": "Entrer le montant a retirer :",
        "type": "input",
        "save_as": "montant_retrait_epargne",
        "next": "MVOLA_EPARGNE_RETRAIT_CONFIRM"
    },
    "MVOLA_EPARGNE_RETRAIT_CONFIRM": {
        "title": "MVOLA",
        "text": "Retrait de {montant_retrait_epargne} Ar vers Mvola principal. Entrer code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    "MVOLA_EPARGNE_SOLDE": {
        "title": "MVOLA",
        "text": "Entrer code secret pour consulter :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_EPARGNE_SOLDE_RESULT"
    },
    "MVOLA_EPARGNE_SOLDE_RESULT": {
        "title": "MVOLA",
        "text": "Votre solde Epargne est de 150 000 Ar. Interets cumules : 1 200 Ar.",
        "type": "message"
    },

    "MVOLA_EPARGNE_HISTO": {
        "title": "MVOLA",
        "text": "Dernieres transactions :\n1. Depot 10 000 Ar (12/01)\n2. Retrait 5 000 Ar (05/01)\n3. Depot 20 000 Ar (01/01)\n0 - Retour",
        "type": "choice",
        "options": {"0": "MVOLA_EPARGNE_MENU"}
    },

    "MVOLA_EPARGNE_INFO": {
        "title": "MVOLA",
        "text": "Taux actuel : 8% par an. Interets verses trimestriellement. Epargne disponible a tout moment sans frais.",
        "type": "message"
    },

    # --- BRANCHE 2 : AVANCE ---
    "MVOLA_AVANCE_MENU": {
        "title": "Mvola Avance",
        "text": "1. Demander une Avance\n2. Rembourser une Avance\n3. Consulter Avance en cours\n4. Ma limite disponible\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_AVANCE_DEMANDER",
            "2": "MVOLA_AVANCE_REMBOURSER",
            "3": "MVOLA_AVANCE_CONSULTER",
            "4": "MVOLA_AVANCE_LIMITE",
            "0": "MVOLA_CREDIT"
        }
    },

    "MVOLA_AVANCE_DEMANDER": {
        "title": "MVOLA",
        "text": "Montant max disponible : 50 000 Ar. Entrer montant souhaite :",
        "type": "input",
        "save_as": "montant_avance",
        "next": "MVOLA_AVANCE_COMPUTE"
    },
    "MVOLA_AVANCE_COMPUTE": {
        "type": "compute",
        "action": "calc_advance_fees",
        "next": "MVOLA_AVANCE_VALIDATE"
    },
    "MVOLA_AVANCE_VALIDATE": {
        "title": "MVOLA",
        "text": "Avance : {montant_avance} Ar.\nA rembourser : {total_avance} Ar avant le {date_limite}.\n1. Confirmer\n2. Annuler",
        "type": "choice",
        "options": {
            "1": "MVOLA_AVANCE_PIN",
            "2": "MVOLA_AVANCE_MENU"
        }
    },
    "MVOLA_AVANCE_PIN": {
        "title": "MVOLA",
        "text": "Entrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    "MVOLA_AVANCE_REMBOURSER": {
        "title": "Rembourser Avance",
        "text": "1. Rembourser Totalite (54 500 Ar)\n2. Rembourser Partiel\n3. Pour un tiers\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_AVANCE_PIN",
            "2": "MVOLA_AVANCE_REMBOURSER_PARTIEL",
            "3": "MVOLA_AVANCE_REMBOURSER_TIERS",
            "0": "MVOLA_AVANCE_MENU"
        }
    },
    "MVOLA_AVANCE_REMBOURSER_PARTIEL": {
        "title": "MVOLA",
        "text": "Entrer le montant a rembourser :",
        "type": "input",
        "save_as": "montant_remboursement",
        "next": "MVOLA_AVANCE_PIN"
    },
    "MVOLA_AVANCE_REMBOURSER_TIERS": {
        "title": "MVOLA",
        "text": "Entrer le numero du beneficiaire :",
        "type": "input",
        "validate": "phone",
        "save_as": "numero_beneficiaire",
        "next": "MVOLA_AVANCE_REMBOURSER_PARTIEL"
    },

    "MVOLA_AVANCE_CONSULTER": {
        "title": "MVOLA",
        "text": "Il vous reste 54 500 Ar a payer avant le 17/02/2026.",
        "type": "message"
    },

    "MVOLA_AVANCE_LIMITE": {
        "title": "MVOLA",
        "text": "Votre score vous permet d'emprunter jusqu'a 50 000 Ar aujourd'hui. Tapez 1 pour demander.",
        "type": "choice",
        "options": {
            "1": "MVOLA_AVANCE_DEMANDER"
        }
    },
    # --- MVOLA : RETRAIT D'ARGENT ---
    "MVOLA_WITHDRAW": {
        "title": "Retrait d'argent",
        "text": "1. Aupres d'un Agent\n2. Aupres d'un GAB (ATM)\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_WITHDRAW_AGENT",
            "2": "MVOLA_WITHDRAW_GAB",
            "0": "MVOLA_MAIN"
        }
    },

    # --- SOUS-MENU 1 : AGENT ---
    "MVOLA_WITHDRAW_AGENT": {
        "title": "MVOLA",
        "text": "Entrer le numero du agent MVOLA",
        "type": "input",
        "save_as": "numero_agent",
        "next": "MVOLA_WITHDRAW_AGENT_MSG"
    },
    "MVOLA_WITHDRAW_AGENT_MSG": {
        "title": "MVOLA",
        "text": "Veuillez entrer un numero telephone d'un agent MVola ou suivez les etapes donnees par l'agent.\n1. Continuer",
        "type": "choice",
        "options": {"1": "MVOLA_WITHDRAW_AGENT_AMOUNT"}
    },
    "MVOLA_WITHDRAW_AGENT_AMOUNT": {
        "title": "MVOLA",
        "text": "Entrer le montant a retirer :",
        "type": "input",
        "save_type": "int",
        "save_as": "montant_retrait",
        "next": "MVOLA_WITHDRAW_AGENT_COMPUTE"
    },
    "MVOLA_WITHDRAW_AGENT_COMPUTE": {
        "type": "compute",
        "action": "calc_withdraw_fees",
        "next": "MVOLA_WITHDRAW_AGENT_CONFIRM"
    },
    "MVOLA_WITHDRAW_AGENT_CONFIRM": {
        "title": "MVOLA",
        "text": "Pour confirmer votre retrait de {montant_retrait} Ar (frais : {frais_retrait} Ar) auprès de {nom_agent} ({numero_agent}), veuillez entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- SOUS-MENU 2 : GAB ---
    "MVOLA_WITHDRAW_GAB": {
        "title": "Selectionnez la banque :",
        "text": "1. BNI MADAGASCAR\n2. SOCIETE GENERALE\n3. BFV-SG\n4. BOA\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "MVOLA_WITHDRAW_GAB_AMOUNT", "save": {"nom_banque": "BNI MADAGASCAR"}},
            "2": {"next": "MVOLA_WITHDRAW_GAB_AMOUNT", "save": {"nom_banque": "SOCIETE GENERALE"}},
            "3": {"next": "MVOLA_WITHDRAW_GAB_AMOUNT", "save": {"nom_banque": "BFV-SG"}},
            "4": {"next": "MVOLA_WITHDRAW_GAB_AMOUNT", "save": {"nom_banque": "BOA"}},
            "0": "MVOLA_WITHDRAW"
        }
    },
    "MVOLA_WITHDRAW_GAB_AMOUNT": {
        "title": "MVOLA",
        "text": "Entrer le montant a retirer :",
        "type": "input",
        "save_type": "int",
        "save_as": "montant_retrait",
        "next": "MVOLA_WITHDRAW_GAB_COMPUTE"
    },
    "MVOLA_WITHDRAW_GAB_COMPUTE": {
        "type": "compute",
        "action": "generate_otp",
        "next": "MVOLA_WITHDRAW_GAB_CONFIRM"
    },
    "MVOLA_WITHDRAW_GAB_CONFIRM": {
        "title": "MVOLA",
        "text": "Pour finaliser votre retrait au GAB {nom_banque} d'un montant de {montant_retrait} Ar (frais : {frais_retrait} Ar), entrez votre code secret. Un code de retrait unique vous sera ensuite envoyé.",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_WITHDRAW_GAB_SUCCESS"
    },
    "MVOLA_WITHDRAW_GAB_SUCCESS": {
        "title": "MVOLA",
        "text": "Retrait initie. Voici votre CODE DE RETRAIT : {otp} (valable 15min). Tapez ce code sur le GAB {nom_banque}.",
        "type": "message"
    },
    # --- MVOLA : PAIEMENT FACTURES ET PARTENAIRES ---
    "MVOLA_PAY": {
        "title": "Partenaires",
        "text": "1. Accepter une demande d'argent\n2. YAS ou MOOV\n3. Electricite et Eau\n4. Assurances\n5. TV et Loisirs\n6. Transports et Voyages\n7. Impots et Cotisations sociales\n8. Ecoles et Universites\n9. Autres fournisseurs\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "PARTENAIRE_DEMANDE",
            "2": "PARTENAIRE_YAS_MOOV",
            "3": "PARTENAIRE_EAU_ELEC",
            "4": "PARTENAIRE_ASSURANCE",
            "5": "PARTENAIRE_TV",
            "6": "PARTENAIRE_TRANSPORT",
            "7": "PARTENAIRE_IMPOTS",
            "8": "PARTENAIRE_ECOLES",
            "9": "PARTENAIRE_AUTRES",
            "0": "MVOLA_MAIN"
        }
    },

    # --- BRANCHE 1 : ACCEPTER DEMANDE ---
    "PARTENAIRE_DEMANDE": {
        "title": "Demandes d'argent",
        "text": "1. Voir les demandes en attente\n0. Retour",
        "type": "choice",
        "options": {
            "1": "PARTENAIRE_DEMANDE_LISTE",
            "0": "MVOLA_PAY"
        }
    },
    "PARTENAIRE_DEMANDE_LISTE": {
        "title": "Demandes en attente",
        "text": "Demandes en attente : 2. Selectionnez :\n1. Demande de Jean pour 5 000 Ar (Raison : Urgence)\n2. Demande de Marie pour 10 000 Ar\n0. Refuser toutes",
        "type": "choice",
        "options": {
            "1": {"next": "PARTENAIRE_DEMANDE_CONFIRM", "save": {"demande_nom": "Jean", "demande_montant": "5 000 Ar"}},
            "2": {"next": "PARTENAIRE_DEMANDE_CONFIRM", "save": {"demande_nom": "Marie", "demande_montant": "10 000 Ar"}},
            "0": "PARTENAIRE_DEMANDE_REFUS"
        }
    },
    "PARTENAIRE_DEMANDE_CONFIRM": {
        "title": "MVOLA",
        "text": "Accepter {demande_montant} Ar ?\n1. Oui\n2. Non",
        "type": "choice",
        "options": {
            "1": "PARTENAIRE_DEMANDE_PIN",
            "2": "PARTENAIRE_DEMANDE_LISTE"
        }
    },
    "PARTENAIRE_DEMANDE_PIN": {
        "title": "MVOLA",
        "text": "Entrer Code Secret pour valider l'envoi.",
        "type": "input",
        "save_as": "pin",
        "next": "PARTENAIRE_DEMANDE_SUCCESS"
    },
    "PARTENAIRE_DEMANDE_SUCCESS": {
        "title": "MVOLA",
        "text": "Demande acceptee. {demande_montant} Ar envoye a {demande_nom}.",
        "type": "message"
    },
    "PARTENAIRE_DEMANDE_REFUS": {
        "title": "MVOLA",
        "text": "Toutes les demandes ont été refusées.",
        "type": "message"
    },

    # --- BRANCHE 2 : YAS OU MOOV ---
    "PARTENAIRE_YAS_MOOV": {
        "title": "YAS ou MOOV",
        "text": "1. Factures PostPayee Fixe et mobile\n3. Précommande mobile\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_FACTUR_POST",
            "3": "YAS_PRECOMMANDE",
            "0": "MVOLA_PAY"
        }
    },
    "YAS_FACTUR_POST": {
        "title": "Factures PostPayee Fixe et mobile",
        "text": "1. Enregistrer mon compte\n2. Payer mes factures\n3. Payer facture d'un tiers\n4. Supprimer compte\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_FACTUR_ENREG",
            "2": "YAS_FACTUR_PAYER",
            "3": "YAS_FACTUR_TIERS",
            "4": "YAS_FACTUR_DEL",
            "0": "PARTENAIRE_YAS_MOOV"
        }
    },
    "YAS_FACTUR_PAYER": {
        "title": "Payer mes factures",
        "text": "Entrer le montant de la facture :",
        "type": "input",
        "save_as": "facture_montant",
        "next": "YAS_FACTUR_PIN"
    },
    "YAS_FACTUR_TIERS": {
        "title": "Payer facture d'un tiers",
        "text": "Entrer le numero du compte tiers :",
        "type": "input",
        "save_as": "facture_tiers",
        "next": "YAS_FACTUR_PAYER"
    },
    "YAS_FACTUR_PIN": {
        "title": "MVOLA",
        "text": "Entrer votre code secret",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },
    "YAS_PRECOMMANDE": {
        "title": "Modèles du mobile à précommander",
        "text": "1. IPhone 4S\n2. BlackBerry Bold 9900\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_PRE_ACOMPTE", "save": {"modele": "IPhone 4S"}},
            "2": {"next": "YAS_PRE_ACOMPTE", "save": {"modele": "BlackBerry Bold 9900"}},
            "0": "PARTENAIRE_YAS_MOOV"
        }
    },
    "YAS_PRE_ACOMPTE": {
        "title": "Sélectionnez votre acompte :",
        "text": "1. 100 000 Ar\n2. 200 000 Ar\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_PRE_CONFIRM", "save": {"acompte": "100 000 Ar"}},
            "2": {"next": "YAS_PRE_CONFIRM", "save": {"acompte": "200 000 Ar"}},
            "0": "YAS_PRECOMMANDE"
        }
    },
    "YAS_PRE_CONFIRM": {
        "title": "MVOLA",
        "text": "Confirmez-vous la précommande de l'{modele} avec un acompte de {acompte} ?\n1. Oui\n2. Non",
        "type": "choice",
        "options": {
            "1": "YAS_FACTUR_PIN",
            "2": "YAS_PRECOMMANDE"
        }
    },

    # --- BRANCHE 3 : ELECTRICITE ET EAU ---
    "PARTENAIRE_EAU_ELEC": {
        "title": "Electricite et Eau",
        "text": "1. Jirama\n0. Retour",
        "type": "choice",
        "options": {
            "1": "JIRAMA_MENU",
            "0": "MVOLA_PAY"
        }
    },
    "JIRAMA_MENU": {
        "title": "Jirama",
        "text": "Entrer reference facture (ex: 123456789) :",
        "type": "input",
        "save_as": "ref_facture",
        "next": "JIRAMA_MONTANT"
    },
    "JIRAMA_MONTANT": {
        "title": "Jirama",
        "text": "Montant a payer pour la facture {ref_facture} :",
        "type": "input",
        "save_as": "montant_facture",
        "next": "JIRAMA_CONFIRM"
    },
    "JIRAMA_CONFIRM": {
        "title": "Jirama",
        "text": "Frais : 100 Ar. Confirmer le paiement de {montant_facture} Ar ?\nEntrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- BRANCHE 4 : ASSURANCES ---
    "PARTENAIRE_ASSURANCE": {
        "title": "Assurances",
        "text": "1. Ny Havana (Auto/Sante)\n2. ARO Assurance\n3. Allianz Madagascar\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "ASSUR_POLICE", "save": {"assur_nom": "Ny Havana"}},
            "2": {"next": "ASSUR_POLICE", "save": {"assur_nom": "ARO Assurance"}},
            "3": {"next": "ASSUR_POLICE", "save": {"assur_nom": "Allianz Madagascar"}},
            "0": "MVOLA_PAY"
        }
    },
    "ASSUR_POLICE": {
        "title": "{assur_nom}",
        "text": "Entrer numero police :",
        "type": "input",
        "save_as": "police_num",
        "next": "ASSUR_PAYER"
    },
    "ASSUR_PAYER": {
        "title": "{assur_nom}",
        "text": "Prime due pour la police {police_num} : 25 000 Ar.\nPayer ? Entrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- BRANCHE 5 : TV ET LOISIRS ---
    "PARTENAIRE_TV": {
        "title": "TV et Loisirs",
        "text": "1. Canal+ Recharge\n2. Blueline TV\n3. StarTimes\n4. Cinema (ex: Majestic)\n0. Retour",
        "type": "choice",
        "options": {
            "1": "TV_CANAL",
            "2": "TV_BLUE",
            "3": "TV_STAR",
            "4": "TV_CINEMA",
            "0": "MVOLA_PAY"
        }
    },
    "TV_CANAL": {
        "title": "Canal+",
        "text": "Entrer numero decodeur :",
        "type": "input",
        "save_as": "decodeur_num",
        "next": "TV_CANAL_BOUQUET"
    },
    "TV_CANAL_BOUQUET": {
        "title": "Canal+",
        "text": "Choisir bouquet :\n1. Access (5 000 Ar)\n2. Premium (15 000 Ar)\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_FACTUR_PIN", "save": {"off_name": "Access"}},
            "2": {"next": "YAS_FACTUR_PIN", "save": {"off_name": "Premium"}},
            "0": "TV_CANAL"
        }
    },

    # --- BRANCHE 6 : TRANSPORTS ET VOYAGES ---
    "PARTENAIRE_TRANSPORT": {
        "title": "Transports et Voyages",
        "text": "1. Air Madagascar (Billets)\n2. Taxi-Be / Uber-like\n3. Cotisse Bus\n4. Agences Voyages (ex: Tsaradia)\n0. Retour",
        "type": "choice",
        "options": {
            "1": "TRANS_AIR",
            "2": "TRANS_TAXI",
            "3": "TRANS_BUS",
            "4": "TRANS_AGENCE",
            "0": "MVOLA_PAY"
        }
    },
    "TRANS_AIR": {
        "title": "Air Madagascar",
        "text": "Entrer reference billet :",
        "type": "input",
        "save_as": "billet_ref",
        "next": "TRANS_AIR_PAY"
    },
    "TRANS_AIR_PAY": {
        "title": "Air Madagascar",
        "text": "Montant pour le billet {billet_ref} : 450 000 Ar.\nEntrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- BRANCHE 7 : IMPOTS ET COTISATIONS ---
    "PARTENAIRE_IMPOTS": {
        "title": "Impots et Cotisations",
        "text": "1. Direction Generale des Impots (DGI)\n2. CNAPS (Securite Sociale)\n3. Autres taxes (ex: Vignette Auto)\n0. Retour",
        "type": "choice",
        "options": {
            "1": "IMPOT_DGI",
            "2": "IMPOT_CNAPS",
            "3": "IMPOT_AUTRES",
            "0": "MVOLA_PAY"
        }
    },
    "IMPOT_DGI": {
        "title": "DGI",
        "text": "Entrer NIF (Numero Fiscal) :",
        "type": "input",
        "save_as": "nif_num",
        "next": "IMPOT_DGI_PAY"
    },
    "IMPOT_DGI_PAY": {
        "title": "DGI",
        "text": "Montant impayé pour NIF {nif_num} : 50 000 Ar.\nPayer ? Entrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- BRANCHE 8 : ECOLES ET UNIVERSITES ---
    "PARTENAIRE_ECOLES": {
        "title": "Ecoles et Universites",
        "text": "1. Universite d'Antananarivo\n2. Ecoles Privees (ex: Sacre Coeur)\n3. Frais Scolaires Generaux\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ECOLE_UNIV",
            "2": "ECOLE_PRIV",
            "3": "ECOLE_GEN",
            "0": "MVOLA_PAY"
        }
    },
    "ECOLE_UNIV": {
        "title": "Universite d'Antananarivo",
        "text": "Entrer matricule etudiant :",
        "type": "input",
        "save_as": "matricule",
        "next": "ECOLE_UNIV_PAY"
    },
    "ECOLE_UNIV_PAY": {
        "title": "Universite d'Antananarivo",
        "text": "Frais inscription pour {matricule} : 15 000 Ar.\nEntrer Code Secret :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- BRANCHE 9 : AUTRES FOURNISSEURS ---
    "PARTENAIRE_AUTRES": {
        "title": "Autres fournisseurs",
        "text": "1. Supermarches (ex: Shoprite)\n2. Pharmacies (ex: PharmaVie)\n3. Services (ex: Orange Money Transfer)\n4. Rechercher par nom\n0. Retour",
        "type": "choice",
        "options": {
            "1": "AUTRE_SUPER",
            "2": "AUTRE_PHARMA",
            "3": "AUTRE_SERVICE",
            "4": "AUTRE_SEARCH",
            "0": "MVOLA_PAY"
        }
    },
    "AUTRE_SEARCH": {
        "title": "Rechercher",
        "text": "Entrer nom fournisseur :",
        "type": "input",
        "save_as": "fournisseur_nom",
        "next": "AUTRE_SEARCH_RESULT"
    },
    "AUTRE_SEARCH_RESULT": {
        "title": "Résultat",
        "text": "Fournisseur {fournisseur_nom} trouvé.\nEntrer montant à payer :",
        "type": "input",
        "save_as": "montant_autre",
        "next": "YAS_FACTUR_PIN"
    },
    # --- MVOLA : MON COMPTE ---
    "MVOLA_ACCOUNT": {
        "title": "Mon compte",
        "text": "1. Consultation de solde\n2. Consulter 3 dernières Transactions\n3. Reçus par e-mail\n4. Mon adresse e-mail\n5. Mon répertoire Mvola\n6. Mon numéro d'identification\n7. Mon code secret\n8. Changer mot secret\n9. Carte VISA MVola\n10. Renvoie numéro coupon\n11. Changement de langue\n12. Annuler transaction\n13. Valider ou refuser une annulation\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_SOLDE",
            "2": "ACC_HISTO",
            "3": "ACC_EMAIL_RECUS",
            "4": "ACC_EMAIL_MON",
            "5": "ACC_REPERTOIRE",
            "6": "ACC_ID",
            "7": "ACC_SECRET_INFO",
            "8": "ACC_SECRET_CHANGE",
            "9": "ACC_VISA",
            "10": "ACC_COUPON",
            "11": "ACC_LANGUE",
            "12": "ACC_ANNULER",
            "13": "ACC_ANNULER_VALID",
            "0": "MVOLA_MAIN"
        }
    },

    # 1. Consultation de solde
    "ACC_SOLDE": {
        "title": "MVOLA",
        "text": "Veuillez entrer votre code secret pour consulter votre solde :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_SOLDE_RESULT"
    },
    "ACC_SOLDE_RESULT": {
        "title": "MVOLA",
        "text": "Votre solde MVola est de : {solde_mvola} Ar. Solde Épargne : {solde_epargne} Ar. Merci.",
        "type": "message"
    },

    # 2. Consulter 3 dernières Transactions
    "ACC_HISTO": {
        "title": "MVOLA",
        "text": "Entrez votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_HISTO_RESULT"
    },
    "ACC_HISTO_RESULT": {
        "title": "MVOLA",
        "text": "Votre demande a été prise en compte. Vous allez recevoir vos 3 dernières transactions par SMS.",
        "type": "message"
    },

    # 3. Reçus par e-mail
    "ACC_EMAIL_RECUS": {
        "title": "Reçus par e-mail",
        "text": "1. Activer la réception automatique\n2. Désactiver la réception automatique\n3. Recevoir le reçu de la dernière transaction\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_EMAIL_ACTIVER",
            "2": "ACC_EMAIL_DESACTIVER",
            "3": "ACC_EMAIL_DERNIER",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_EMAIL_ACTIVER": {
        "title": "MVOLA",
        "text": "Entrez votre adresse e-mail :",
        "type": "input",
        "save_as": "email",
        "next": "ACC_EMAIL_ACTIVER_PIN"
    },
    "ACC_EMAIL_ACTIVER_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_EMAIL_ACTIVER_SUCCESS"
    },
    "ACC_EMAIL_ACTIVER_SUCCESS": {
        "title": "MVOLA",
        "text": "Service activé.",
        "type": "message"
    },
    "ACC_EMAIL_DESACTIVER": {
        "title": "MVOLA",
        "text": "Entrez code secret pour désactiver :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_EMAIL_DESACTIVER_SUCCESS"
    },
    "ACC_EMAIL_DESACTIVER_SUCCESS": {
        "title": "MVOLA",
        "text": "Service désactivé.",
        "type": "message"
    },
    "ACC_EMAIL_DERNIER": {
        "title": "MVOLA",
        "text": "Entrez code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_EMAIL_DERNIER_SUCCESS"
    },
    "ACC_EMAIL_DERNIER_SUCCESS": {
        "title": "MVOLA",
        "text": "Le reçu de votre dernière transaction a été envoyé par e-mail.",
        "type": "message"
    },

    # 4. Mon adresse e-mail
    "ACC_EMAIL_MON": {
        "title": "Mon adresse e-mail",
        "text": "1. Voir mon adresse e-mail actuelle\n2. Modifier mon adresse e-mail\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_EMAIL_VOIR",
            "2": "ACC_EMAIL_MODIF",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_EMAIL_VOIR": {
        "title": "MVOLA",
        "text": "Votre adresse e-mail actuelle est : {email}\n0. Retour",
        "type": "choice",
        "options": {"0": "ACC_EMAIL_MON"}
    },
    "ACC_EMAIL_MODIF": {
        "title": "MVOLA",
        "text": "Entrez votre nouvel e-mail :",
        "type": "input",
        "save_as": "new_email",
        "next": "ACC_EMAIL_MODIF_CONFIRM"
    },
    "ACC_EMAIL_MODIF_CONFIRM": {
        "title": "MVOLA",
        "text": "Confirmez l'e-mail :",
        "type": "input",
        "save_as": "confirm_email",
        "next": "ACC_EMAIL_MODIF_PIN"
    },
    "ACC_EMAIL_MODIF_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret pour valider :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_EMAIL_MODIF_SUCCESS"
    },
    "ACC_EMAIL_MODIF_SUCCESS": {
        "title": "MVOLA",
        "text": "Adresse e-mail modifiée avec succès.",
        "type": "message"
    },

    # 5. Mon répertoire Mvola
    "ACC_REPERTOIRE": {
        "title": "Mon répertoire Mvola",
        "text": "1. Ajouter un numéro favori\n2. Voir ma liste de favoris\n3. Supprimer un favori\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_REP_ADD",
            "2": "ACC_REP_LIST",
            "3": "ACC_REP_DEL",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_REP_ADD": {
        "title": "MVOLA",
        "text": "Entrez le Nom du favori :",
        "type": "input",
        "save_as": "fav_nom",
        "next": "ACC_REP_ADD_NUM"
    },
    "ACC_REP_ADD_NUM": {
        "title": "MVOLA",
        "text": "Entrez le Numéro :",
        "type": "input",
        "validate": "phone",
        "save_as": "fav_num",
        "next": "ACC_REP_ADD_SUCCESS"
    },
    "ACC_REP_ADD_SUCCESS": {
        "title": "MVOLA",
        "text": "Favori {fav_nom} ({fav_num}) ajouté avec succès.",
        "type": "message"
    },
    "ACC_REP_LIST": {
        "title": "Favoris",
        "text": "1. Jean (0340000001)\n2. Marie (0340000002)\n0. Retour",
        "type": "choice",
        "options": {"0": "ACC_REPERTOIRE"}
    },
    "ACC_REP_DEL": {
        "title": "Supprimer un favori",
        "text": "Sélectionnez le favori à supprimer :\n1. Jean\n2. Marie\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_REP_DEL_CONFIRM",
            "2": "ACC_REP_DEL_CONFIRM",
            "0": "ACC_REPERTOIRE"
        }
    },
    "ACC_REP_DEL_CONFIRM": {
        "title": "MVOLA",
        "text": "Confirmer la suppression ?\n1. Oui\n2. Non",
        "type": "choice",
        "options": {
            "1": "ACC_REP_DEL_SUCCESS",
            "2": "ACC_REPERTOIRE"
        }
    },
    "ACC_REP_DEL_SUCCESS": {
        "title": "MVOLA",
        "text": "Favori supprimé.",
        "type": "message"
    },

    # 6. Mon numéro d'identification
    "ACC_ID": {
        "title": "MVOLA",
        "text": "Votre numéro de compte MVola est le : 034 xx xxx xx. Votre compte est : Certifié.",
        "type": "message"
    },

    # 7. Mon code secret
    "ACC_SECRET_INFO": {
        "title": "Mon code secret",
        "text": "1. Sécuriser mon compte (Infos)\n2. Réinitialiser code (Si bloqué)\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_SECRET_SECURE",
            "2": "ACC_SECRET_RESET",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_SECRET_SECURE": {
        "title": "MVOLA",
        "text": "Ne partagez jamais votre code secret. MVola ne vous le demandera jamais par téléphone.",
        "type": "message"
    },
    "ACC_SECRET_RESET": {
        "title": "MVOLA",
        "text": "Pour réinitialiser votre code, veuillez vous rendre en agence avec votre CIN.",
        "type": "message"
    },

    # 8. Changer mot secret
    "ACC_SECRET_CHANGE": {
        "title": "Changer mot secret",
        "text": "Entrez votre code secret ACTUEL :",
        "type": "input",
        "save_as": "old_pin",
        "next": "ACC_SECRET_NEW"
    },
    "ACC_SECRET_NEW": {
        "title": "MVOLA",
        "text": "Entrez votre NOUVEAU code secret (4 chiffres) :",
        "type": "input",
        "save_as": "new_pin",
        "next": "ACC_SECRET_CONFIRM"
    },
    "ACC_SECRET_CONFIRM": {
        "title": "MVOLA",
        "text": "Confirmez votre NOUVEAU code secret :",
        "type": "input",
        "save_as": "confirm_pin",
        "next": "ACC_SECRET_SUCCESS"
    },
    "ACC_SECRET_SUCCESS": {
        "title": "MVOLA",
        "text": "Votre code secret a été modifié avec succès.",
        "type": "message"
    },

    # 9. Carte VISA MVola
    "ACC_VISA": {
        "title": "Carte VISA MVola",
        "text": "1. Souscrire / Acheter une carte\n2. Lier ma carte (Appairage)\n3. Infos carte & Solde\n4. Bloquer / Débloquer la carte\n5. Obtenir code PIN carte\n6. Historique transactions carte\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_VISA_SOUS",
            "2": "ACC_VISA_LIER",
            "3": "ACC_VISA_INFO",
            "4": "ACC_VISA_BLOCK",
            "5": "ACC_VISA_PIN",
            "6": "ACC_VISA_HISTO",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_VISA_SOUS": {
        "title": "MVOLA",
        "text": "Rendez-vous en agence pour acheter votre carte VISA MVola.",
        "type": "message"
    },
    "ACC_VISA_LIER": {
        "title": "MVOLA",
        "text": "Entrez les 4 derniers chiffres de votre carte :",
        "type": "input",
        "save_as": "visa_last4",
        "next": "ACC_VISA_LIER_PIN"
    },
    "ACC_VISA_LIER_PIN": {
        "title": "MVOLA",
        "text": "Entrez votre code secret MVola :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_VISA_LIER_SUCCESS"
    },
    "ACC_VISA_LIER_SUCCESS": {
        "title": "MVOLA",
        "text": "Carte VISA liée avec succès.",
        "type": "message"
    },
    "ACC_VISA_INFO": {
        "title": "MVOLA",
        "text": "Carte VISA : 4506 **** **** 1234\nStatut : Active\nSolde : 50 000 Ar",
        "type": "message"
    },
    "ACC_VISA_BLOCK": {
        "title": "MVOLA",
        "text": "1. Bloquer la carte\n2. Débloquer la carte\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_VISA_BLOCK_PIN",
            "2": "ACC_VISA_UNBLOCK_PIN",
            "0": "ACC_VISA"
        }
    },
    "ACC_VISA_BLOCK_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret pour BLOQUER :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_VISA_BLOCK_SUCCESS"
    },
    "ACC_VISA_BLOCK_SUCCESS": {
        "title": "MVOLA",
        "text": "Carte bloquée.",
        "type": "message"
    },
    "ACC_VISA_UNBLOCK_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret pour DEBLOQUER :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_VISA_UNBLOCK_SUCCESS"
    },
    "ACC_VISA_UNBLOCK_SUCCESS": {
        "title": "MVOLA",
        "text": "Carte débloquée.",
        "type": "message"
    },
    "ACC_VISA_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret MVola pour recevoir le PIN carte :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_VISA_PIN_SUCCESS"
    },
    "ACC_VISA_PIN_SUCCESS": {
        "title": "MVOLA",
        "text": "Votre code PIN carte vous a été envoyé par SMS.",
        "type": "message"
    },
    "ACC_VISA_HISTO": {
        "title": "MVOLA",
        "text": "Dernières transactions carte :\n1. Retrait GAB 10 000 Ar\n2. Paiement TPE 5 000 Ar\n0. Retour",
        "type": "choice",
        "options": {"0": "ACC_VISA"}
    },

    # 10. Renvoie numéro coupon
    "ACC_COUPON": {
        "title": "Renvoie numéro coupon",
        "text": "Entrez la référence de la transaction (ID) :",
        "type": "input",
        "save_as": "coupon_ref",
        "next": "ACC_COUPON_PIN"
    },
    "ACC_COUPON_PIN": {
        "title": "MVOLA",
        "text": "Entrez votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_COUPON_SUCCESS"
    },
    "ACC_COUPON_SUCCESS": {
        "title": "MVOLA",
        "text": "Le code de retrait (coupon) a été renvoyé par SMS au destinataire.",
        "type": "message"
    },

    # 11. Changement de langue
    "ACC_LANGUE": {
        "title": "Changement de langue",
        "text": "1. Malagasy\n2. Français\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_LANGUE_SUCCESS",
            "2": "ACC_LANGUE_SUCCESS",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_LANGUE_SUCCESS": {
        "title": "MVOLA",
        "text": "Langue modifiée avec succès.",
        "type": "message"
    },

    # 12. Annuler transaction
    "ACC_ANNULER": {
        "title": "Annuler transaction",
        "text": "Entrez la référence de la transaction à annuler (ex: 123456789) :",
        "type": "input",
        "save_as": "annul_ref",
        "next": "ACC_ANNULER_CONFIRM"
    },
    "ACC_ANNULER_CONFIRM": {
        "title": "MVOLA",
        "text": "Vous souhaitez annuler le transfert de 10 000 Ar vers 0340000001.\n1. Confirmer\n2. Quitter",
        "type": "choice",
        "options": {
            "1": "ACC_ANNULER_PIN",
            "2": "MVOLA_ACCOUNT"
        }
    },
    "ACC_ANNULER_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_ANNULER_SUCCESS"
    },
    "ACC_ANNULER_SUCCESS": {
        "title": "MVOLA",
        "text": "Demande d'annulation envoyée au destinataire.",
        "type": "message"
    },

    # 13. Valider ou refuser une annulation
    "ACC_ANNULER_VALID": {
        "title": "Annulation en attente",
        "text": "Demande d'annulation de Jean pour 10 000 Ar.\n1. Accepter le remboursement\n2. Refuser\n0. Retour",
        "type": "choice",
        "options": {
            "1": "ACC_ANNULER_VALID_PIN",
            "2": "ACC_ANNULER_REFUSE",
            "0": "MVOLA_ACCOUNT"
        }
    },
    "ACC_ANNULER_VALID_PIN": {
        "title": "MVOLA",
        "text": "Entrez code secret pour valider le renvoi des fonds :",
        "type": "input",
        "save_as": "pin",
        "next": "ACC_ANNULER_VALID_SUCCESS"
    },
    "ACC_ANNULER_VALID_SUCCESS": {
        "title": "MVOLA",
        "text": "Remboursement effectué avec succès.",
        "type": "message"
    },
    "ACC_ANNULER_REFUSE": {
        "title": "MVOLA",
        "text": "Demande d'annulation refusée.",
        "type": "message"
    },
    # --- MVOLA : RECEVOIR DE L'ARGENT ---
    "MVOLA_RECEIVE": {
        "title": "Recevoir de l'argent depuis :",
        "text": "1. MVola Épargne\n2. MVola Avance (Crédit)\n3. Western Union\n0. Retour",
        "type": "choice",
        "options": {
            "1": "REC_EPARGNE",
            "2": "MVOLA_AVANCE_MENU", # On réutilise le menu avance existant
            "3": "REC_WU",
            "0": "MVOLA_MAIN"
        }
    },

    # 1. MVola Épargne
    "REC_EPARGNE": {
        "title": "MVOLA",
        "text": "Votre solde Épargne disponible est de : 50 000 Ar.\nEntrez le montant à transférer vers votre compte principal :\n(0 pour Retour)",
        "type": "input",
        "save_type": "int",
        "save_as": "montant_recevoir_epargne",
        "next": "REC_EPARGNE_CONFIRM",
        "options": {"0": "MVOLA_RECEIVE"}
    },
    "REC_EPARGNE_CONFIRM": {
        "title": "MVOLA",
        "text": "Vous allez transférer {montant_recevoir_epargne} Ar de votre Épargne vers votre compte Principal.\n1. Confirmer\n2. Annuler",
        "type": "choice",
        "options": {
            "1": "REC_EPARGNE_PIN",
            "2": "REC_EPARGNE"
        }
    },
    "REC_EPARGNE_PIN": {
        "title": "MVOLA",
        "text": "Entrez votre code secret pour valider :",
        "type": "input",
        "save_as": "pin",
        "next": "REC_EPARGNE_SUCCESS"
    },
    "REC_EPARGNE_SUCCESS": {
        "title": "MVOLA",
        "text": "Succès. Votre compte principal a été crédité de {montant_recevoir_epargne} Ar.\nNouveau solde principal : 60 000 Ar.",
        "type": "message"
    },

    # 3. Western Union
    "REC_WU": {
        "title": "Western Union",
        "text": "Recevoir un transfert Western Union.\nAssurez-vous que le nom sur le transfert correspond à votre compte MVola.\n1. Continuer\n0. Retour",
        "type": "choice",
        "options": {
            "1": "REC_WU_MTCN",
            "0": "MVOLA_RECEIVE"
        }
    },
    "REC_WU_MTCN": {
        "title": "Western Union",
        "text": "Veuillez entrer le numéro de transfert (MTCN) à 10 chiffres :",
        "type": "input",
        "save_as": "wu_mtcn",
        "next": "REC_WU_MONTANT"
    },
    "REC_WU_MONTANT": {
        "title": "Western Union",
        "text": "Entrez le montant attendu en Ariary (ou 0 si inconnu) :",
        "type": "input",
        "save_as": "wu_montant_attendu",
        "next": "REC_WU_RECAP"
    },
    "REC_WU_RECAP": {
        "title": "Western Union",
        "text": "Transfert Western Union trouvé :\nExpéditeur : JEAN DUPONT (France)\nMontant : 200 000 Ar\n1. Confirmer la réception\n2. Annuler",
        "type": "choice",
        "options": {
            "1": "REC_WU_PIN",
            "2": "MVOLA_RECEIVE"
        }
    },
    "REC_WU_PIN": {
        "title": "Western Union",
        "text": "Entrez votre code secret pour créditer votre compte :",
        "type": "input",
        "save_as": "pin",
        "next": "REC_WU_SUCCESS"
    },
    "REC_WU_SUCCESS": {
        "title": "Western Union",
        "text": "Succès ! 200 000 Ar ont été crédités sur votre compte MVola.\nRef transaction : WU-889900.",
        "type": "message"
    },
    "MVOLA_BANK": {
        "title": "MVOLA",
        "text": "Services temporairement indisponibles, veuiller ressaier plus tard",
        "type": "message"
    },

    # --- MENU EH'WA ---
    "EH_WA_MENU": {
        "title": "Programme Eh'Wa",
        "text": "1 - Inscription\n2 - A propos de Eh'Wa\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "EHWA_INSCRIPTION",
            "2": "EHWA_ABOUT",
            "0": "MAIN_MENU"
        }
    },
    "EHWA_INSCRIPTION": {
        "title": "Inscription Eh'Wa",
        "text": "Indiquez votre âge :\n1 - Entre 15 et 17 ans\n2 - Entre 18 et 35 ans\n3 - Plus de 35 ans",
        "type": "choice",
        "options": {
            "1": "EHWA_INSCRIPTION_RESULT",
            "2": "EHWA_INSCRIPTION_RESULT",
            "3": "EHWA_INSCRIPTION_RESULT"
        }
    },
    "EHWA_INSCRIPTION_RESULT": {
        "title": "Inscription Eh'Wa",
        "text": "Ta demande d'inscription à Eh'Wa est en cours de traitement. On revient vers toi au plus vite !",
        "type": "message"
    },
    "EHWA_ABOUT": {
        "title": "A propos de Eh'Wa",
        "text": "1 - Avantages\n2 - Support\n00 - Page précédente",
        "type": "choice",
        "options": {
            "1": "EHWA_ADVANTAGES",
            "2": "EHWA_SUPPORT",
            "00": "EH_WA_MENU"
        }
    },
    "EHWA_ADVANTAGES": {
        "title": "Avantages Eh'Wa",
        "text": "Eh'Wa, c'est le programme conçu pour toi. Tu auras des avantages chez tes marques préférées, des ventes, des formations et plein d'autres surprises.\n0 - Retour",
        "type": "choice",
        "options": {"0": "EHWA_ABOUT"}
    },
    "EHWA_SUPPORT": {
        "title": "Support Eh'Wa",
        "text": "Pour plus d'informations sur Eh'Wa, contacte notre service client en appelant le 800.\n0 - Retour",
        "type": "choice",
        "options": {"0": "EHWA_ABOUT"}
    },

    # Autres menus (placeholders)
    "SOS_CREDIT_MENU": {
        "title": "SOS Crédit - Avance Urgente",
        "text": "1. Demander SOS Crédit\n2. Rembourser SOS Crédit\n3. Demander a un ami\n5. Infos et Conditions\n0. Retour",
        "type": "choice",
        "options": {
            "1": "SOS_DEMANDER",
            "2": "SOS_REMBOURSER",
            "3": "SOS_AMI_NUM",
            "5": "SOS_INFOS",
            "0": "MAIN_MENU"
        }
    },

    # 1. Demander SOS Crédit
    "SOS_DEMANDER": {
        "title": "SOS Crédit",
        "text": "Vérification en cours... Montant max disponible : 2 000 Ar.\nChoisir montant :\n1. 500 Ar (Remboursement : 550 Ar)\n2. 1 000 Ar (Remboursement : 1 100 Ar)\n3. 2 000 Ar (Remboursement : 2 200 Ar)\n4. Autre montant (max 5 000 Ar)\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "SOS_CONFIRM", "save": {"sos_montant": "500 Ar"}},
            "2": {"next": "SOS_CONFIRM", "save": {"sos_montant": "1 000 Ar"}},
            "3": {"next": "SOS_CONFIRM", "save": {"sos_montant": "2 000 Ar"}},
            "4": "SOS_AUTRE",
            "0": "SOS_CREDIT_MENU"
        }
    },
    "SOS_AUTRE": {
        "title": "SOS Crédit",
        "text": "Entrer montant souhaité (max 5 000 Ar) :",
        "type": "input",
        "save_as": "sos_montant",
        "next": "SOS_CONFIRM"
    },
    "SOS_CONFIRM": {
        "title": "SOS Crédit",
        "text": "Pour confirmer votre demande de SOS credit de {sos_montant} taper 1\n1. Confirmer\n2. Annuler",
        "type": "choice",
        "options": {
            "1": "SOS_SUCCESS",
            "2": "SOS_CREDIT_MENU"
        }
    },
    "SOS_SUCCESS": {
        "title": "SOS Crédit",
        "text": "SOS Crédit accordé ! {sos_montant} ajoutés à votre solde. Remboursez lors de la prochaine recharge. Ref: SOS12345.",
        "type": "message"
    },

    # 2. Rembourser SOS Crédit
    "SOS_REMBOURSER": {
        "title": "Rembourser SOS Crédit",
        "text": "SOS en cours : 1 100 Ar.\nRembourser 1000 Ar , entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "SOS_REMBOURSER_SUCCESS"
    },
    "SOS_REMBOURSER_SUCCESS": {
        "title": "SOS Crédit",
        "text": "Remboursement réussi. Solde SOS restant : 600 Ar.",
        "type": "message"
    },

    # 3. Demander a un ami
    "SOS_AMI_NUM": {
        "title": "Demander a un ami",
        "text": "Entrer le numero de votre ami :",
        "type": "input",
        "validate": "phone",
        "save_as": "ami_num",
        "next": "SOS_AMI_MONTANT"
    },
    "SOS_AMI_MONTANT": {
        "title": "Demander a un ami",
        "text": "Entrer le montant :",
        "type": "input",
        "save_as": "ami_montant",
        "next": "SOS_AMI_SUCCESS"
    },
    "SOS_AMI_SUCCESS": {
        "title": "Demander a un ami",
        "text": "Demande de recharger votre compte de {ami_montant} par {ami_num} envoyer avec succes.",
        "type": "message"
    },

    # 5. Infos et Conditions
    "SOS_INFOS": {
        "title": "Infos et Conditions",
        "text": "SOS Crédit : Empruntez 500-5 000 Ar. Frais 10-15%. Remboursement auto sur recharge. Éligibilité : Abonné >3 mois, sans dette. Plus d'infos : Appelez 111 (gratuit).",
        "type": "message"
    },
    "SERVICES_YAS_MENU": {
        "title": "Services YAS",
        "text": "1. Info credit\n2. Recharge\n3. Gerer Friend and Family\n4. Envoyer Credit/offre/Mega\n5. Rappel moi\n6. Acheter un offre\n7. Ajouter une jours de validiter\n8. Changement de langue\n9. Recuperer mon numero\n10. Mon numero\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_INFO",
            "2": "YAS_RECHARGE",
            "3": "YAS_FNF",
            "4": "YAS_ENVOYER",
            "5": "YAS_RAPPEL",
            "6": "YAS_ACHETER",
            "7": "YAS_VALIDITE",
            "8": "YAS_LANGUE",
            "9": "YAS_RECUPERER",
            "10": "YAS_MON_NUMERO",
            "0": "MAIN_MENU"
        }
    },

    # 1. Info credit
    "YAS_INFO": {
        "title": "Info credit",
        "text": "Votre solde actuelle est de 1 500 Ar. valide jusqu'au 20/02/2026. Pour plus d'info taper #359#.",
        "type": "message"
    },

    # 2. Recharge
    "YAS_RECHARGE": {
        "title": "Recharge",
        "text": "1. Par code\n2. Via MVola\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_RECHARGE_CODE",
            "2": "MVOLA_CREDIT_TYPE_SELF",
            "0": "SERVICES_YAS_MENU"
        }
    },
    "YAS_RECHARGE_CODE": {
        "title": "Recharge par code",
        "text": "Entrer code recharge :",
        "type": "input",
        "save_as": "code_recharge",
        "next": "YAS_RECHARGE_SUCCESS"
    },
    "YAS_RECHARGE_SUCCESS": {
        "title": "Recharge",
        "text": "Recharge a ete effectuer avec succes. Votre solde actuelle est de 6 500 Ar.",
        "type": "message"
    },

    # 3. Gerer Friend and Family
    "YAS_FNF": {
        "title": "Gerer FnF (Max 5)",
        "text": "1. Ajouter numéro\n2. Supprimer numéro\n3. Liste actuelle\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_FNF_ADD",
            "2": "YAS_FNF_DEL",
            "3": "YAS_FNF_LIST",
            "0": "SERVICES_YAS_MENU"
        }
    },
    "YAS_FNF_ADD": {
        "title": "Ajouter FnF",
        "text": "Entrer numéro (034...) :",
        "type": "input",
        "validate": "phone",
        "save_as": "fnf_num",
        "next": "YAS_FNF_ADD_SUCCESS"
    },
    "YAS_FNF_ADD_SUCCESS": {
        "title": "FnF",
        "text": "Ajouté à FnF (Tarif réduit 50%). PIN : 1234",
        "type": "message"
    },
    "YAS_FNF_DEL": {
        "title": "Supprimer FnF",
        "text": "Sélectionner de la liste :\n1. 0341234567\n2. 0347654321\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_FNF_DEL_SUCCESS",
            "2": "YAS_FNF_DEL_SUCCESS",
            "0": "YAS_FNF"
        }
    },
    "YAS_FNF_DEL_SUCCESS": {
        "title": "FnF",
        "text": "Numéro supprimé de votre liste FnF.",
        "type": "message"
    },
    "YAS_FNF_LIST": {
        "title": "Liste FnF",
        "text": "FnF : 1. 0341234567 2. 0347654321\n0. Retour",
        "type": "choice",
        "options": {"0": "YAS_FNF"}
    },

    # 4. Envoyer Credit/offre/Mega
    "YAS_ENVOYER": {
        "title": "Envoyer",
        "text": "1. Crédit\n2. Offre\n0. Retour",
        "type": "choice",
        "options": {
            "1": "MVOLA_ENTER_PHONE",
            "2": "YAS_ENVOYER_OFFRE_CAT",
            "0": "SERVICES_YAS_MENU"
        }
    },
    "YAS_ENVOYER_OFFRE_CAT": {
        "title": "Envoyer Offre",
        "text": "1 - MORA\n2 - FIRST\n3 - YELOW\n4 - YAS NET\n5 - ROAMING\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "YAS_SEND_MORA",
            "2": "YAS_SEND_FIRST",
            "3": "YAS_SEND_YELLOW",
            "4": "YAS_SEND_NET",
            "5": "YAS_SEND_ROAMING",
            "0": "YAS_ENVOYER"
        }
    },
    "YAS_SEND_MORA": {
        "title": "Offres Mora",
        "text": "1. M'ora 500\n2. M'ora One\n3. M'ora +5000\n4. M'ora International\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_SEND_PHONE", "save": {"off_name": "M'ora 500", "off_price": "500 Ar"}},
            "2": {"next": "YAS_SEND_PHONE", "save": {"off_name": "M'ora One", "off_price": "1 000 Ar"}},
            "3": {"next": "YAS_SEND_PHONE", "save": {"off_name": "M'ora +5000", "off_price": "5 000 Ar"}},
            "4": {"next": "YAS_SEND_PHONE", "save": {"off_name": "M'ora International", "off_price": "5 000 Ar"}},
            "0": "YAS_ENVOYER_OFFRE_CAT"
        }
    },
    "YAS_SEND_FIRST": {
        "title": "Offres First",
        "text": "1. First Premium\n2. First Premium +\n3. First Prestige\n4. First Royal\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_SEND_PHONE", "save": {"off_name": "First Premium", "off_price": "10 000 Ar"}},
            "2": {"next": "YAS_SEND_PHONE", "save": {"off_name": "First Premium +", "off_price": "15 000 Ar"}},
            "3": {"next": "YAS_SEND_PHONE", "save": {"off_name": "First Prestige", "off_price": "30 000 Ar"}},
            "4": {"next": "YAS_SEND_PHONE", "save": {"off_name": "First Royal", "off_price": "50 000 Ar"}},
            "0": "YAS_ENVOYER_OFFRE_CAT"
        }
    },
    "YAS_SEND_YELLOW": {
        "title": "Offres Ye'low",
        "text": "1. Ye'low 100\n2. Ye'low SMS\n3. Ye'low 200\n4. Ye'low 500\n5. Ye'low One\n6. Ye'low 1000\n7. Ye'low 2000\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low 100", "off_price": "100 Ar"}},
            "2": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low SMS", "off_price": "200 Ar"}},
            "3": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low 200", "off_price": "200 Ar"}},
            "4": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low 500", "off_price": "500 Ar"}},
            "5": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low One", "off_price": "1 000 Ar"}},
            "6": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low 1000", "off_price": "1 000 Ar"}},
            "7": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Ye'low 2000", "off_price": "2 000 Ar"}},
            "0": "YAS_ENVOYER_OFFRE_CAT"
        }
    },
    "YAS_SEND_NET": {
        "title": "Offres Yas Net",
        "text": "1. Net Week 3000\n2. Net Week 5000\n3. Net Week 10 000\n4. Net Month 15 000\n5. Net Month 25 000\n6. Net Month 75 000\n7. Net Month 125 000\n8. Net Month 175 000\n9. Net Month 200 000\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Week 3000", "off_price": "3 000 Ar"}},
            "2": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Week 5000", "off_price": "5 000 Ar"}},
            "3": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Week 10 000", "off_price": "10 000 Ar"}},
            "4": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 15 000", "off_price": "15 000 Ar"}},
            "5": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 25 000", "off_price": "25 000 Ar"}},
            "6": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 75 000", "off_price": "75 000 Ar"}},
            "7": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 125 000", "off_price": "125 000 Ar"}},
            "8": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 175 000", "off_price": "175 000 Ar"}},
            "9": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Net Month 200 000", "off_price": "200 000 Ar"}},
            "0": "YAS_ENVOYER_OFFRE_CAT"
        }
    },
    "YAS_SEND_ROAMING": {
        "title": "Offres Roaming",
        "text": "1. Roaming Run\n2. Roaming Jump\n3. Roaming Win\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Roaming Run", "off_price": "12 000 Ar"}},
            "2": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Roaming Jump", "off_price": "60 000 Ar"}},
            "3": {"next": "YAS_SEND_PHONE", "save": {"off_name": "Roaming Win", "off_price": "100 000 Ar"}},
            "0": "YAS_ENVOYER_OFFRE_CAT"
        }
    },
    "YAS_SEND_PHONE": {
        "title": "Destinataire",
        "text": "Entrer le numero du destinataire :",
        "type": "input",
        "validate": "phone",
        "save_as": "numero_dest",
        "next": "YAS_SEND_CONFIRM"
    },
    "YAS_SEND_CONFIRM": {
        "title": "Confirmation",
        "text": "Pour confirmer l'envoie du offre {off_name} pour une montant de {off_price} Ar avec votre compte principal. Entrer votre code secret :",
        "type": "input",
        "save_as": "pin",
        "next": "YAS_SEND_SUCCESS"
    },
    "YAS_SEND_SUCCESS": {
        "title": "Succès",
        "text": "Envoi de l'offre {off_name} vers {numero_dest} effectué avec succès.",
        "type": "message"
    },

    # 5. Rappel moi
    "YAS_RAPPEL": {
        "title": "Rappel moi",
        "text": "Entrer numéro :",
        "type": "input",
        "validate": "phone",
        "save_as": "rappel_num",
        "next": "YAS_RAPPEL_SUCCESS"
    },
    "YAS_RAPPEL_SUCCESS": {
        "title": "Rappel moi",
        "text": "Demande 'Rappel Moi' envoyée gratuitement. Cette messag evou sa ete offert par YAS.",
        "type": "message"
    },

    # 6. Acheter un offre
    "YAS_ACHETER": {
        "title": "Acheter Offre",
        "text": "1 - MORA\n2 - FIRST\n3 - YELOW\n4 - YAS NET\n5 - ROAMING\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "YAS_BUY_MORA",
            "2": "YAS_BUY_FIRST",
            "3": "YAS_BUY_YELLOW",
            "4": "YAS_BUY_NET",
            "5": "YAS_BUY_ROAMING",
            "0": "SERVICES_YAS_MENU"
        }
    },
    "YAS_BUY_MORA": {
        "title": "Offres Mora",
        "text": "1. M'ora 500\n2. M'ora One\n3. M'ora +5000\n4. M'ora International\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "M'ora 500"}},
            "2": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "M'ora One"}},
            "3": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "M'ora +5000"}},
            "4": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "M'ora International"}},
            "0": "YAS_ACHETER"
        }
    },
    "YAS_BUY_FIRST": {
        "title": "Offres First",
        "text": "1. First Premium\n2. First Premium +\n3. First Prestige\n4. First Royal\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "First Premium"}},
            "2": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "First Premium +"}},
            "3": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "First Prestige"}},
            "4": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "First Royal"}},
            "0": "YAS_ACHETER"
        }
    },
    "YAS_BUY_YELLOW": {
        "title": "Offres Ye'low",
        "text": "1. Ye'low 100\n2. Ye'low SMS\n3. Ye'low 200\n4. Ye'low 500\n5. Ye'low One\n6. Ye'low 1000\n7. Ye'low 2000\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low 100"}},
            "2": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low SMS"}},
            "3": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low 200"}},
            "4": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low 500"}},
            "5": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low One"}},
            "6": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low 1000"}},
            "7": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Ye'low 2000"}},
            "0": "YAS_ACHETER"
        }
    },
    "YAS_BUY_NET": {
        "title": "Offres Yas Net",
        "text": "1. Net Week 3000\n2. Net Week 5000\n3. Net Week 10 000\n4. Net Month 15 000\n5. Net Month 25 000\n6. Net Month 75 000\n7. Net Month 125 000\n8. Net Month 175 000\n9. Net Month 200 000\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Week 3000"}},
            "2": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Week 5000"}},
            "3": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Week 10 000"}},
            "4": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 15 000"}},
            "5": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 25 000"}},
            "6": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 75 000"}},
            "7": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 125 000"}},
            "8": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 175 000"}},
            "9": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Net Month 200 000"}},
            "0": "YAS_ACHETER"
        }
    },
    "YAS_BUY_ROAMING": {
        "title": "Offres Roaming",
        "text": "1. Roaming Run\n2. Roaming Jump\n3. Roaming Win\n0. Retour",
        "type": "choice",
        "options": {
            "1": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Roaming Run"}},
            "2": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Roaming Jump"}},
            "3": {"next": "YAS_BUY_SUCCESS", "save": {"off_name": "Roaming Win"}},
            "0": "YAS_ACHETER"
        }
    },
    "YAS_BUY_SUCCESS": {
        "title": "Succès",
        "text": "Achat de l'offre {off_name} effecter avec succes.",
        "type": "message"
    },

    # 7. Ajouter une jours de validiter
    "YAS_VALIDITE": {
        "title": "Extension validité",
        "text": "Validité étendue au 20/01/2026",
        "type": "message"
    },

    # 8. Changement de langue
    "YAS_LANGUE": {
        "title": "Changement de Langue",
        "text": "1. Français\n2. Malagasy\n3. English\n0. Retour",
        "type": "choice",
        "options": {
            "1": "YAS_LANGUE_SUCCESS",
            "2": "YAS_LANGUE_SUCCESS",
            "3": "YAS_LANGUE_SUCCESS",
            "0": "SERVICES_YAS_MENU"
        }
    },
    "YAS_LANGUE_SUCCESS": {
        "title": "Langue",
        "text": "Langue changée !",
        "type": "message"
    },

    # 9. Recuperer mon numero
    "YAS_RECUPERER": {
        "title": "Recuperer mon numero",
        "text": "Entrer PIN pour récupérer :",
        "type": "input",
        "save_as": "pin_recup",
        "next": "YAS_RECUPERER_SUCCESS"
    },
    "YAS_RECUPERER_SUCCESS": {
        "title": "Recuperer mon numero",
        "text": "Votre numéro : 0345678901 (Envoyé par SMS).",
        "type": "message"
    },

    # 10. Mon numero
    "YAS_MON_NUMERO": {
        "title": "Mon numero",
        "text": "Votre numéro YAS : 0340000000.",
        "type": "message"
    },

    "PRODUITS_DIV_MENU": {
        "title": "PRODUITS ET DIVERTISSEMENT",
        "text": "1 - Yas Mitsinjo\n2 - Moozik\n3 - Zara Soa\n4 - MBalik\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MITSINJO_MENU",
            "2": "MOOZIK_MENU",
            "3": "ZARA_SOA_MENU",
            "4": "MBALIK_MENU",
            "0": "MAIN_MENU"
        }
    },

    # --- 1. YAS MITSINJO ---
    "MITSINJO_MENU": {
        "title": "Yas Mitsinjo",
        "text": "1 - Achat terminal\n2 - Paiement\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MITSINJO_PIN_ACHAT",
            "2": "MITSINJO_PAIEMENT_MENU",
            "0": "PRODUITS_DIV_MENU"
        }
    },
    "MITSINJO_PIN_ACHAT": {
        "title": "Mvola",
        "text": "Pour connaître les kits proposés, Entrer votre code secret Mvola :",
        "type": "input",
        "save_as": "pin",
        "next": "MITSINJO_KITS_LIST"
    },
    "MITSINJO_KITS_LIST": {
        "title": "Kits disponibles",
        "text": "1 - ZTE A36\n2 - ZTE A76 4G\n3 - ZTE Blade A76 5G\n4 - Samsung Galaxy A04e\n5 - Samsung Galaxy A15\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "MITSINJO_ACHAT_SUCCESS", "save": {"kit_name": "ZTE A36"}},
            "2": {"next": "MITSINJO_ACHAT_SUCCESS", "save": {"kit_name": "ZTE A76 4G"}},
            "3": {"next": "MITSINJO_ACHAT_SUCCESS", "save": {"kit_name": "ZTE Blade A76 5G"}},
            "4": {"next": "MITSINJO_ACHAT_SUCCESS", "save": {"kit_name": "Samsung Galaxy A04e"}},
            "5": {"next": "MITSINJO_ACHAT_SUCCESS", "save": {"kit_name": "Samsung Galaxy A15"}},
            "0": "MITSINJO_MENU"
        }
    },
    "MITSINJO_ACHAT_SUCCESS": {
        "title": "Succès",
        "text": "Demande envoyée pour {kit_name}, vous allez recevoir un SMS pour confirmation.",
        "type": "message"
    },
    "MITSINJO_PAIEMENT_MENU": {
        "title": "Paiement",
        "text": "1 - Mon compte\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MITSINJO_PAIEMENT_NUMERO",
            "0": "MITSINJO_MENU"
        }
    },
    "MITSINJO_PAIEMENT_NUMERO": {
        "title": "Paiement",
        "text": "Entrer le numero de kit :",
        "type": "input",
        "save_as": "kit_num",
        "next": "MITSINJO_PAIEMENT_COMPUTE"
    },
    "MITSINJO_PAIEMENT_COMPUTE": {
        "type": "compute",
        "action": "get_mitsinjo_payment_details",
        "next": "MITSINJO_PAIEMENT_CONFIRM"
    },
    "MITSINJO_PAIEMENT_CONFIRM": {
        "title": "Paiement",
        "text": "Pour effectuer le paiement du {kit_name} qui porte le numero {kit_num}, pour un prix de {kit_paiement}. Veuillez entrer votre mot de passe.",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },

    # --- 2. MOOZIK ---
    "MOOZIK_MENU": {
        "title": "Moozik",
        "text": "1 - Achat pour mon numéro depuis mon crédit Yas\n2 - Offre pour mon numéro via Mvola\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MOOZIK_UNAVAILABLE",
            "2": "MOOZIK_UNAVAILABLE",
            "0": "PRODUITS_DIV_MENU"
        }
    },
    "MOOZIK_UNAVAILABLE": {
        "title": "Service",
        "text": "Service temporairement indisponible",
        "type": "message"
    },

    # --- 3. ZARA SOA ---
    "ZARA_SOA_MENU": {
        "title": "Zara Soa",
        "text": "Vérifier votre éligibilité\n1 - Oui\n2 - Non\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "ZARA_SOA_SUCCESS",
            "2": "PRODUITS_DIV_MENU",
            "0": "PRODUITS_DIV_MENU"
        }
    },
    "ZARA_SOA_SUCCESS": {
        "title": "Zara Soa",
        "text": "Vous allez recevoir un SMS de notre part, veuillez patienter.",
        "type": "message"
    },

    # --- 4. MBALIK ---
    "MBALIK_MENU": {
        "title": "MBalik",
        "text": "1 - Achat de kit\n2 - Achat recharge\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MBALIK_ACHAT_PIN",
            "2": "MBALIK_RECHARGE_MENU",
            "0": "PRODUITS_DIV_MENU"
        }
    },
    "MBALIK_ACHAT_PIN": {
        "title": "Mvola",
        "text": "Pour voir les kits proposés, entrer votre code secret Mvola :",
        "type": "input",
        "save_as": "pin",
        "next": "MBALIK_KITS_LIST"
    },
    "MBALIK_KITS_LIST": {
        "title": "Kits disponibles",
        "text": "1 - MBalik Pro\n2 - MBalik Boom\n3 - MBalik Home 40 Plus\n4 - MBalik Wow 60\n5 - MBalik Solar Fan\n6 - MBalik Home 200X Plus\n7 - MBalik WOW TV + TV 32\"\n8 - MBalik Home 500X + TV\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "1"}},
            "2": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "2"}},
            "3": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "3"}},
            "4": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "4"}},
            "5": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "5"}},
            "6": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "6"}},
            "7": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "7"}},
            "8": {"next": "MBALIK_KIT_DETAIL_COMPUTE", "save": {"kit_id": "8"}},
            "0": "MBALIK_MENU"
        }
    },
    "MBALIK_KIT_DETAIL_COMPUTE": {
        "type": "compute",
        "action": "get_mbalik_kit_details",
        "next": "MBALIK_KIT_DETAIL_VIEW"
    },
    "MBALIK_KIT_DETAIL_VIEW": {
        "title": "{kit_name}",
        "text": "{mbalik_msg}\n\n1 - Être contacté\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MBALIK_CONTACT_SUCCESS",
            "0": "MBALIK_KITS_LIST"
        }
    },
    "MBALIK_CONTACT_SUCCESS": {
        "title": "MBalik",
        "text": "Votre demande est en cours d'exécution, vous allez recevoir un SMS.",
        "type": "message"
    },
    "MBALIK_RECHARGE_MENU": {
        "title": "Payer / Recharger mon kit",
        "text": "1 - Payer pour 1 jour\n2 - Payer pour 7 jours\n3 - Payer pour 30 jours\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "MBALIK_RECHARGE_COMPUTE", "save": {"duree": "1"}},
            "2": {"next": "MBALIK_RECHARGE_COMPUTE", "save": {"duree": "7"}},
            "3": {"next": "MBALIK_RECHARGE_COMPUTE", "save": {"duree": "30"}},
            "0": "MBALIK_MENU"
        }
    },
    "MBALIK_RECHARGE_COMPUTE": {
        "type": "compute",
        "action": "get_mbalik_recharge_details",
        "next": "MBALIK_RECHARGE_CONFIRM"
    },
    "MBALIK_RECHARGE_CONFIRM": {
        "title": "Confirmation",
        "text": "Confirmez-vous le paiement de {recharge_price} Ar pour recharger votre kit {kit_name} pour {recharge_duree} jours ?\n1 - Oui\n2 - Non",
        "type": "choice",
        "options": {
            "1": "MBALIK_RECHARGE_PIN",
            "2": "MBALIK_RECHARGE_MENU"
        }
    },
    "MBALIK_RECHARGE_PIN": {
        "title": "Mvola",
        "text": "Pour confirmer le paiement, Entrer votre code secret Mvola :",
        "type": "input",
        "save_as": "pin",
        "next": "MVOLA_SUCCESS"
    },
    "BEST_OFFERS_MENU": {
        "title": "Meilleure Offre",
        "text": "Merci d'avoir choisi YAS. Tapez #322# pour aheter une offre",
        "type": "message"
    },
    # --- 8. MON IDENTITÉ ---
    "IDENTITY_MENU": {
        "title": "MON IDENTITÉ",
        "text": "Votre numéro mobile est {numero} attribué à {nom} qui porte le numéro CIN {numero_cin}.\n\nSouhaitez-vous recevoir ces informations par SMS ?\n1 - Oui\n2 - Non",
        "type": "choice",
        "options": {
            "1": "IDENTITY_SMS_SUCCESS",
            "2": "MAIN_MENU"
        }
    },
    "IDENTITY_SMS_SUCCESS": {
        "title": "MON IDENTITÉ",
        "text": "Votre demande a bien été prise en compte. Vous allez recevoir un SMS contenant vos informations.",
        "type": "message"
    },

    # --- 9. CONFIGURER MON MOBILE ---
    "CONFIG_MOBILE": {
        "type": "logic",
        "conditions": [
            {"if": {"internet_active": True}, "then": "CONFIG_INTERNET_DISABLE_PROMPT"},
            {"else": "CONFIG_INTERNET_ENABLE_PROMPT"}
        ]
    },
    
    "CONFIG_INTERNET_DISABLE_PROMPT": {
        "title": "CONFIGURATION",
        "text": "Voulez-vous désactiver l'utilisation d'internet via votre compte principal ?\n1 - Oui, désactiver\n2 - Non, annuler",
        "type": "choice",
        "options": {
            "1": "CONFIG_INTERNET_DISABLE_EXEC",
            "2": "CONFIG_CANCEL"
        }
    },
    "CONFIG_INTERNET_ENABLE_PROMPT": {
        "title": "CONFIGURATION",
        "text": "Voulez-vous activer l'utilisation d'internet via votre compte principal ?\n1 - Oui, activer\n2 - Non, annuler",
        "type": "choice",
        "options": {
            "1": "CONFIG_INTERNET_ENABLE_EXEC",
            "2": "CONFIG_CANCEL"
        }
    },

    "CONFIG_INTERNET_DISABLE_EXEC": {
        "type": "compute",
        "action": "disable_internet",
        "next": "CONFIG_DISABLE_SUCCESS"
    },
    "CONFIG_INTERNET_ENABLE_EXEC": {
        "type": "compute",
        "action": "enable_internet",
        "next": "CONFIG_ENABLE_SUCCESS"
    },

    "CONFIG_DISABLE_SUCCESS": {
        "title": "CONFIGURATION",
        "text": "L'utilisation d'internet via votre compte principal a été désactivée avec succès.",
        "type": "message"
    },
    "CONFIG_ENABLE_SUCCESS": {
        "title": "CONFIGURATION",
        "text": "L'utilisation d'internet via votre compte principal a été activée avec succès.",
        "type": "message"
    },
    "CONFIG_CANCEL": {
        "title": "CONFIGURATION",
        "text": "Opération annulée. Aucune modification n'a été apportée à votre configuration.",
        "type": "message"
    },
    
    # --- CONSULTATION SOLDE ET HISTORIQUE ---
    "MVOLA_CONSULTER_SOLDE": {
        "title": "CONSULTER SOLDE",
        "text": "💰 SOLDES ACTUELS\n\nMVola: {solde_mvola} Ar\nCompte Principal: {solde_principal} Ar\nÉpargne: {solde_epargne} Ar\n\nNom: {nom}\nNuméro: {numero}\n\n0 - Retour",
        "type": "choice",
        "options": {
            "0": "MVOLA_MAIN"
        }
    },
    
    "MVOLA_HISTORIQUE": {
        "title": "HISTORIQUE",
        "text": "📜 Historique des transactions (voir terminal)\n\n0 - Retour",
        "type": "choice",
        "options": {
            "0": "MVOLA_MAIN"
        }
    },
    
    # --- A PROPOS / CREDITS ---
    "MENU_CREDITS": {
        "title": "A PROPOS",
        "text": "YAS USSD Simulator v1.0\n\nDéveloppé par : Narindra Ranjalahy\nAnnée : 2026\n\nMerci d'utiliser cette application !\n\n0 - Retour",
        "type": "choice",
        "options": {
            "0": "MAIN_MENU"
        }
    },

    # --- MENUS #359# ---
    "MENU_359": {
        "title": "YAS",
        "text": "Votre crédit est : {solde_principal} Ar valable jusqu'au {validite_credit}\n1 - Mes offres\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "MENU_359_OFFRES",
            "0": "MAIN_MENU"
        }
    },
    
    "MENU_359_OFFRES": {
        "title": "MES OFFRES",
        "text": "Vos offres :\n{liste_offres}\n0 - Retour",
        "type": "choice",
        "options": {
            "0": "MENU_359"
        }
    },
    
    # --- PROMOTIONS & ACHAT VIA COMPTE PRINCIPAL ---
    "PROMOTION_MENU": {
        "title": "OFFRES YAS",
        "text": "Acheter un forfait (Solde Principal: {solde_principal} Ar)\n1 - MORA (VOIX - SMS - INTERNET)\n2 - FIRST (VOIX - SMS - INTERNET)\n3 - YELOW (SMS - INTERNET)\n4 - YAS NET (INTERNET)\n0 - Retour",
        "type": "choice",
        "options": {
            "1": "OFFER_MAIN_MORA",
            "2": "OFFER_MAIN_FIRST",
            "3": "OFFER_MAIN_YELLOW",
            "4": "OFFER_MAIN_NET",
            "0": "MAIN_MENU"
        }
    },
    
    # --- OFFRES VIA COMPTE PRINCIPAL (Duplication structure sans PIN) ---
    "OFFER_MAIN_MORA": {
        "title": "Les Offres Mora",
        "text": "1. M'ora 500\n2. M'ora One\n3. M'ora +5000\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "M'ora 500", "off_price": "500 Ar", "off_cat": "MORA"}},
            "2": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "M'ora One", "off_price": "1 000 Ar", "off_cat": "MORA"}},
            "3": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "M'ora +5000", "off_price": "5 000 Ar", "off_cat": "MORA"}},
            "0": "PROMOTION_MENU"
        }
    },
    "OFFER_MAIN_FIRST": {
        "title": "Les Offres First",
        "text": "1. First Premium\n2. First Premium +\n3. First Prestige\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "First Premium", "off_price": "10 000 Ar", "off_cat": "FIRST"}},
            "2": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "First Premium +", "off_price": "15 000 Ar", "off_cat": "FIRST"}},
            "3": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "First Prestige", "off_price": "30 000 Ar", "off_cat": "FIRST"}},
            "0": "PROMOTION_MENU"
        }
    },
    "OFFER_MAIN_YELLOW": {
        "title": "Les Offres Ye'low",
        "text": "1. Ye'low 100\n2. Ye'low 200\n3. Ye'low SMS\n4. Ye'low 500\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Ye'low 100", "off_price": "100 Ar", "off_cat": "YELLOW"}},
            "2": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Ye'low 200", "off_price": "200 Ar", "off_cat": "YELLOW"}},
            "3": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Ye'low SMS", "off_price": "200 Ar", "off_cat": "YELLOW"}},
            "4": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Ye'low 500", "off_price": "500 Ar", "off_cat": "YELLOW"}},
            "0": "PROMOTION_MENU"
        }
    },
    "OFFER_MAIN_NET": {
        "title": "Les Offres Net",
        "text": "1. Net Week 3000\n2. Net Week 5000\n3. Net Month 15 000\n0 - Retour",
        "type": "choice",
        "options": {
            "1": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Net Week 3000", "off_price": "3 000 Ar", "off_cat": "YAS_NET"}},
            "2": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Net Week 5000", "off_price": "5 000 Ar", "off_cat": "YAS_NET"}},
            "3": {"next": "OFFER_MAIN_CONFIRM", "save": {"off_name": "Net Month 15 000", "off_price": "15 000 Ar", "off_cat": "YAS_NET"}},
            "0": "PROMOTION_MENU"
        }
    },
    
    "OFFER_MAIN_CONFIRM": {
        "title": "CONFIRMATION",
        "text": "Acheter {off_name} pour {off_price} ?\n(Débit Compte Principal)\n\n1 - Confirmer\n2 - Annuler",
        "type": "choice",
        "options": {
            "1": "OFFER_MAIN_SUCCESS_PROCESS",
            "2": "PROMOTION_MENU"
        }
    },
    
    "OFFER_MAIN_SUCCESS_PROCESS": {
        "type": "compute",
        "action": "buy_offer_main",
        "next": "OFFER_MAIN_MSG"
    },
    
    "OFFER_MAIN_MSG": {
        "title": "FELICITATIONS",
        "text": "Achat réussi ! {off_message}",
        "type": "message"
    }
};
