import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df=pd.read_csv("zepto_bonificato.csv")
print(f"Dataset caricato: {df.shape[0]} prodotti unici.\n")

#Identificazione dei prodotti senza giacenza
df_senza_giacenza = df[df['availableQuantity'] == 0].copy()

print(f"Prodotti senza giacenza: {len(df_senza_giacenza)}")

# Esclusione dei prodotti senza giacenza
df = df[df['availableQuantity'] > 0].copy()

print(f"Prodotti con giacenza positiva: {len(df)}")

# Controllo dei valori mancanti
variabili_ml = ['Stock_Value', 'Discount_Rate']

print("--- VALORI MANCANTI RESIDUI ---")
print(df[variabili_ml].isna().sum())

# Ispezione dei record problematici
print("--- RECORD ANOMALI ---")

print(df.loc[df[variabili_ml].isna().any(axis=1),['name', 'mrp', 'availableQuantity','Stock_Value','Total_Stock_Discount','Discount_Rate']])

# Identificazione delle anomalie economiche
maschera_anomalie = df[variabili_ml].isna().any(axis=1)
df_anomalie = df[maschera_anomalie].copy()

print(f"Prodotti con anomalie economiche: {len(df_anomalie)}")

# Esportazione delle anomalie
df_anomalie.to_csv("anomalie_clustering.csv", index=False)

# Esclusione delle anomalie dal clustering
df = df[~maschera_anomalie].copy()
print(f"Prodotti ammessi al clustering: {len(df)}")

#selezione variabili economiche per il calcolo
variabili_ml=['Stock_Value','Discount_Rate']
input_ml=df[variabili_ml]
scaler=StandardScaler()
input_scaled=scaler.fit_transform(input_ml)

#inizializzazione algoritmo K-Means per creare 3 cluster
kmeans=KMeans(n_clusters=3, random_state=42, n_init=10)

#addestramento algoritmo e assegnazione di un gruppo a ogni prodotto
df['Cluster']=kmeans.fit_predict(input_scaled)
print("--- ADDESTRAMENTO COMPLETATO ---")
print("L'intelligenza artificiale ha classificato tutti i prodotti.\n")

#conteggio prodotti per cluster
print("--- DISTRIBUZIONE DEI PRODOTTI NEI CLUSTER ---")
print(df['Cluster'].value_counts())
print("\n")

#calcolo medie economiche
print("--- MEDIE ECONOMICHE DEI CLUSTER ---")
print(df.groupby('Cluster')[['Stock_Value','Discount_Rate','availableQuantity']].mean())
print("\n")

df.to_csv("zepto_con_cluster.csv", index=False)
print("File finale 'zepto_con_cluster.csv' salvato con successo!")

print("--- VALORI MANCANTI ---")
print(df[['Stock_Value', 'Discount_Rate']].isna().sum())

print("--- PRODOTTI CON DISCOUNT RATE NON DEFINITO ---")
print(df.loc[df['Discount_Rate'].isna(),['name', 'availableQuantity', 'Stock_Value','Total_Stock_Discount']])
