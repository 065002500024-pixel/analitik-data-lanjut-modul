import pandas as pd
import streamlit as st


# Ganti fungsi koneksi database dengan membaca file CSV
def get_data_from_db():
    return pd.read_csv("pddikti_example.csv")