# Prédiction de la Performance des Étudiants

Projet de data science pour analyser les données d'étudiants et prédire leur performance académique avec des modèles de machine learning.

## Structure du projet

- `dataset/`
  - `Morocco_Student_Data_Pool.csv` : données brutes
  - `Morocco_Student_Data_Cleaned.csv` : données nettoyées
- `code/`
  - `clean_data.ipynb` : préparation/nettoyage
  - `analyze_data.ipynb` : EDA de base
  - `Advanced_EDA_Morocco_Students.ipynb` : EDA avancée
  - `ML_student_performance_VF.ipynb` : entraînement/sélection de modèles
  - `evaluation.ipynb` : évaluation finale
  - `best_model_student_prediction.pkl` : modèle sauvegardé
  - `model_features.pkl` : schéma des features du modèle
- `rapport_par_partie/`
  - `EDA_Report_Complete.pdf` : rapport EDA complet

## Convention recommandée

1. Mettre les notebooks de travail dans `code/`.
2. Mettre les jeux de données dans `dataset/`.
3. Mettre les rapports PDF dans `rapport_par_partie/`.
4. Garder la racine pour les fichiers de projet (`README.md`, `requirements.txt`, `.gitignore`).

## Prérequis

- Python 3.9+

Installation :

```bash
pip install -r requirements.txt
```

## Exécution recommandée

Ordre conseillé :

1. `code/clean_data.ipynb`
2. `code/analyze_data.ipynb` ou `code/Advanced_EDA_Morocco_Students.ipynb`
3. `code/ML_student_performance_VF.ipynb`
4. `code/evaluation.ipynb`

## Notes

- `.venv/` est ignoré par Git pour éviter les commits volumineux et inutiles.
