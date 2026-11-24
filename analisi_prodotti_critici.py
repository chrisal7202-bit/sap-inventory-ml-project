import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df = pd.read_csv("zepto_con_cluster.csv")

# Profilazione dei cluster
profilo_cluster = df.groupby('Cluster')[['Stock_Value', 'Discount_Rate', 'availableQuantity']].mean()

# Identificazione dinamica del cluster
# con il maggiore valore medio delle giacenze
cluster_prioritario = profilo_cluster['Stock_Value'].idxmax()

print(f"Cluster prioritario: {cluster_prioritario}")

df_critici = df[df['Cluster'] == cluster_prioritario].copy()

print(f"Prodotti nel cluster prioritario: {len(df_critici)}")

# Selezione dei 15 prodotti a maggiore valore
top_15 = df_critici.sort_values(by='Stock_Value',ascending=False).head(15)

print("--- WATCHLIST PRODOTTI PRIORITARI ---")

print(top_15[['name', 'Category', 'availableQuantity','Stock_Value', 'Discount_Rate']])

valore_totale = top_15['Stock_Value'].sum()

print(f"\nValore commerciale watchlist: {valore_totale:,.2f}")

incidenza = valore_totale / df['Stock_Value'].sum() * 100

print(f"Incidenza sul valore totale: {incidenza:.2f}%")

top_15.to_csv("top_15_prodotti_da_verificare.csv",index=False)
