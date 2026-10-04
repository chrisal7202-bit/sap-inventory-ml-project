import pandas as pd

#mostrare tutte le colonne senza tagliarle
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

df=pd.read_csv("zepto_preparato.csv")
print(f"Dimensione ORIGINALE del dataset:{df.shape[0]} righe.\n")

#consolidare le colonne quando si uniscono i prodotti con stesso nome
regole_consolidamento={'Category':'first','mrp':'mean','discountPercent':'mean','availableQuantity':'sum','discountedSellingPrice':'mean','weightInGms':'first','outOfStock':'first','quantity':'sum','Stock_Value':'sum','Discount_Value':'mean'}

#raggruppamento per 'name' e Data Consolidation
df_bonificato=df.groupby('name').agg(regole_consolidamento).reset_index()
print("--- BONIFICA COMPLETATA ---")
print(f"Dimensione del dataset bonificato: {df_bonificato.shape[0]} righe.")

#calcolo righe ridondanti accorpate
righe_eliminate=df.shape[0]-df_bonificato.shape[0]
print(f"Sono state accorpate {righe_eliminate} righe ridondanti.\n")

#verifica del capitale bloccato dopo la fusione
nuovo_capitale=df_bonificato['Stock_Value'].sum()
print(f"Nuovo valore economico totale bloccato: {nuovo_capitale:,} unità monetarie.")
print("(Deve essere identico a: 224,308,060)\n")

#nuova classifica top 5 prodotti per capitale bloccato
print("--- NUOVA TOP 5 PRODOTTI PER CAPITALE IMMOBILIZZATO ---")
top_5_nuova=df_bonificato[['name','Category','availableQuantity','Stock_Value']].sort_values(by='Stock_Value', ascending=False).head(5)
print(top_5_nuova)

df_bonificato.to_csv("zepto_bonificato.csv", index=False)
print("\nFile 'zepto_bonificato.csv' salvato con successo!")
