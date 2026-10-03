import pandas as pd

#carica il dataset (deve essere nella stessa cartella di questo script)
df=pd.read_csv("zepto_v2.csv", encoding="latin1")

#verifica la dimensione del database
print("--- DIMENSIONE DEL DATASET ---")
print(f"Il dataset contiene {df.shape[0]} righe (prodotti) e {df.shape[1]} colonne.\n")

#controlla i tipi di dato di ogni colonna
print("--- STRUTTURA E TIPI DI DATO ---")
df.info()
print("\n")

#verifica se ci sono dati mancanti
print("--- VALORI MANCANTI PER COLONNA ---")
print(df.isnull().sum())
print("\n")

#guarda le statistiche principali delle quantità e dei prezzi
print("--- STATISTICHE PRINCIPALI ---")
colonne_numeriche=['mrp', 'discountPercent', 'availableQuantity', 'discountedSellingPrice']
print(df[colonne_numeriche].describe())
print("\n")

#scopri le categorie più frequenti
print("--- TOP 10 CATEGORIE NEL MAGAZZINO ---")
print(df['Category'].value_counts().head(10))
