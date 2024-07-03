#Marlene Albers, Benedict Herrnleben, Tom Eifflaender 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hier wird die CSV Datei eingelesen
df = pd.read_csv('/home/tom/Uni/dbs/Abfrageerg4.csv')

# 
print(df.head())
print(df.info())

# DataFrame umwandeln für Seaborn
df_melted = df.melt(id_vars='region', value_vars=['maennlich', 'weiblich'], var_name='Geschlecht', value_name='Anzahl')

# Hier wird das Balkendiagramm erstellen
plt.figure(figsize=(100, 50))  # Angaben zur Höhe und Breite des Graphen
sns.barplot(x='region', y='Anzahl', hue='Geschlecht', data=df_melted, palette='viridis')

# Hier wird der Graph beschriftet 
plt.xlabel('Region')
plt.ylabel('Anzahl')
plt.title('Anzahl der männlichen und weiblichen Bevölkerung pro Ort')

# Anpassung des Graphen
plt.xticks(rotation=45, ha='right')  #Drehen der x-Achsenbeschriftungen, damit diese nicht überlappen
plt.tight_layout()

# Speichern des Graphen
plt.savefig('/home/tom/Uni/dbs/Anzahl_Männlich_Weiblich_pro_Ort.png')

# Anzeigen des fertigen Graphen
plt.show()
