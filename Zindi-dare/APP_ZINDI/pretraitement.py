# 🎯 Data preprocessing
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import KNNImputer
from sklearn.compose import ColumnTransformer
import pandas as pd

def pretraitement(df):
    df.drop(["ID"], axis=1, inplace=True)

    numerical_features = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    categorical_features = df.select_dtypes(include=['object', 'category']).columns.tolist()

    num_features = numerical_features
    cat_features = categorical_features

    num_transformer = Pipeline([
        ("imputer", KNNImputer(n_neighbors = 5)),
        ("scaler", MinMaxScaler())
    ])

    # cat_transformer = Pipeline([
    #     ("encoder", OneHotEncoder(handle_unknown = "ignore"))
    # ])

    cat_transformer = Pipeline([
        ("encoder", OrdinalEncoder(handle_unknown = "use_encoded_value", unknown_value=-1))
    ])

    preprocessor = ColumnTransformer([
        ("num", num_transformer, num_features),
        ("cat", cat_transformer, cat_features)
    ])
    
    processed_data = preprocessor.fit_transform(df)
    new_columns = (num_features +
        list(preprocessor.named_transformers_['cat'].named_steps['encoder'].get_feature_names_out(cat_features))
    )

    # Convert in Pandas DataFrame
    processed_data = pd.DataFrame(processed_data, columns=new_columns)
    return processed_data