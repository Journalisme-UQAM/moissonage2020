# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

fichier = "devoir3-JHR.csv"

url = "https://www.rds.ca/1."

entetes = {
    "User-Agent":"Nicholas Pereira, étudiant à l'UQAM"
}

n = 0

# date = list(range(7240200,7249300))
date = list(range(7240000,7241000)) ### J'ESSAIE UN AUTRE INTERVALLE D'UN MILLIER
for code in date:
    infos = []
    try:
        urlDuJour = url + str(code)

        site = requests.get(urlDuJour,headers=entetes)
        #print(site.status_code)

        page = BeautifulSoup(site.text, "html.parser")
        #print(page)
        n += 1
        #print(article)
        
        titreArticle = page.find("h1", class_="section").text.strip()
        sectionArticle = page.find("meta", property="article:section")["content"]
        auteurArticle = page.find("div", class_="author").text.strip()
        dateArticle = page.find("div", class_="pubdate").text.strip()

        print(n)
        print(urlDuJour)
        print(titreArticle)
        print(sectionArticle)
        print(auteurArticle)
        print(dateArticle)
        print("."*10)

        infos.append(n)
        infos.append(urlDuJour)
        infos.append(titreArticle)
        infos.append(sectionArticle)
        infos.append(auteurArticle)
        infos.append(dateArticle)

        media = open(fichier, "a")
        rds = csv.writer(media)
        rds.writerow(infos)

    except:
        print("Il n'y a rien à cet URL")

#EXPLICATIONS :
#Ce script permet d'aller chercher toutes les informations relatives aux articles de la plateforme
#web de RDS. 

#Lors de ma recherche, j'ai réalisé que les articles étaient tous liés à un code numérique.
#Toutefois, ceux-ci ne suivent pas un ordre logique, ce qui rend la classification difficile. De nombreux
#liens ne donne pas de résultats, car ils n'existent pas ou ne représentent pas un article. Dans mon
#travail, j'ai sélectionné tous ceux classifiés entre 7249200 et 7249300. Parmi ces nombres, seulement trois
#permettent d'accéder à un lien existant. La plateforme de RDS est également plutôt lente, ce qui a 
#ralenti le processus. 

# Dans le fichier csv, il est possible de retrouver l'url, le titre, la catégorie (prise à partir 
# des métadonnées), l'auteur et la date de parution.