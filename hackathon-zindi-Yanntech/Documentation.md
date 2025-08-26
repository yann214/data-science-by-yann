## 📝 **Documentation Technique — Challenge Zindi: SheCures — AI for Diabetes Prediction**  
**Nom du participant :** Yanntech  
**Submission ID :** JQeK6V9K  
**Fichier de soumission :** `submission3.csv`

---

### 📌 1. Objectif du Projet

L'objectif de ce projet est de développer un modèle de classification multi-classes pour prédire le type ou le risque de diabète chez des patient·e·s en se basant sur des variables biomédicales, démographiques et comportementales.

Ce projet vise à prédire le **type de diabète** d’un patient parmi quatre classes :  
- Type 1 Diabetes  
- Type 2 Diabetes  
- Gestational Diabetes  
- Prediabetic


---

### 🧠 2. Approche et Méthodologie
- **Prétraitement :**  
  - Encodage des variables catégorielles (LabelEncoder et OneHotEncoder selon le modèle).
  - Normalisation des variables numériques comme le `BMI`, `Blood Glucose Levels`, `Waist Circumference`, etc.
  - Suppression ou traitement des valeurs manquantes si presente.

- **Modèle utilisé :**  
  Un modèle basé sur **XGBoostClassifier** a été retenu pour sa robustesse et sa capacité à gérer les variables mixtes.

- **Explicabilité (Explainability) :**  
  Utilisation de **SHAP** pour comprendre l’importance des variables.  
  Les plus influentes sont : `BMI`, `Blood Glucose Levels`, `Waist Circumference`, `Cholesterol Levels`.

---

### 🧪 3. Évaluation du modèle

- Méthodologie : **Validation croisée à 5 plis**
- Métriques : F1-score macro, accuracy, confusion matrix
- Résultats : le modèle a obtenu une **cross-validation élevée**, indiquant une bonne généralisation.

---

### 🔁 4. Reproduction des Résultats

1. Installer les dépendances :  
```bash
pip install -r requirements.txt
```

2. Lancer le fichier `notebookfinal.py` ou utiliser le `Notebook_final.ipynb`
3. Le script génère `submission3.csv`
4. Vérifier que le fichier est identique à celui soumis

---

### ⚙️ 5. Environnement
                
- Langage: Python 3.10+          
- IDE utilisé : Jupyter Notebook      
- Librairies clés pandas, numpy, xgboost, shap, sklearn 
- Matériel :CPU / GPU local       

---

### ✅ 6. Conclusion
Le modèle s’est montré performant, interprétable, et reproductible. Les variables les plus influentes médicalement sont cohérentes avec les connaissances scientifiques connues sur le diabète.

### ✅ 7. Bonus : Application Streamlit pour les Utilisateurs.



### 🎯 Objectif
Cette application web permet de **prédire le type de diabète** à partir d'un fichier de données (CSV ou Excel) en utilisant un modèle de machine learning pré-entraîné.

---

### 🚀 Fonctionnalités
- **Interface utilisateur simple avec Streamlit**
- **Chargement de fichiers CSV ou Excel**
- **Affichage des données chargées**
- **Prétraitement automatique** des données via une fonction externe
- **Prédiction du type de diabète**
- **Téléchargement des résultats** avec les prédictions intégrées

---
### Utilisation
```bash
pip install -r requirements.txt
```
```bash
streamlit run APP.py
```

### 📁 Structure du Code

#### 1. **Importation des bibliothèques**
- `streamlit` : pour l’interface utilisateur web
- `pandas` : pour la manipulation de données tabulaires
- `joblib` : pour charger le modèle entraîné
- `pretraitement` : module local contenant la fonction de nettoyage des données

#### 2. **Configuration de la page Streamlit**
- Titre personnalisé
- Mise en page large
- Icône médicale

#### 3. **Personnalisation CSS**
- Amélioration visuelle via balises `<style>`

#### 4. **Chargement du modèle de classification**
- Chargement d’un modèle ML `Classification_diabete.pkl` via `joblib.load`

#### 5. **Chargement et affichage des données**
- Le fichier utilisateur (CSV ou Excel) est chargé et affiché

#### 6. **Prétraitement des données**
- Appel à la fonction `pretraitement(df)` pour nettoyer et formater les données

#### 7. **Prédictions et téléchargement**
- Prédictions appliquées aux données nettoyées
- Résultats affichés + option de téléchargement au format `.xlsx` (en réalité export CSV mais renommé)

---


