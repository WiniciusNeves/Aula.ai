# Importar as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('caminho_para_o_seu_dataset.csv')

print(df.head())

df_numeric = df.select_dtypes(include=[np.number])

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

range_n_clusters = list(range(1, 11))

inertia = []

for k in range_n_clusters:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)


plt.figure(figsize=(8, 6))
plt.plot(range_n_clusters, inertia, 'bo-', markersize=8)
plt.xlabel('Número de Clusters (K)')
plt.ylabel('Inertia')
plt.title('Método do Cotovelo para Identificar o Número Ideal de Clusters')
plt.grid(True)
plt.show()


n_clusters_ideal = 3

kmeans = KMeans(n_clusters=n_clusters_ideal, random_state=42)
df['Cluster'] = kmeans.fit_predict(df_scaled)


print(df.head())


df.to_csv('dataset_com_clusters.csv', index=False)

print("Novo dataset com clusters salvo como 'dataset_com_clusters.csv'")

