import pandas as pd


# Ganti fungsi get_data_from_db() menjadi seperti ini:
def get_data_from_db():
    return pd.read_csv("data.csv")