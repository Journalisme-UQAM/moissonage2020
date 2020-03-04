# coding : utf-8

#ce code permet de creer un csv avec tous les urls des archives du site actualite.uqam

#commandes de bases pour le log-in et la creation du csv

import requests, csv
from bs4 import BeautifulSoup

#liste des urls des articles
contenu = list()

#creation d'une entête
entetes = {
    "User-Agent":"Francois-Alexis Favreau:Étudiant journalisme UQAM"
}

#boucle pour consulter toutes les pages d'archives (576 au moment de realiser ce travail)
for i in range(88, 576):

    #test pour definir l'url de la page suivante ### INTÉRASSANT, MAIS LA PAGE 0 FONCTIONNE AVEC CE SITE
    if i == 0:
        url = "https://www.actualites.uqam.ca/toutes-les-archives"
    elif i > 0:
        url = "https://www.actualites.uqam.ca/toutes-les-archives?page={}".format(i)

#vérification qua chaque page fonctionne
    print(url)

    page = requests.get(url, headers=entetes)
    print("Les articles de cette page se retrouvent dans la liste")
    soup = BeautifulSoup(page.text, 'html.parser')

    #vérification du statut, 200=ok
    #print(page.status_code)

    #view-content contient le corps de la page
    article = soup.find(class_="view-content")
    # print(article)
    #on va chercher les titres
    titres = article.find_all("h4")


    #pour chaque titre, aller chercher le href (url)
    for titre in titres:
        contenu = [] ### ON INITIALISE UNE LISTE DANS LAQUELLE ON VA METTRE TOUS LES ÉLÉMENTS RELATIFS AUX ARTICLES D'ACTUALITÉ UQAM
        elem = titre.find('a')
        # print(elem)
        lien = elem.get('href')
        # print(lien)
        contenu.append(lien) ### POURQUOI NE RAMASSER QUE LE LIEN, ALLONS CHERCHER D'AUTRES INFOS
        # print(contenu)

        titreArticle = titre.text.strip()
        contenu.append(titreArticle)

        resume = titre.find_next("p", class_="chapeau").text.strip()
        contenu.append(resume)

        date = titre.find_previous("p", class_="date").text.strip()
        contenu.append(date)

        print(contenu)

### CE CODE NE CRÉE UN CSV UNIQUEMENT APRÈS QUE TON SCRIPT AIT MOISSONNÉ TOUTES LES PAGES...
### SI TON SCRIPT PLANTE EN COURS DE ROUTE, IL FAUT TOUT RECOMMENCER...
### C'EST JUSTEMENT ARRIVÉ À QUELQUES REPRISES QUAND JE L'AI FAIT ROULER, D'OÙ L'INTÉRÊT D'ENREGISTRER LE MATÉRIEL AU FUR ET À MESURE 
#creation d'un csv qui contient chaque url
# with open('archives-JHR.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for occ in contenu:
#         writer.writerow([occ])

### ÉCRIS PLUTÔT TON CSV À L'INTÉRIEUR DE TA BOUCLE "FOR TITRE IN TITRES"
### ET ÉCRIS-LA EN MODE "A", ET NON EN MODE "W"
        romano = open("archivesUQAM-JHR.csv", "a")
        fafard = csv.writer(romano)
        fafard.writerow(contenu)

print("Les articles se retrouvent dans archives.csv")

### TON DEVOIR AURAIT DÛ ÊTRE ACCOMPAGNÉ D'UN FICHIER CSV.
