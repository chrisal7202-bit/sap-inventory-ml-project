import pandas as pd
from sklearn.cluster import KMeans

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df=pd.read_csv("zepto_bonificato.csv")
print(f"Dataset caricato: {df.shape[0]} prodotti unici.\n")

#selezione variabili economiche per il calcolo
variabili_ml=['Stock_Value','Discount_Value']
input_ml=df[variabili_ml]

#inizializzazione algoritmo K-Means per creare 3 cluster
kmeans=KMeans(n_clusters=3, random_state=42, n_init=10)

#addestramento algoritmo e assegnazione di un gruppo a ogni prodotto
df['Cluster']=kmeans.fit_predict(input_ml)
print("--- ADDESTRAMENTO COMPLETATO ---")
print("L'intelligenza artificiale ha classificato tutti i prodotti.\n")

#conteggio prodotti per cluster
print("--- DISTRIBUZIONE DEI PRODOTTI NEI CLUSTER ---")
print(df['Cluster'].value_counts())
print("\n")

#calcolo medie economiche
print("--- MEDIE ECONOMICHE DEI CLUSTER ---")
print(df.groupby('Cluster')[['Stock_Value','Discount_Value','availableQuantity']].mean())
print("\n")

df.to_csv("zepto_con_cluster.csv", index=False)
print("File finale 'zepto_con_cluster.csv' salvato con successo!")
