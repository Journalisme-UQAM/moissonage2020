#coding utf-8
import requests, csv
from bs4 import BeautifulSoup
import tika ### MODULE POUR EXTRAIRE LE TEXTE DES PDF
from tika import parser

fichier = "procesverbaux-JHR.csv"

# Je désire recueillir tous les liens vers les documents PDF des procès verbaux de 2019
# disponibles sur le site de la municipalité de Saint-Léon-le-Grand.

### TRÈS INTÉRESSANT SUJET; DONT L'INTÉRÊT PUBLIC PARAÎT MANIFESTE

entetes = {
    "User-Agent":"David Masse, etudiant journalisme UQAM, ###/***-@@@@"
}

url = "https://municipalite.saint-leon-le-grand.qc.ca/documents/proces-verbaux.html"
url2 = "https://municipalite.saint-leon-le-grand.qc.ca/"
contenu = requests.get(url, headers = entetes)
page = BeautifulSoup(contenu.text, "html.parser")

liste = []
# Verifier si tout fonctionne avec un seul lien
# for pv in page.find("div", class_="contenu").find_next("p").find_all("a") : ### SUPER COMMANDE... QUI NE VA CHERCHER QUE LE PREMIER LIEN; IL FAUT JUSTE ENLEVER LE "FIND_NEXT("P")" POUR QUE ÇA FONCTIONNE.
for pv in page.find("div", class_="contenu").find_all("a") :
    # print(pv) ### TESTING 1-2-3

#     ### LE CONTENU DE TA BOUCLE ÉTAIT MAL INDENTÉ D'UN CRAN DE TROP VERS LA DROITE; J'AI TOUT TASSÉ D'UN CRAN VERS LA GAUCHE
    
    urlpv = pv.get("href") ### EXCELLENT
    # print(urlpv)
    urlpv = pv["href"] ### CETTE SYNTAXE FONCTIONNE ÉGALEMENT
    # print(urlpv)
    print("."*20)

    urltest = url2 + str(urlpv) ### INUTILE DE CONVERTIR DU TEXTE EN TEXTE :)
    urlpv = url2 + urlpv
    print(urlpv)
#     if "proces-verbaux" in url2: ### JE NE COMPRENDS PAS CETTE CONDITION...
#         PV = url2
#         PVfinal=PV.split(",")
#         liste.append(PVfinal)

    ### TANT QU'À Y ÊTRE, ON VA EXTRAIRE LE TEXTE DES PDF DES RÉSOLUTIONS!
    ### POUR CELA, ON VA SE SERVIR D'UN MODULE APPELÉ "TIKA"

    ### ON COMMENCE PAR ALLER CHERCHER CHACUN DES FICHIERS AVEC REQUESTS
    req = requests.get(urlpv, headers=entetes)

    ### LE CONTENU DE NOTRE REQUÊTE PEUT ÊTRE PLACÉ DANS UNE VARIABLE TEMPORAIRE
    pdfTemp = req.content

    ### IL FAUT ENSUITE ENREGISTRER LOCALEMENT LE FICHIER PDF
    ### ON UTILISE LE MODE "WB" (WRITE BINARY)
    with open("fichierPDF.pdf", "wb") as f1:
        f1.write(pdfTemp)

    ### ENSUITE, ON UTILISE L'OUTIL "PARSER" DE TIKA (IMPORTÉ AU DÉBUT DE NOTRE SCRIPT) POUR OUVRIR LE FICHIER PDF QUI SE TROUVE SUR NOTRE ORDI (ON L'OUVRE EN MODE "RB" (READ BINARY)) ET POUR PLACER LE TEXTE DU PDF DANS UNE VARIABLE
    textePDF = parser.from_file(open("fichierPDF.pdf", 'rb'))

    ### EN FAIT, TIKA CRÉE UN DICTIONNAIRE OÙ LE TEXTE DU PDF EST LA VALEUR DE LA CLÉ "content"
    # print(textePDF["content"])

    ### MAIS IL Y A D'AUTRES INFOS DISPONIBLES DANS LA CLÉ "metadata"

    procesVerbal = [urlpv,textePDF["metadata"]["pdf:charsPerPage"],textePDF["metadata"]["Author"],textePDF["content"]]

# # print(urltest)
# # oui :-D
# # je fais une boucle pour afficher tous générer tous mes liens 2019.
# # for urlpv1 in url2:
#     # print(url2+str(urlpv))

# night=open(fichier, "a") ### CETTE PARTIE DE CODE NE MARCHE PAS PARCE QU'ELLE N'EST PAS INDENTÉE DANS TA BOUCLE
# dark=csv.writer(night)
# dark.writerow(liste)

    knight=open(fichier, "a")
    dark=csv.writer(knight)
    dark.writerow(procesVerbal)

# # Pourtant, j'imprime tous les mêmes liens. Je n'arrive pas à faire changer la fin
# # de mon lien pour qu'il change. De plus, rien ne s'écrit dans mon fichier CSV. 