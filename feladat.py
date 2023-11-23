#modul importálása
import json

#adatbázis szimlácio
adatbazis = []

# fájlkezelése
with open("database.json", "r", encoding="utf8") as fájl:

     #feldolgozás
     adatbazis =json.load(fájl)

 #tesztel!
 print(adatbazis)    