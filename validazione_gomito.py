import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Caricamento dataset
df = pd.read_csv("zepto_bonificato.csv")

# Esclusione dei prodotti senza giacenza
df = df[df['availableQuantity'] > 0].copy()

# Selezione delle variabili
variabili_ml = ['Stock_Value', 'Discount_Rate']

# Esclusione delle anomalie economiche
df = df.dropna(subset=variabili_ml).copy()

print(f"Prodotti analizzati: {len(df)}")

# Standardizzazione
input_ml = df[variabili_ml]

scaler = StandardScaler()
input_scaled = scaler.fit_transform(input_ml)

# Inizializzazione liste
inerzia = []
silhouette = []

# Intervallo dei cluster da testare
valori_k = range(1, 11)

for k in valori_k:

    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(input_scaled)

    inerzia.append(kmeans.inertia_)

    print(f"K={k} - Inerzia: {kmeans.inertia_:.2f}")

    if k >= 2:

        score = silhouette_score(input_scaled, labels)

        silhouette.append(score)

        print(f"Silhouette Score: {score:.4f}")

# Metodo del gomito
plt.figure(figsize=(9, 5))
plt.plot(valori_k, inerzia, marker='o')
plt.xlabel("Numero di cluster (K)")
plt.ylabel("Inerzia")
plt.title("Elbow Method - Dati standardizzati")
plt.xticks(list(valori_k))
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_metodo_gomito.png", dpi=300)
plt.show()

# Silhouette Score
plt.figure(figsize=(9, 5))
plt.plot(range(2, 11), silhouette, marker='o')
plt.xlabel("Numero di cluster (K)")
plt.ylabel("Silhouette Score")
plt.title("Validazione del clustering")
plt.xticks(list(range(2, 11)))
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico_silhouette.png", dpi=300)
plt.show()

# Migliore K secondo Silhouette
migliore_k = silhouette.index(max(silhouette)) + 2

print(f"\nMigliore K secondo Silhouette: {migliore_k}")
print(f"Silhouette massima: {max(silhouette):.4f}")
