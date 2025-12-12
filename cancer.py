# 1️⃣ Para manipular datos
import pandas as pd        # Leer CSV, manipular DataFrames
import numpy as np         # Operaciones numéricas y matrices

# 2️⃣ Para separar train/test y otras utilidades de ML
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error  # Métricas de evaluación

# 3️⃣ LightGBM
import lightgbm as lgb
import os
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
data = pd.read_excel("cancerdatos.xlsx")

# Información general
print(data.info())
# Estadísticas descriptivas
print(data.describe())      
print(data.head())

sum = data.duplicated().sum()
print(f"Número de filas duplicadas: {sum}")
xd = data.isnull().sum()
print(f"Número de valores nulos por columna:\n{xd}")