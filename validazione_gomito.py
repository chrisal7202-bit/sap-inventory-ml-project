import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df=pd.read_csv("zepto_bonificato.csv")
dati_input_ml=df[['Stock_Value','Discount_Value']]

#calcolo errore matematico (inerzia) per diversi numeri di cluster
inerzia=[]
for k in range(1,11):
    kmeans=KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(dati_input_ml)
    inerzia.append(kmeans.inertia_)

#rappresentazione grafico del "gomito"
plt.figure(figsize=(8,5))
plt.plot(range(1,11), inerzia, marker='o', linewidth=2, color='blue')
plt.title("Metodo del gomito - Validazione cluster")
plt.xlabel("Numero di cluster (k)")
plt.ylabel("Inerzia (somma dei quadrati delle distanze)")
plt.xticks(range(1,11))
plt.grid(True)

print("--- GRAFICO GENERATO ---")
print("Chiudi la finestra del grafico per terminare correttamente lo script.")

plt.show()
