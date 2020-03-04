# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

#Après avoir importé request, csv et BeautifulSoup, j'insère mon URL, soit le site internet de Ricardo.
# Important de le mettre entre guillemets, sinon ça ne fonctionne pas. 

url = "https://www.ricardocuisine.com/recettes/"

# J'insère ensuite mon entête pour me présenter. 

entetes = {
    "User-Agent": "Alexandra Lauzon, étudiante journalisme UQAM"
}

# site = requests.get(url, headers=entetes)

# print(site.status_code) #Je vérifie ainsi si tout fonctionne bien. J'ai mon 200, je continue.

# page = BeautifulSoup(site.text, "html.parser")

# print(page) #On voit bien ici l'accueil du site de Ricardo. Tout fonctionne. 

sections = ["plats-principaux","entrees","desserts"]

n=0

for recettes in sections:
    # print(recettes)
    niveau1 = recettes
    urlsection = url + recettes #Il s'agit de mes urls de bases pour mes trois grandes sections.
    # print(urlsection)

    site = requests.get(urlsection, headers=entetes)
#     # print(site.status_code) #Je vérifie ainsi si tout fonctionne bien. J'ai mon 200, je continue.
    page = BeautifulSoup(site.text, "html.parser")

#     # print(page)

    # section2 = page.find_all("div", class_="desc") ### EN FAIT, POUR MIEUX S'Y RETROUVER, JE VAIS RENOMMER CETTE VARIABLE "SOUS-SECTIONS"
    sousSections = page.find_all("div", class_="desc")

    numero = list(range(1,20)) ### J'AI CHANGÉ TON INTERVALLE POUR LE FAIRE DÉBUTER À 1, CAR LES "PAGE/1" FONCTIONNENT SUR LE SITE DE RICARDO

    ### TU N'ÉTAIS VRAIMENT PAS LOIN! :)
    ### ICI, TOUT CE QU'IL S'AGISSAIT DE FAIRE UNE BOUCLE DANS TA LISTE "SOUS-SECTIONS":

    for sousSection in sousSections:
        urlSousSection = sousSection.find("a")["href"]
        urlSousSection = "https://www.ricardocuisine.com" + urlSousSection
        print(urlSousSection)
        niveau2 = urlSousSection[urlSousSection.rfind("/")+1:]

        ### C'EST DANS CHACUNE DE CES SOUS-SECTIONS QUE LES PAGES SONT UTILES
        ### C'EST DONC ICI QU'ON PEUT FAIRE CETTE BOUCLE:
    
        for nombre in numero:
            # print(nombre)
            urlSousSectionPaginee = urlSousSection + "/page/" + str(nombre)

            ### TU PEUX TE CONNECTER À CHACUNE DES "urlSousSectionPaginee" POUR ALLER CHERCHER TOUS LES LIENS QU'ELLE CONTIENT (CHAQUE LIEN EST UNE RECETTE)

            siteA = requests.get(urlSousSectionPaginee, headers=entetes)
            print(urlSousSectionPaginee)
            pageA = BeautifulSoup(siteA.text, "html.parser")

            ### DANS CHACUNE DE CES "PAGEA", IL Y A 20 RECETTES
            # recettes = pageA.find_all("h2", class_="title") ### TU AVAIS BIEN IDENTIFIÉ QUEL ÉLÉMENT DE QUELLE CLASSE QU'IL TE FALLAIT, MAIS JE VAIS LA CHANGER LÉGÈREMENT POUR ALLER CHERCHER PLUS D'INFOS
            recettes = pageA.find_all("div", class_="desc")
            for recette in recettes:
                n += 1
                urlRecette = recette.find("a")["href"]
                urlRecette = "https://www.ricardocuisine.com" + urlRecette
                print(urlRecette)

                nomRecette = recette.find("a").text.strip()
                temps = recette.find_all("li")
                # print(temps)
                try:
                    tempsPrep = temps[0].text.split(":")[-1].replace("min","").strip()
                    if "h" in tempsPrep:
                        heures = tempsPrep.split("h")
                        if heures[1] == "":
                            tempsPrep = int(heures[0].strip()) * 60
                        else:
                            tempsPrep = int(heures[0].strip()) * 60 + int(heures[1])
                except:
                    tempsPrep = 0
                try:
                    if "-" in tempsPrep:
                        tempsPrep = 0
                except:
                    tempsPrep = tempsPrep

                try:
                    tempsTotal = temps[1].text.split(":")[-1].replace("min","").strip()
                    # tempsTotal = temps[1].text.split(":")
                    # print(tempsTotal)
                    if "h" in tempsTotal:
                        heures2 = tempsTotal.split("h")
                        # print(heures2)
                        if heures2[1] == "":
                            tempsTotal = int(heures2[0].strip()) * 60
                        else:
                            tempsTotal = int(heures2[0].strip()) * 60 + int(heures2[1])
                     # print(tempsTotal)
                except:
                    tempsTotal = 0
                try:
                    if "-" in tempsTotal:
                        tempsTotal = 0
                except:
                    tempsTotal = tempsTotal

# #Ma section2 constitue les trois grandes classes ""
#     for section3 in section2:
#         n += 1
#         # print(section3)
#         urlRecettes = "https://www.ricardocuisine.com" + section3.find("a")["href"] #Il s'agit de mes urls pour chaque sous-sections de mes grandes sections (ex: Plats principaux>Canard)
#         urlRecettes2 = "https://www.ricardocuisine.com" + section3.find("a")["href"] + "/page/" + str(nombre) #Url pour les recettes des autres pages
#         # print(n, urlRecettes)
#         # print("."*10)

#         siteA = requests.get(urlRecettes, headers=entetes)
#         pageA = BeautifulSoup(siteA.text, "html.parser")

#         siteB = requests.get(urlRecettes2, headers=entetes)
#         pageB = BeautifulSoup(siteB.text, "html.parser")

#         section4 = pageA.find_all("h2", class_="title")
#         section4 = pageB.find_all("h2", class_="title")

#         for section5 in section4:
#             n += 1
#             # print(section5)
#             urlRecettes2 = "https://www.ricardocuisine.com" + section5.find("a")["href"] #Je me suis rendue compte que les liens qui menaient directement aux recettes ne contenaient pas "plats-principaux" (par exemple). Ça me menait directement à la page "Canard" (par exemple). Donc je n'ai pas besoin de le rajouter à l'url. 
#             print(n,urlRecettes2) 
#             print("."*10)

### IL NE TE MANQUAIT QUE D'ÉCRIRE LE TOUT DANS UN CSV

                fichier = "touteRicardo-JHR.csv"

                infos = [n,niveau1,niveau2,nomRecette,int(tempsPrep),int(tempsTotal),urlRecette]
                print(infos)

                josee = open(fichier,"a")
                distasio = csv.writer(josee)
                distasio.writerow(infos)

# #Pour une raison qui m'échappe, je n'ai que les résultats pour les desserts. Je croyais que c'était à cause de l'ajout des numéros de pages, mais même lorsque je le sépare en deux "recettes", ça ne fonctionne pas. 

### CE QUI NE FONCTIONNAIT PAS, DONC, C'EST SIMPLEMENT LE FAIT QUE TU NE FAISAIS PAS DE BOUCLES DANS DES BOUCLES
### TU AS UN PREMIER NIVEAU: TES TROIS GRANDES SECTIONS
### DANS CHACUNE, IL FALLAIT QUE TU FASSE UNE BOUCLE POUR ALLER CHERCHER TOUTES LES SOUS-SECTIONS
### PUIS DANS CHACUNE DE CES SOUS-SECTIONS, TU DEVAIS TESTER TOUTES LES PAGES POSSIBLES (AVEC UNE AUTRE BOUCLE -> NUMÉROS)