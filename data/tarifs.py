"""
YAS USSD Simulator - Tariff Data
Copyright (c) 2026 Narindra Ranjalahy
All rights reserved.

This software is the property of Narindra Ranjalahy.
Educational/Personal use only.
"""

OFFRES = {
    "MORA": {
        "M'ora 500": {"prix": "500 Ar", "appels": "500 Ar", "data": "25 Mo", "sms": "25", "validite": "1 jour"},
        "M'ora One": {"prix": "1 000 Ar", "appels": "1 000 Ar", "data": "40 Mo", "sms": "40", "validite": "1 jour"},
        "M'ora +5000": {"prix": "5 000 Ar", "appels": "5 000 Ar", "data": "200 Mo", "sms": "100", "validite": "7 jours"},
        "M'ora International": {"prix": "5 000 Ar", "appels": "15 min (Int.)", "data": "0", "sms": "0", "validite": "24 H"}
    },
    "FIRST": {
        "First Premium": {"prix": "10 000 Ar", "appels": "10 000 Ar", "data": "350 Mo", "sms": "100", "validite": "30 Jours"},
        "First Premium +": {"prix": "15 000 Ar", "appels": "15 000 Ar", "data": "500 Mo", "sms": "150", "validite": "30 Jours"},
        "First Prestige": {"prix": "30 000 Ar", "appels": "30 000 Ar", "data": "1 Go", "sms": "400", "validite": "30 Jours"},
        "First Royal": {"prix": "50 000 Ar", "appels": "50 000 Ar", "data": "2 Go", "sms": "700", "validite": "30 Jours"}
    },
    "YELLOW": {
        "Ye'low 100": {"prix": "100 Ar", "appels": "0", "data": "20 Mo", "sms": "20", "validite": "1 jour"},
        "Ye'low SMS": {"prix": "200 Ar", "appels": "0", "data": "0", "sms": "100 sms vers numero YAS + 25 sms vers toutes operateurs", "validite": "24 H"},
        "Ye'low 200": {"prix": "200 Ar", "appels": "0", "data": "40 Mo", "sms": "40", "validite": "24 H"},
        "Ye'low 500": {"prix": "500 Ar", "appels": "0", "data": "100 Mo", "sms": "0", "validite": "24 H"},
        "Ye'low One": {"prix": "1 000 Ar", "appels": "0", "data": "1 Go", "sms": "0", "validite": "24 H"},
        "Ye'low 1000": {"prix": "1 000 Ar", "appels": "0", "data": "100 Mo", "sms": "100", "validite": "30 Jours"},
        "Ye'low 2000": {"prix": "2 000 Ar", "appels": "0", "data": "450 Mo", "sms": "0", "validite": "48 H"}
    },
    "YAS_NET": {
        "Net Week 3000": {"prix": "3 000 Ar", "appels": "0", "data": "550 Mo", "sms": "0", "validite": "7 jours"},
        "Net Week 5000": {"prix": "5 000 Ar", "appels": "0", "data": "1 Go", "sms": "0", "validite": "7 jours"},
        "Net Week 10 000": {"prix": "10 000 Ar", "appels": "0", "data": "2,2 Go", "sms": "0", "validite": "7 jours"},
        "Net Month 15 000": {"prix": "15 000 Ar", "appels": "0", "data": "2,5 Go", "sms": "0", "validite": "30 jours"},
        "Net Month 25 000": {"prix": "25 000 Ar", "appels": "0", "data": "4,5 Go", "sms": "0", "validite": "30 jours"},
        "Net Month 75 000": {"prix": "75 000 Ar", "appels": "0", "data": "15 Go", "sms": "0", "validite": "30 jours"},
        "Net Month 125 000": {"prix": "125 000 Ar", "appels": "0", "data": "29 Go", "sms": "0", "validite": "30 jours"},
        "Net Month 175 000": {"prix": "175 000 Ar", "appels": "0", "data": "58 Go", "sms": "0", "validite": "30 jours"},
        "Net Month 200 000": {"prix": "200 000 Ar", "appels": "0", "data": "100 Go", "sms": "0", "validite": "30 jours"}
    },
    "ROAMING": {
        "Roaming Run": {"prix": "12 000 Ar", "appels": "12 000 Ar", "data": "1 Go", "sms": "5", "validite": "30 jours", "note": "Appels/SMS vers numéros étrangers"},
        "Roaming Jump": {"prix": "60 000 Ar", "appels": "60 000 Ar", "data": "6,5 Go", "sms": "15", "validite": "30 jours", "note": "Appels/SMS vers numéros étrangers"},
        "Roaming Win": {"prix": "100 000 Ar", "appels": "100 000 Ar", "data": "12 Go", "sms": "20", "validite": "30 jours", "note": "Appels/SMS vers numéros étrangers"}
    }
}

# Frais de Retrait (pour le destinataire)
FRAIS_RETRAIT = [
    {"max": 1000, "frais": 100},
    {"max": 5000, "frais": 150},
    {"max": 10000, "frais": 275},
    {"max": 20000, "frais": 550},
    {"max": 25000, "frais": 650},
    {"max": 50000, "frais": 1300},
    {"max": 100000, "frais": 1900},
    {"max": 250000, "frais": 3400},
    {"max": 500000, "frais": 4700},
    {"max": 1000000, "frais": 8800},
    {"max": 2000000, "frais": 14700},
    {"max": 20000000, "frais": 20000},
]

# Frais de Transfert vers MVola
FRAIS_TRANSFERT_MVOLA = [
    {"max": 5000, "frais": 70},
    {"max": 10000, "frais": 150},
    {"max": 25000, "frais": 250},
    {"max": 20000000, "frais": 500},
]

# Frais de Transfert vers Autres Opérateurs
FRAIS_TRANSFERT_AUTRES = [
    {"max": 1000, "frais": 200},
    {"max": 5000, "frais": 250},
    {"max": 10000, "frais": 500},
    {"max": 25000, "frais": 1000},
    {"max": 50000, "frais": 1500},
    {"max": 100000, "frais": 2000},
    {"max": 250000, "frais": 3500},
    {"max": 500000, "frais": 5000},
    {"max": 1000000, "frais": 8500},
    {"max": 2000000, "frais": 12000},
    {"max": 3000000, "frais": 14500},
    {"max": 4000000, "frais": 19500},
    {"max": 5000000, "frais": 24000},
    {"max": 20000000, "frais": 0},
]

# YAS MITSINJO Kits
YAS_MITSINJO_KITS = {
    "1": {"name": "ZTE A36", "price": "269 000 Ar", "paiement": "1 200 Ar / jour"},
    "2": {"name": "ZTE A76 4G", "price": "389 000 Ar", "paiement": "1 700 Ar / jour"},
    "3": {"name": "ZTE Blade A76 5G", "price": "490 000 Ar", "paiement": "1 900 Ar / jour"},
    "4": {"name": "Samsung Galaxy A04e", "price": "(Postpayé)", "paiement": "Contrat Telma Shop", "acompte": "150 000 Ar"},
    "5": {"name": "Samsung Galaxy A15", "price": "(Postpayé)", "paiement": "Contrat Telma Shop", "acompte": "200 000 Ar"},
}

# MBalik Kits
MBALIK_KITS = {
    "1": {"name": "MBalik Pro", "price": "149 000 Ar", "acompte": "15 000 Ar", "daily": "500 Ar", "duration": "Jusqu'à paiement total"},
    "2": {"name": "MBalik Boom", "price": "189 000 Ar", "acompte": "Variable", "daily": "Variable", "duration": "Jusqu'à paiement total"},
    "3": {"name": "MBalik Home 40 Plus", "price": "219 000 Ar", "acompte": "28 000 Ar", "daily": "800 Ar", "duration": "Jusqu'à paiement total"},
    "4": {"name": "MBalik Wow 60", "price": "299 000 Ar", "acompte": "Variable", "daily": "Variable", "duration": "Jusqu'à paiement total"},
    "5": {"name": "MBalik Solar Fan", "price": "389 000 Ar", "acompte": "46 000 Ar", "daily": "Variable", "duration": "Jusqu'à paiement total"},
    "6": {"name": "MBalik Home 200X Plus", "price": "529 000 Ar", "acompte": "Sur devis", "daily": "Variable", "duration": "Jusqu'à paiement total"},
    "7": {"name": "MBalik WOW TV + TV 32\"", "price": "1 759 000 Ar", "acompte": "Sur devis", "daily": "Variable", "duration": "Jusqu'à paiement total"},
    "8": {"name": "MBalik Home 500X + TV", "price": "1 899 000 Ar", "acompte": "Sur devis", "daily": "Variable", "duration": "Jusqu'à paiement total"}
}

# MBalik Recharges
MBALIK_RECHARGES = {
    "1": "1 500",
    "7": "10 000",
    "30": "40 000"
}
