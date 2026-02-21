<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/XGBoost-ML-orange?logo=xgboost" />
  <img src="https://img.shields.io/badge/Flask-API-lightgrey?logo=flask" />
  <img src="https://img.shields.io/badge/scikit--learn-ML-f7931e?logo=scikitlearn&logoColor=white" />
</p>

# 🎓 Prédiction de la Performance des Étudiants Marocains

> **Projet de fin de module** — Master Big Data & Data Science  
> Année Universitaire 2025–2026

Application web de prédiction de la **moyenne annuelle** des lycéens marocains, basée sur un pipeline complet de Machine Learning : collecte, nettoyage, analyse exploratoire, modélisation et déploiement.

## 📸 Aperçu

| Hero | Prédiction |
|:---:|:---:|
| ![Hero](static/images/hero.png) | ![Prediction](static/images/prediction.png) |

## ✨ Fonctionnalités

- 🔍 **Pipeline ML complet** : Collecte → Nettoyage → EDA → Modélisation → Évaluation → Déploiement
- 🧠 **Prédiction interactive** : Formulaire à 35 features avec résultat en temps réel (gauge animée)
- 📊 **6 modèles comparés** : Régression Linéaire, Ridge, Lasso, Random Forest, XGBoost, MLP
- ⭐ **Meilleur modèle** : XGBoost (Tuned) — R² = 0.1827
- 🎨 **Interface premium** : Dark theme, glassmorphism, animations fluides
- 📈 **SHAP Values** : Interprétabilité du modèle

## 📁 Structure du Projet

```
├── api.py                          # 🚀 Flask API (serveur web)
├── static/
│   ├── index.html                  # 🎨 Interface web (SPA)
│   ├── style.css                   # 💅 Styles (dark glassmorphism)
│   └── script.js                   # ⚡ Animations & logique
├── code/
│   ├── clean_data.ipynb            # 🧹 Nettoyage des données
│   ├── analyze_data.ipynb          # 📋 Analyse initiale
│   ├── Advanced_EDA_Morocco_Students.ipynb  # 📊 EDA avancée
│   ├── ML_student_performance_VF.ipynb      # 🤖 Modélisation ML
│   ├── evaluation.ipynb            # 📈 Évaluation des modèles
│   ├── best_model_student_prediction.pkl    # 💾 Modèle sauvegardé
│   └── model_features.pkl          # 📝 Liste des features
├── dataset/
│   └── Morocco_Student_Data_*.csv  # 📦 Données (10 000 étudiants)
├── requirements-web.txt            # 📋 Dépendances web
└── render.yaml                     # ☁️ Config déploiement Render
```

## 🚀 Installation & Lancement

### Prérequis

- Python 3.11+
- pip

### Installation

```bash
git clone https://github.com/youssefelalem/Pr-diction-de-la-Performance-des-tudiants.git
cd Pr-diction-de-la-Performance-des-tudiants
pip install -r requirements-web.txt
```

### Lancement

```bash
python api.py
```

Ouvrir [http://localhost:5000](http://localhost:5000) dans votre navigateur.

## 📊 Dataset

| Caractéristique | Valeur |
|---|---|
| **Source** | Morocco Student Data Pool |
| **Taille** | 10 000 étudiants |
| **Colonnes originales** | 286 |
| **Features retenues** | 35 (17 numériques + 18 catégorielles) |
| **Régions** | 12 régions du Maroc |
| **Target** | `moyenne_annuelle` (note /20) |

## 🤖 Modèles & Résultats

| Modèle | R² Test | RMSE | MAE |
|---|---|---|---|
| Régression Linéaire | 0.1769 | 2.0162 | 1.7147 |
| Ridge (L2) | 0.1777 | 2.0152 | 1.7137 |
| Lasso (L1) | 0.1430 | 2.0573 | 1.7408 |
| Random Forest | 0.1478 | 2.0515 | 1.7384 |
| **⭐ XGBoost (Tuned)** | **0.1827** | **Meilleur** | **Meilleur** |
| Deep Learning (MLP) | 0.1585 | 2.0386 | 1.7351 |

> 💡 Le **revenu familial** est la variable la plus corrélée avec la performance (r = +0.37).

## 🛠️ Technologies

| Technologie | Usage |
|---|---|
| **Python** | Langage principal |
| **Pandas / NumPy** | Manipulation de données |
| **scikit-learn** | Preprocessing & pipelines |
| **XGBoost** | Modèle de prédiction |
| **SHAP** | Interprétabilité |
| **Flask** | API web |
| **HTML/CSS/JS** | Interface utilisateur |

## 👥 Équipe

| Membre | Rôle Scrum | Responsabilités |
|---|---|---|
| **Maryem Boulaaqidate** | Product Owner | Vision produit, backlog, rapport |
| **Douae Moussaoui** | Scrum Master | Coordination, JIRA, Daily Meetings |
| **Youssef Elalem** | Équipe Dev | Data Engineering & Nettoyage |
| **Taha Kachmar** | Équipe Dev | Modélisation ML & Optimisation |
| **Mohammed Rakhila** | Équipe Dev | Évaluation & Code Review |

### Encadrants

- **Pr. Said Nouh** — Encadrant Académique
- **M. Taoufik Amzil** — Co-Encadrant

## ☁️ Déploiement

L'application est déployable sur [Render](https://render.com) :

```bash
# Build
pip install -r requirements-web.txt

# Start
gunicorn api:app --bind 0.0.0.0:$PORT
```

---

<p align="center">
  <strong>🎓 EduPredictors</strong> — Master Big Data & Data Science • 2025‑2026
</p>
