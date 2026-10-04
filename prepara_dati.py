import pandas as pd

df=pd.read_csv("zepto_v2.csv", encoding="latin1")

#Feature Engineering: colonne per il machine learning
#capitale totale bloccato per ogni prodotto
df['Stock_Value']=df['availableQuantity']*df['discountedSellingPrice']

#sconto effettivo in valuta
df['Discount_Value']=df['mrp']-df['discountedSellingPrice']

#analisi del capitale immobilizzato
capitale_totale=df['Stock_Value'].sum()
print("--- ANALISI ECONOMICA DEL MAGAZZINO ---")
print(f"Il valore economico totale bloccato in magazzino è di: {capitale_totale:,} unità monetarie.\n")

#i primi 5 prodotti con più capitale bloccato
print("--- TOP 5 PRODOTTI PER CAPITALE IMMOBILIZZATO ---")
top_bloccati=df[['name','Category','availableQuantity','Stock_Value']].sort_values(by='Stock_Value', ascending=False).head(5)
print(top_bloccati)
print("\n")

df.to_csv("zepto_preparato.csv", index=False)
print("File 'zepto_preparato.csv' salvato con successo!")
