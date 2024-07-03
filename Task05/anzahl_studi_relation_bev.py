#Marlene Albers, Benedict Herrnleben, Tom Eifflaender 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Hier wird die CSV-Datei einlesen
df = pd.read_csv('/home/tom/Uni/dbs/Abfrageerg2.csv')

# Hier werden eingelesenen Daten geprüft
print(df.head())
print(df.info())

# Hier wird das Balkendiagramm erstellen
plt.figure(figsize=(10, 6))  # Angaben zur höhe und breite des Graphen
sns.barplot(x='studirate', y='region', data=df, palette='viridis')

# Beschriftung des Graphen
plt.xlabel('Studirate')
plt.ylabel('Region')
plt.title('Anzahl Studierende pro Bundesland in Relation zur Bevölkerungsmenge')


plt.tight_layout()

# Speichern des Graphen als Bild
plt.savefig('/home/tom/Uni/dbs/Anzahl_Studi_Relation_Bevölk.png')

# Anzeigen des Grahen nachen Erzeugung
plt.show()