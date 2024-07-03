#Marlene Albers, Benedict Herrnleben, Tom Eifflaender 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hier wird die CSV Datei eingelesen 
df = pd.read_csv('/home/tom/Uni/dbs/Abfrageerg3.csv')

# Hier werden die Daten geprüfen
print(df.head())
print(df.info())

# Hier wird das Balkendiagramm erzeugt
plt.figure(figsize=(10, 6))  # Angaben zur Größe und Breite des Graphen
sns.barplot(x='count', y='region', data=df, palette='viridis')

# Beschriftung des Graphen
plt.xlabel('Count')
plt.ylabel('Region')
plt.title('Anzahl von öffentlich rechtlichen Hochschulen pro Ort')

plt.tight_layout()

# Speichern des Graphen
plt.savefig('/home/tom/Uni/dbs/öffentlich_rechtliche.png')

# Anzeigen des Graphen nach Ertsellung 
plt.show()