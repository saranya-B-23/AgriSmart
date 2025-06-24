#dataset/data_collection.py
import pandas as pd

def load_data(path='data/crop.csv'):
    df = pd.read_csv(path)
    return df

