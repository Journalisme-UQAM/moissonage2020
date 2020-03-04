# -*- coding: utf-8 -*- 
import csv, json, encodings

dep = input("De quel député voulez-vous savoir le signe astrologique? ")
dep2 = dep.replace("\xa0", " ")
# print(dep)

fichier = "New.csv" ### À QUOI SERT CE FICHIER?

with open("signe-JHR.csv") as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        # nom = str(row["Nom"]).replace(u'\xa0',u ' ').encode('utf-8')
        # nom = nom.replace(u"\xc3\"", "é")
        
        if dep in str(row):
            print(row["Nom"] + " est " + row[" Signe"])
            # print(row)
            # print(nom)