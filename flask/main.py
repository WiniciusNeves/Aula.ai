
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


df = pd.read_csv("data.csv")
colunas_independentes = ["numero-de-alunos","temperatura-ambiende","N-Computadores","capacidade-de-sala","Horario-do-dia"]
colunas_dependentes = ["Temperadura"]


dados_x = df[colunas_independentes]
dados_y = df[colunas_dependentes]


modelo = LinearRegression().fit(dados_x, dados_y)

num_alunos = 21
temperatura = 27
N_computadores = 27
capacidade_de_sala = 30
Horario_do_dia = 20

valores = np.array([num_alunos,temperatura,N_computadores,capacidade_de_sala,Horario_do_dia])


print("A temperatura prevista   de:", modelo.predict([valores]))




