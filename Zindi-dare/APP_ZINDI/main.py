from pydantic import BaseModel, Field  # Utilisé pour la validation des données
import numpy as np
import pandas as pd  # Utilisé pour la manipulation de données
import joblib  # Utilisé pour charger le modèle sauvegardé
from flask import Flask, request, jsonify  # Flask est un micro-framework pour les applications web

# Charger le modèle de forêt aléatoire depuis le disque
modele = joblib.load(r"Classification_diabete.pkl")

# Définition du schéma des données d'entrée avec Pydantic
# Cela garantit que les données reçues correspondent aux attentes du modèle
from pydantic import BaseModel, Field

class DonneesEntree(BaseModel):
    genetic_markers: str = Field(..., alias="Genetic Markers")
    family_history: str = Field(..., alias="Family History")
    insulin_levels: float = Field(..., alias="Insulin Levels")
    blood_glucose_levels: float = Field(..., alias="Blood Glucose Levels")
    glucose_tolerance_test: str = Field(..., alias="Glucose Tolerance Test")
    bmi: float = Field(..., alias="BMI")
    waist_circumference: float = Field(..., alias="Waist Circumference")
    physical_activity: str = Field(..., alias="Physical Activity")
    dietary_habits: str = Field(..., alias="Dietary Habits")
    smoking_status: str = Field(..., alias="Smoking Status")
    alcohol_consumption: str = Field(..., alias="Alcohol Consumption")
    blood_pressure: float = Field(..., alias="Blood Pressure")
    cholesterol_levels: float = Field(..., alias="Cholesterol Levels")
    liver_function_tests: str = Field(..., alias="Liver Function Tests")
    previous_gestational_diabetes: str = Field(..., alias="Previous Gestational Diabetes")
    pregnancy_history: str = Field(..., alias="Pregnancy History")
    weight_gain_during_pregnancy: float = Field(..., alias="Weight Gain During Pregnancy")
    ethnicity: str = Field(..., alias="Ethnicity")
    socioeconomic_factors: float = Field(..., alias="Socioeconomic Factors")


    class Config:
        allow_population_by_field_name = True  # Permet d'accepter à la fois les alias et les noms internes

# Création de l'instance de l'application Flask
app = Flask(__name__)

# Définition de la route racine qui retourne un message de bienvenue
@app.route("/", methods=["GET"])
def accueil():
    """ Endpoint racine qui fournit un message de bienvenue. """
    return jsonify({"message": "Bienvenue sur l'API de prédiction pour le diagnostic du type de diabète"})

# Définition de la route pour les prédictions de diabète
@app.route("/predire", methods=["POST"])
def predire():
    """
    Endpoint pour les prédictions en utilisant le modèle chargé.
    Les données d'entrée sont validées et transformées en DataFrame pour le traitement par le modèle.
    """
    if not request.json:
        return jsonify({"erreur": "Aucun JSON fourni"}), 400
    
    
    try:
        # print(f"colo du mod {modele.feature_names_in_}")

        # Extraction et validation des données d'entrée en utilisant Pydantic
        donnees = DonneesEntree.parse_obj(request.json)
        donnees_df = pd.DataFrame([donnees.dict(by_alias=True)])  # important: garde les alias !

        # Utilisation du modèle pour prédire et obtenir les probabilités
        predictions = modele.predict(donnees_df)[0]
        # probas = modele.predict_proba(donnees_df)[0]  # Probabilité de la classe positive (diabète)
        classe = modele.classes_
       
        print(donnees_df.head(1))

        # Compilation des résultats dans un dictionnaire
        resultats = donnees.dict()
        resultats['prediction'] = predictions 
        resultats['probabilite_par_classe'] = probabilities

        # Renvoie les résultats sous forme de JSON 
        return jsonify({"resultats": resultats}) 
    except Exception as e:
        # Gestion des erreurs et renvoi d'une réponse d'erreur
        return jsonify({"erreur": str(e)}), 400

# Point d'entrée pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Lancement de l'application sur le port 8000 avec le mode debug activé
