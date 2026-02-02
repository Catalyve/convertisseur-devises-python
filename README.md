# Convertisseur de Devises

Convertisseur de devises est une application graphique développée en **Python** avec **PySide6**.  
Elle permet de convertir des montants entre différentes monnaies, d’afficher le taux de change en temps réel et de conserver un historique clair des conversions.

Projet conçu comme une application **simple, robuste et exploitable**, adaptée à un usage pédagogique, démonstratif ou portfolio.

---

## Objectif

Ce projet a été conçu afin de démontrer :

- la création d’une **interface graphique moderne** avec PySide6
- la structuration propre d’une application Python orientée UI
- l’intégration d’une **bibliothèque externe de données financières**
- la gestion d’événements utilisateurs (signals / slots)
- la production d’un outil **fonctionnel et immédiatement utilisable**

---

## Fonctionnalités

- Conversion instantanée entre plus de **160 devises**
- Sélection des devises source et cible
- Affichage du **taux de change actuel**
- Inversion rapide des devises
- Historique chronologique des conversions
- Copie du résultat dans le presse-papiers
- Interface stylisée via **QSS**
- Icône d’application personnalisée

---

## Logique de fonctionnement

- Les devises disponibles sont chargées automatiquement depuis `currency-converter`
- Chaque interaction utilisateur (montant, devise) déclenche un recalcul
- Les erreurs de taux manquants sont gérées via une alerte graphique
- L’historique conserve les conversions les plus récentes en tête de liste
- Le style graphique est dissocié du code via un fichier `.qss`

---

## Structure du projet

```text
convertisseur_devises/
│
├── app/
│   ├── app.py
│   │
│   └── styles/
│       ├── style.qss
│       └── logo.png
│
├── env/      # Environnement virtuel (non versionné)
│
└── README.md
```

---

## Technologies utilisées

- **Python 3**
- **PySide6** (Qt for Python)
- **currency-converter**
- **Qt Style Sheets (QSS)**

---

## Installation

### Installation rapide

```bash
pip install PySide6 currencyconverter
```

### Installation recommandée (venv)

**Windows (PowerShell)**

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install PySide6 currencyconverter
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install PySide6 currencyconverter
```

---

## Lancer l'application

```bash
python main.py
```

L’interface graphique s’ouvre automatiquement.

---

## Remarques

- Les taux sont accessibles hors ligne (selon les devises)
- Certaines devises peuvent être indisponibles selon la source
- Projet volontairement simple pour rester lisible et maintenable

---

## Améliorations possibles

- Mode sombre / clair dynamique
- Export de l’historique (CSV / TXT)
- Interface verticale ou responsive
- Ajout d’un graphique d’évolution des taux
- Génération d’un exécutable (.exe)

---

## Licence

License MIT
