import pandas as pd

def extract():

    df = pd.read_csv('chamados.csv')

    return df.to_dict(orient='records')