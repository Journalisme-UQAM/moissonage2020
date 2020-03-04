# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

fichier = "devoir3-JHR.csv"

### TON SCRIPT FONCTIONNE BIEN
### IL AURAIT PU ALLER CHERCHER PLUS D'INFORMATION

# Mon but est de voir les villes d'origine et les destinations des vols que la compagnie Air Transat considère comme étant "pas chers". 
url = "https://www.airtransat.com/fr-CA/vols-pas-chers-du-canada?ici=footerlink&icn=cheap-flights_french"

entetes = {
    "User-Agent":"Éloi Fournier, étudiant en journalisme à l'UQAM"
}

site = requests.get(url, headers=entetes)
page = BeautifulSoup(site.text, "html.parser")
# print(page)

n = 0

# Cette fonction me permet d'obtenir tous les vols pas chers d'Air Transat par pays de destination. 
vols = page.find_all("li", class_="CMSSiteMapListItem")
# vols = page.find_all("ul", class_="CMSSiteMapList")
print(site.status_code)
# print(vols)

# Ma boucle, qui me permettra d'extraire les données que je recherche pour le csv.
for vol in vols: 
    infos=[]
    n += 1
    urlVol = "https://www.airtransat.com" + vol.find("a")["href"]
    nomVol = vol.find("a").text.strip()

    if "Vol" in nomVol: ### CONDITION POUR NE PRENDRE QUE LES PAGES QUI DÉCRIVENT DES VOLS ENTRE DEUX VILLES
        print(n, urlVol, nomVol)
        # if "https" in urlVol: 
        #     print(n, urlVol)
        # else: 
        #     urlVol2 = " https://www.airtransat.com" + str(urlVol)
        #     print(n, urlVol2)
        # print(nomVol)
        infos.append(n)
        # infos.append(urlVol2)
        infos.append(urlVol)
        # infos.append(nomVol)

        villes = nomVol.split("vers")
        depart = villes[0].replace("Vol de", "").replace("Vol d'", "").strip()
        destination = villes[1].strip()
        infos.append(depart)
        infos.append(destination)

        ### C'EST ICI QUE TU AURAIS PU OUVRIR CHACUNE DES PAGES ET TROUVER LES PRIX DE CES VOLS. VOICI UNE SUGGESTION:

        siteVols = requests.get(urlVol, headers=entetes)
        pageVols = BeautifulSoup(siteVols.text, "html.parser")

        tousPrix = pageVols.find_all("span", class_ = "price")

        listePrix = []
        prixMax = 0
        prixMin = 0

        for prix in tousPrix:
            print(prix.text)
            if prix.text != "0":
                listePrix.append(int(prix.text.replace("$","")))
        print(listePrix)
        
        if len(listePrix) > 0:
            prixMax = max(listePrix)
            prixMin = min(listePrix)

        infos.append(prixMax)
        infos.append(prixMin)

        print(infos)
        print("X"*20)

        # Code menant à la création de mon csv.
        air = open(fichier,"a")
        transat = csv.writer(air)
        transat.writerow(infos)