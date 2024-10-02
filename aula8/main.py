import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ler arquirvo csv pelo pandas
def ler_csy (file_path):
    return pd.read_csv(file_path)

def treinar(df):
    x = df[['acidez','densidade','viscosidade','tonalidade']]
    y = df['tipos_de_vinho']