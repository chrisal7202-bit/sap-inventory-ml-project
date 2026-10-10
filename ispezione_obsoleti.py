import pandas as pd

pd.set_option('display.max_columns',None)
pd.set_option('display.width',1000)
df=pd.read_csv("zepto_con_cluster.csv")

#isolamento prodotti appartenenti al cluster 2 (codici da eliminare)
df_obsoleti=df[df['Cluster']==2]

print("--- ESTRATTO LISTA PRODOTTI OBSOLETI (CLUSTER 2) ---")
print(f"Totale prodotti critici isolati dall'IA: {df_obsoleti.shape[0]} prodotti.\n")

#ordinamento della lista per valore bloccato decrescente
colonne_report=['name','Category','availableQuantity','discountedSellingPrice','Stock_Value','Discount_Value']
report_obsoleti=df_obsoleti[colonne_report].sort_values(by='Stock_Value',ascending=False)

#primi 15 prodotti più critici
print("--- TOP 15 CODICI CRITICI DA MANDARE IN OBSOLESCENZA ---")
print(report_obsoleti.head(15))
print("\n")

#calcolo impatto economico cluster 2
capitale_lista_obsoleti=df_obsoleti['Stock_Value'].sum()
capitale_totale=df['Stock_Value'].sum()
impatto_percentuale=(capitale_lista_obsoleti/capitale_totale)*100

print("--- RIEPILOGO FINANZIARIO ---")
print(f"Capitale totale immobilizzato nei 34 prodotti obsoleti:{capitale_lista_obsoleti:,} unità monetarie.")
print(f"Questo ristretto gruppo rappresenta il {impatto_percentuale:.2f}% dell'intero valore del magazzino.\n")

report_obsoleti.to_csv("lista_nera_obsoleti.csv", index=False)
print("File 'lista_nera_obsoleti.csv' esportato con successo per il report!")

