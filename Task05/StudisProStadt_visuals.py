#Marlene Albers, Benedict Herrnleben, Tom Eifflaender 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hier wird die CSV Datei eingelesen
df = pd.read_csv('/home/tom/Uni/dbs/Abfrageerg1.csv')

# Hier werden die Daten geprüft 
print(df.head())
print(df.info())

# Hier wird das Balkendiagramm erzeugt 
plt.figure(figsize=(50, 40))  # Angaben zur Höhe und Breite des Graphen 
sns.barplot(x='studisinort', y='ort', data=df, palette='viridis')

# Beschriftung des Graphen  
plt.xlabel('ort')
plt.ylabel('studisinort')
plt.title('Anzahl von Studierenden pro Ort')

plt.tight_layout()

# Speichern des Graphen 
plt.savefig('/home/tom/Uni/dbs/Studi_pro_Ort.png')

# Ausgeben des Graphen nach Erzeugung 
plt.show()