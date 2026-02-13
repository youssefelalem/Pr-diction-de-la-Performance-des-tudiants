# Prediction de la Performance des Etudiants

Ce projet analyse des donnees d'etudiants et construit des modeles de machine learning pour predire la performance academique.

## Contenu du projet

- `dataset/../dataset/Morocco_Student_Data_Pool.csv` : jeu de donnees brut.
- `dataset/../dataset/Morocco_Student_Data_Cleaned.csv` : jeu de donnees nettoye.
- `clean_data.ipynb` : nettoyage et preparation des donnees.
- `analyze_data.ipynb` : analyse exploratoire de base.
- `EDA_Advanced.ipynb` : analyse exploratoire avancee.
- `ML_student_performance_VF.ipynb` : entrainement et comparaison de modeles.
- `evaluation.ipynb` : evaluation des performances.
- `code/best_model_student_prediction.pkl` : meilleur modele sauvegarde.
- `code/model_features.pkl` : variables/features du modele.

## Prerequis

- Python 3.9+

Installer les dependances :

```bash
pip install -r requirements.txt
```

## Demarrage rapide

1. Ouvrir le dossier du projet.
2. Installer les dependances.
3. Lancer Jupyter Notebook :

```bash
jupyter notebook
```

4. Executer les notebooks dans cet ordre recommande :
   - `clean_data.ipynb`
   - `analyze_data.ipynb` ou `EDA_Advanced.ipynb`
   - `ML_student_performance_VF.ipynb`
   - `evaluation.ipynb`

## Resultat attendu

Le pipeline permet de :

- preparer les donnees et traiter les variables,
- entrainer plusieurs algorithmes de regression,
- comparer les metriques,
- sauvegarder le meilleur modele pour reutilisation.

## Notes

- Certains notebooks peuvent prendre du temps selon la machine.
- Le modele final est deja fourni via `code/best_model_student_prediction.pkl`.



