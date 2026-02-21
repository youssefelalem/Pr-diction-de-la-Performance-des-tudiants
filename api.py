"""
🎓 EduPredictors — API Flask
Prédiction de la Performance des Étudiants Marocains
"""

from flask import Flask, jsonify, request, send_from_directory
import pandas as pd
import joblib
import os

app = Flask(__name__, static_folder='static')

# ---------------------------------------------------------------------------
# Chargement du modèle et des features au démarrage
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'code', 'best_model_student_prediction.pkl')
FEATURES_PATH = os.path.join(BASE_DIR, 'code', 'model_features.pkl')

pipeline = joblib.load(MODEL_PATH)
features_cols = joblib.load(FEATURES_PATH)

# Métadonnées des features (pour le formulaire)
NUM_FEATURES = [
    'heures_etude_jour', 'heures_etude_weekend', 'absences_totales',
    'age', 'distance_ecole_km', 'revenu_familial',
    'nombre_freres_soeurs', 'nombre_membres_famille',
    'heures_soutien_semaine', 'heures_sommeil_semaine',
    'activite_physique_heures_semaine', 'temps_ecran_heures_jour',
    'taux_assiduite', 'taux_ponctualite', 'taux_remise_devoirs',
    'annees_redoublement', 'retards',
]

CAT_FEATURES = [
    'sexe', 'zone', 'soutien_familial', 'niveau', 'filiere', 'region',
    'niveau_education_pere', 'niveau_education_mere', 'statut_parental',
    'cours_particuliers', 'niveau_motivation', 'participation_classe',
    'attention_cours', 'implication_parents', 'confiance_en_soi',
    'internet', 'chambre_personnelle', 'ordinateur_portable',
]

# Options des catégories
CAT_OPTIONS = {
    'sexe': ['F', 'M'],
    'zone': ['Rural', 'Semi-Urbain', 'Urbain'],
    'soutien_familial': ['Faible', 'Moyen', 'Eleve', 'Tres Eleve'],
    'niveau': ['Tronc Commun', '1Bac', '2Bac'],
    'filiere': [
        'Arts Appliques', 'Lettres Et Sciences Humaines', 'Sciences',
        'Sciences Economiques', 'Sciences Et Technologies',
        'Sciences Experimentales', 'Sciences Mathematiques',
    ],
    'region': [
        'Beni Mellal-Khenifra', 'Casablanca-Settat', 'Dakhla-Oued Ed-Dahab',
        'Draa-Tafilalet', 'Fes-Meknes', 'Guelmim-Oued Noun',
        'Laayoune-Sakia El Hamra', 'Marrakech-Safi', 'Oriental',
        'Rabat-Sale-Kenitra', 'Souss-Massa', 'Tanger-Tetouan-Al Hoceima',
    ],
    'niveau_education_pere': ['Aucun', 'Primaire', 'Secondaire', 'Universitaire', 'Master', 'Doctorat'],
    'niveau_education_mere': ['Aucun', 'Primaire', 'Secondaire', 'Universitaire', 'Master', 'Doctorat'],
    'statut_parental': ['Maries', 'Divorces', 'Veuf'],
    'cours_particuliers': ['Non', 'Oui'],
    'niveau_motivation': ['Faible', 'Moyen', 'Eleve', 'Tres Eleve'],
    'participation_classe': ['Faible', 'Moyen', 'Eleve', 'Tres Eleve'],
    'attention_cours': ['Faible', 'Moyen', 'Eleve'],
    'implication_parents': ['Faible', 'Moyen', 'Eleve', 'Tres Eleve'],
    'confiance_en_soi': ['Faible', 'Moyen', 'Eleve'],
    'internet': ['Non', 'Oui'],
    'chambre_personnelle': ['Non', 'Oui'],
    'ordinateur_portable': ['Non', 'Oui'],
}

# Plages numériques
NUM_RANGES = {
    'heures_etude_jour':               {'min': 0, 'max': 8,     'step': 0.5, 'default': 2},
    'heures_etude_weekend':            {'min': 0, 'max': 12,    'step': 0.5, 'default': 3},
    'absences_totales':                {'min': 0, 'max': 30,    'step': 1,   'default': 5},
    'age':                             {'min': 17,'max': 19,    'step': 1,   'default': 18},
    'distance_ecole_km':               {'min': 0, 'max': 50,    'step': 0.5, 'default': 5},
    'revenu_familial':                 {'min': 0, 'max': 70000, 'step': 500, 'default': 14000},
    'nombre_freres_soeurs':            {'min': 0, 'max': 6,     'step': 1,   'default': 2},
    'nombre_membres_famille':          {'min': 2, 'max': 12,    'step': 1,   'default': 5},
    'heures_soutien_semaine':          {'min': 0, 'max': 10,    'step': 0.5, 'default': 2},
    'heures_sommeil_semaine':          {'min': 4, 'max': 12,    'step': 0.5, 'default': 7},
    'activite_physique_heures_semaine':{'min': 0, 'max': 14,    'step': 0.5, 'default': 4},
    'temps_ecran_heures_jour':         {'min': 0, 'max': 10,    'step': 0.5, 'default': 3},
    'taux_assiduite':                  {'min': 78,'max': 100,   'step': 1,   'default': 89},
    'taux_ponctualite':                {'min': 82,'max': 100,   'step': 1,   'default': 91},
    'taux_remise_devoirs':             {'min': 65,'max': 100,   'step': 1,   'default': 83},
    'annees_redoublement':             {'min': 0, 'max': 1,     'step': 1,   'default': 0},
    'retards':                         {'min': 0, 'max': 12,    'step': 1,   'default': 5},
}


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Prédire la moyenne annuelle d'un étudiant."""
    try:
        data = request.get_json(force=True)

        # Construire un DataFrame avec exactement les features attendues
        row = {}
        for feat in features_cols:
            if feat in data:
                row[feat] = data[feat]
            else:
                # Valeur par défaut
                if feat in NUM_RANGES:
                    row[feat] = NUM_RANGES[feat]['default']
                elif feat in CAT_OPTIONS:
                    row[feat] = CAT_OPTIONS[feat][0]
                else:
                    row[feat] = 0

        df = pd.DataFrame([row])

        # Conversion des types
        for col in NUM_FEATURES:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

        prediction = pipeline.predict(df)[0]
        prediction = round(float(prediction), 2)

        # Clamp la prédiction entre 0 et 20
        prediction = max(0.0, min(20.0, prediction))

        return jsonify({
            'success': True,
            'prediction': prediction,
            'note_sur_20': prediction,
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


@app.route('/metadata', methods=['GET'])
def metadata():
    """Retourner les métadonnées des features pour le formulaire."""
    return jsonify({
        'num_features': NUM_FEATURES,
        'cat_features': CAT_FEATURES,
        'cat_options': CAT_OPTIONS,
        'num_ranges': NUM_RANGES,
    })


if __name__ == '__main__':
    print("🎓 EduPredictors — Serveur démarré sur http://localhost:5000")
    app.run(debug=True, port=5000)
