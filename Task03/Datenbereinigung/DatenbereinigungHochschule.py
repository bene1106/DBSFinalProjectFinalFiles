#   Datenbereinigung:

# rausnehmen:
# - Homepage (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreifen)
# - Hochschulkurzname (Wir haben den ganzen Hochschulnamen schon)
# - Hochschultyp (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreifen)
# - Gründungsjahr (Brauchen wir nicht für unsere Abfragen und auch nicht um auf den anderen Datensatz zuzugreifen)
# - Habilitationsrecht (Brauchen wir nicht für unsere Abfragen und auch nicht um auf den anderen Datensatz zuzugreifen)
# - Promotionsrecht (Brauchen wir nicht für unsere Abfragen und hilft uns nicht auf einen anderen Datensatz zuzugreife
# - Staße

# -> äöü werden ersetzt

import pandas as pa

# Datei laden
file_path = 'D:\\FU\\DBS\\FinalProject\\hochschulen.csv'
# Funktion zum Einlesen: pandas.read
hochsch = pa.read_csv(file_path, encoding='latin1', delimiter=';')

# Umlaute ersetzen:
replacements = {'Ã¤': 'ae', 'Ã¶': 'oe', 'Ã¼': 'ue', 'Ã„': 'Ae', 'Ã–': 'Oe', 'Ãœ': 'Ue', 'ÃŸ': 'ss'}
hochsch.replace(replacements, regex=True, inplace=True)

# Zu entfernende Spalten (als Liste für schnellen Zugriff)
columns_to_remove = [
    'Home Page', 
    'Hochschulkurzname', 
    'Hochschultyp', 
    'Gründungsjahr', 
    'Habilitationsrecht', 
    'Promotionsrecht', 
    'Straße',
    'Postleitzahl',
    'Bundesland',
    'GrÃ¼ndungsjahr',
    'ï»¿Hochschulkurzname',
    'StraÃe',
    'Postleitzahl (Hausanschrift)'
]


# Entfernen der Spalten, die tatsächlich im DataFrame vorhanden sind
existing_columns_to_remove = [col for col in columns_to_remove if col in hochsch.columns]
hochsch_cleaned = hochsch.drop(columns=existing_columns_to_remove)

# In neue CSV-Datei speichern
hochsch_cleaned.to_csv('D:\\FU\\DBS\\FinalProject\\cleaned_hochschulen.csv', sep=';', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_hochschulen.csv'.")

