# Datenbereinugung:
# Bevölkerung reinigen
# -> Zeilen, die nicht vollständig mit Werten ausgefüllt sind werden entfenrt
# -> äöü werden ersetzt

# Pandas-Bib ermöglicht Datenmanipulation und -analyse:
import pandas as pa

# CSV-Datei laden:
file_path = 'D:\\FU\\DBS\\FinalProject\\bevoelkerung.csv'  # hier liedt die Datei
# Funktion zum Einlesen: pandas.read
bev = pa.read_csv(file_path, encoding='latin1', delimiter=';', skiprows=7)  #, error_bad_lines=False
# Parameter:
# encoding = 'latin1': Zeichen werden richtig dargestellt
# delimeter: Trennzeichen der CSV
# skiprows: erste 6 Zeilen überspringen (Tabelle geht da noch nicht los; Metadata)
# (error_bad_lines: nicht notwendig; überspringt Zeilen die nicht eingelesen werden können)


# Umlaute ersetzen:
replacements = {'Ã¤': 'ae', 'Ã¶': 'oe', 'Ã¼': 'ue', 'Ã„': 'Ae', 'Ã–': 'Oe', 'Ãœ': 'Ue', 'ÃŸ': 'ss'}
bev.replace(replacements, regex=True, inplace=True)

# Zeilen mit fehlenden Werten entfernen:
# dropna() entfernt Spalten, die mindestens einen fehlenden Wert enthalten
# (Standardparameter: how='any' -> min. 1 fehl. val
# axis=0 -> Zeilen)
cleaned_bev = bev.dropna()

# Entfernen von Zeilen mit '-' in irgendeiner Zelle
cleaned_bev = cleaned_bev[~cleaned_bev.isin(['-']).any(axis=1)]  
cleaned_bev = cleaned_bev[~cleaned_bev.isin(['.']).any(axis=1)]

# erste und dritte Spalte entfernen
cleaned_bev = cleaned_bev.drop(cleaned_bev.columns[0], axis=1)
cleaned_bev = cleaned_bev.drop(cleaned_bev.columns[1], axis=1)


# speichern der bereinigten Datei in neue CSV:
cleaned_bev.to_csv('D:\\FU\\DBS\\FinalProject\\cleaned_bevoelkerung.csv', sep=';', index=False)

print("Data cleaning complete. Cleaned data saved to 'cleaned_bevoelkerung.csv'.")