# 📱 YAS USSD - Système de Services Mobiles Complet

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](README.md)

## 📖 À Propos du Projet

**YAS USSD** est une **remake complète et fonctionnelle** du système USSD de **YAS Madagascar** (anciennement **Telma Madagascar**). Ce projet reproduit fidèlement l'ensemble des services mobiles proposés par l'opérateur, incluant :

- 💰 **MVola** - Système de paiement mobile complet
- 📞 **Gestion de compte** - Consultation solde, recharge, forfaits
- 🎁 **Offres promotionnelles** - Forfaits M'ora, First, Yellow
- 💸 **Transferts d'argent** - Entre comptes MVola et vers d'autres opérateurs
- 📊 **Historique des transactions** - Suivi complet de toutes les opérations
- 🔐 **Sécurité** - Authentification par code PIN

Ce simulateur offre une expérience utilisateur authentique avec deux modes d'interaction : une **interface en ligne de commande (CLI)** pour des tests rapides et une **interface graphique moderne (GUI)** pour une expérience visuelle complète.

---

## 👨‍💻 Développeur

**Narindra Ranjalahy**  
Développement complet du système - 2026

---

## 🎯 Fonctionnalités Principales

### 💰 Services MVola

- ✅ **Transfert d'argent** - Envoi et réception de fonds
- ✅ **Paiement de factures** - Électricité, eau, Internet, etc.
- ✅ **Achat de crédit** - Recharge téléphonique
- ✅ **Consultation solde MVola** - Vérification du compte
- ✅ **Historique des transactions** - Suivi complet
- ✅ **Gestion de code PIN** - Modification sécurisée

### 📞 Services Téléphoniques

- ✅ **Consultation crédit** - Solde principal et validité
- ✅ **Achat d'offres** - M'ora, First, Yellow
- ✅ **Gestion des forfaits actifs** - Suivi data/SMS/appels
- ✅ **Codes USSD** - `#144#`, `#111#`, `#359#`, etc.
- ✅ **Tarification dynamique** - Grilles tarifaires réalistes

### 🎁 Système d'Offres

- ✅ **Offres M'ora & First** - Forfaits Internet et SMS
- ✅ **Offres Yellow** - Forfaits voix (appels)
- ✅ **Expiration automatique** - Gestion des dates de validité
- ✅ **Compteurs en temps réel** - Data/SMS/Appels restants
- ✅ **Affichage conditionnel** - Menu dynamique selon offres actives

---

## 📁 Structure du Projet

```
YAS USSD CODE/
│
├── 📂 src/                     # Code source principal
│   ├── main.py                 # Point d'entrée CLI
│   ├── interface.py            # Point d'entrée GUI
│   ├── ussd_engine.py          # Moteur USSD (logique centrale)
│   └── utils.py                # Fonctions utilitaires partagées
│
├── 📂 data/                    # Données statiques
│   ├── ussd_menus.py           # Définition des menus USSD
│   └── tarifs.py               # Grilles tarifaires détaillées
│
├── 📂 storage/                 # Données utilisateur
│   └── user_profile.json       # Profil utilisateur (solde, PIN, offres)
│
├── main.py                     # 🚀 Lanceur CLI
├── interface.py                # 🚀 Lanceur GUI
└── README.md                   # Documentation
```

---

## 🚀 Installation et Utilisation

### Prérequis

- **Python 3.8+** 
- **customtkinter** (pour l'interface graphique)

### Installation

```bash
# Cloner ou télécharger le projet
cd "YAS USSD CODE"

# Installer les dépendances
pip install customtkinter
```

### Lancement

#### Mode CLI (Terminal)
Interface en ligne de commande pour tests rapides et débogage :
```bash
python main.py
```

#### Mode GUI (Interface Graphique)
Interface moderne avec design visuel :
```bash
python interface.py
```

---

## 🎮 Guide d'Utilisation

### Codes USSD Principaux

| Code | Description |
|------|-------------|
| `#144#` | Menu principal MVola |
| `#111#` | Consultation solde et recharge |
| `#359#` | Mes offres actives (data/SMS/appels) |
| `#Forfait#` | Codes directs pour achats de forfaits |

### Informations de Test

- **Code PIN par défaut** : `1234`
- **Profil utilisateur** : `storage/user_profile.json`
- **Solde initial** : Configurable dans le JSON

### Opérations Disponibles

1. **Transfert d'argent** - Envoyer de l'argent entre comptes
2. **Achat de crédit** - Recharger son compte
3. **Paiement factures** - Services (électricité, eau, etc.)
4. **Consultation solde** - MVola, crédit principal, validité
5. **Gestion d'offres** - Achat et suivi de forfaits
6. **Historique** - Toutes les transactions effectuées

---

## 🏗️ Architecture Technique

### Conception Modulaire

Le projet suit une architecture **sans duplication de code** :

- **`ussd_engine.py`** - Contient toute la logique métier USSD
- **`utils.py`** - Fonctions utilitaires partagées
- **`main.py` & `interface.py`** - Interfaces légères utilisant le moteur

### Principes de Design

- ✅ **Séparation des préoccupations** - Logique / Présentation
- ✅ **Réutilisabilité** - Un seul moteur pour toutes les interfaces
- ✅ **Extensibilité** - Facile d'ajouter de nouvelles fonctionnalités
- ✅ **Maintenabilité** - Code organisé et documenté

### Flux de Navigation

```
Code USSD → ussd_engine.py → Traitement → Retour résultat
                ↓
         user_profile.json (mise à jour)
```

---

## 📊 Données et Persistance

### Format de Stockage

Les données utilisateur sont stockées dans `storage/user_profile.json` :

```json
{
  "phone": "034 XX XXX XX",
  "nom": "Utilisateur",
  "prenom": "Test",
  "mvola_balance": 50000,
  "main_account_balance": 5000,
  "pin": "1234",
  "credit_validity": "2026-12-31",
  "active_offers": [],
  "transaction_history": []
}
```

### Gestion des Transactions

Toutes les opérations sont enregistrées avec :
- 📅 Date et heure
- 💰 Montant et type d'opération
- 📝 Description détaillée
- ✅ Statut (succès/échec)

---

## 🔒 Sécurité

- 🔐 **Authentification PIN** - Requis pour opérations sensibles
- 🚫 **Validation des montants** - Vérification solde disponible
- 📊 **Traçabilité** - Historique complet des opérations
- ⏱️ **Expiration des offres** - Gestion automatique

---

## 🎓 Contexte

Ce projet a été développé dans un cadre **pédagogique** pour démontrer :

- La conception d'un système USSD complet
- L'architecture logicielle modulaire
- La gestion de données utilisateur
- La création d'interfaces multiples (CLI/GUI)

**Note** : Il s'agit d'une simulation à des fins éducatives. Pour un système en production, des mesures de sécurité supplémentaires seraient nécessaires (chiffrement, authentification serveur, etc.).

---

## 🚀 Évolutions Futures

- [ ] Intégration base de données (SQLite/MySQL)
- [ ] API REST pour services web
- [ ] Application mobile native
- [ ] Système d'authentification multi-facteurs
- [ ] Rapports et statistiques avancés

---

## 📝 Licence

**Projet Éducatif** - Libre d'utilisation à des fins d'apprentissage

---

## 📞 Contact

Pour toute question ou suggestion concernant ce projet :

**Narindra Ranjalahy**  
Développeur du projet YAS USSD

---

<div align="center">

**⭐ Si ce projet vous a été utile, n'hésitez pas à le partager ! ⭐**

*Développé avec passion pour l'apprentissage* 🚀

</div>
