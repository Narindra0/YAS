
# 📱 YAS USSD Ecosystem  
## Madagascar Mobile Services Simulator

---

## 🏛️ Présentation générale

**YAS USSD Ecosystem** est un projet de simulation logicielle **à haute fidélité** visant à reproduire le fonctionnement réel des services USSD proposés par l’opérateur **YAS Madagascar**, incluant les services financiers **MVola**.

Ce projet a été conçu comme une **preuve de concept technique**, démontrant la capacité à modéliser :
- des flux transactionnels complexes,
- des menus USSD arborescents multi-niveaux,
- une gestion persistante et sécurisée des comptes utilisateurs,
- une séparation claire entre interface, logique métier et données.

Contrairement aux scripts USSD simplifiés, ce simulateur adopte une approche **orientée architecture logicielle**, proche des standards utilisés dans les systèmes télécoms et fintech.

---

## 🎯 Objectifs du projet

- Simuler fidèlement l’expérience utilisateur USSD
- Implémenter un moteur transactionnel sécurisé
- Mettre en œuvre une architecture modulaire et évolutive
- Fournir un socle technique réutilisable pour d’autres opérateurs ou services
- Servir de projet académique et professionnel démontrant une maîtrise avancée de Python

---

## 🚀 Fonctionnalités principales

### 💳 Module MVola – Mobile Money

Le module MVola simule une plateforme complète de **Mobile Banking** :

- **Transfert de fonds**
  - Envoi d’argent entre comptes utilisateurs
  - Calcul automatique et dynamique des frais de transaction
  - Vérification du solde avant validation

- **Paiements marchands**
  - Paiement de services (JIRAMA, CANAL+, Internet, etc.)
  - Simulation d’APIs fournisseurs
  - Génération de reçus transactionnels

- **Sécurité**
  - Authentification par code PIN
  - Masquage des entrées sensibles
  - Blocage des opérations en cas d’erreur critique

- **Historique financier**
  - Journal horodaté de toutes les opérations
  - Catégorisation pour audit et suivi

---

### 📶 Services Télécom & Forfaits

- **Moteur USSD dynamique**
  - Navigation fluide dans les menus (#111#, #359#)
  - Gestion du retour arrière et annulation
  - Conservation du contexte utilisateur

- **Catalogue d’offres**
  - Gammes M’ora, First, Yellow
  - Offres Data, Voix et SMS

- **Gestion du crédit**
  - Consultation du solde principal
  - Recharge par code secret
  - Suivi de validité de la ligne

- **Provisionnement automatique**
  - Activation immédiate des bonus
  - Mise à jour en temps réel du profil utilisateur

---

## 🛠️ Architecture technique

Le projet repose sur une **architecture N-Tier simplifiée**, facilitant :
- la maintenance,
- l’évolution,
- la migration vers un environnement de production.

### 📂 Structure du projet

```
YAS-USSD/
├── src/
│   ├── main.py              # Point d’entrée CLI
│   ├── interface.py         # Interface graphique (GUI)
│   ├── ussd_engine.py       # Cœur logique USSD (State Machine)
│   └── utils.py             # Fonctions utilitaires
│
├── data/
│   ├── ussd_menus.py        # Arborescence USSD
│   └── tarifs.py            # Offres, coûts et bonus
│
├── storage/
│   └── user_profile.json    # Persistance NoSQL simulée
│
└── README.md
```

---

## ⚙️ Choix technologiques

- **Langage** : Python 3.10+
- **Interface graphique** : CustomTkinter (Dark Mode)
- **Persistance** : JSON (NoSQL simulé)
- **Logique métier** : Machine à états (State Machine)
- **Architecture** : Séparation UI / Business Logic / Data

---

## 📋 Spécifications des données

Le fichier `user_profile.json` est le registre central.

| Attribut | Type | Description |
|--------|------|------------|
| mvola_balance | Integer | Solde MVola |
| main_balance | Integer | Crédit télécom |
| active_offers | Object | Quotas et expirations |
| history | List | Historique des actions |

---

## ⚙️ Installation et exécution

### Dépendances

```bash
pip install customtkinter
```

### Lancement

- Mode GUI :
```bash
python interface.py
```

- Mode CLI :
```bash
python main.py
```

---

## 🔐 Sécurité & intégrité

- Validation systématique des soldes
- Atomicité des opérations
- Sauvegarde automatique après chaque action critique
- Prévention des incohérences de données

---

## 📈 Roadmap

- [ ] Migration SQLite (multi-utilisateurs)
- [ ] Tableau de bord statistiques
- [ ] Interface administrateur opérateur
- [ ] Simulation réseau USSD en temps réel

---

## 👨‍💻 Auteur

**Narindra Ranjalahy**  
Ingénierie logicielle & Développement Python  
Promotion 2026

---

_Ce projet est une initiative éducative démontrant la maîtrise des systèmes USSD, télécoms et fintech._
