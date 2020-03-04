# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

fichier = "vege-JHR.csv"

entetes = {
    "User-Agent":"Maude Faucher, étudiante en journalisme à l'UQAM"
}
# Je vais essayer de moissoner, dans les pages de recettes de plats végétariens de la page de Ricardo, les plats qui contiennent le mot "tofu" dans le titre. 

urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
# Mon url est celui de la page 1 parce que je vais devoir moissoner les données sur 11 pages. Il va donc falloir que je travaille avec un url différent à chaque fois. Je commence donc par la page 1.

### C'EST UN CAS TYPIQUE D'UTILISATION D'UNE BOUCLE.
### TOUT L'URL RESTE IDENTIQUE, SAUF LE NUMÉRO DE PAGE.
### ON PEUT DONC CRÉER, AU LIEU DE RÉPÉTER 11 FOIS LE MÊME CODE, UNE BOUCLE ALLANT DE 1 À 11.

numsDePage = list(range(1,12))

n = 0 ### TRÈS BONNE IDÉE QUE D'UTILISER UN COMPTEUR

for num in numsDePage:
    url = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/{}".format(str(num))

    print(url)

    site = requests.get(urlp1, headers=entetes)
    page = BeautifulSoup(site.text,"html.parser")
    plats = page.find_all("h2", class_="title")

# n=0
# liste = []
    for plat in plats:
        # print(plat.find("a")["href"])
        urlplat = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
        # liste.append(urlplat1)
        n+=1
        print(n, urlplat)
        # Je ne me souvenais plus comment simplement ajouter des éléments, alors j'ai triché un peu avec .replace mais ça fonctionne !
        # Pour chacune de mes pages (il y en a 11), je vais sortir le titre des 20 recettes affichées sur la page. 
        # Il y a certainement une manière plus efficace de faire, mais je ne la connais pas ou bien je n'arrive pas à l'imaginer !
        # Désolée pour ce script éternellement long ! 
        ### VOIR COMMENTAIRES PLUS HAUT

        ### MAINTENANT QUE TU AS PLUS DE 200 RECETTES, POURQUOI S'ARRÊTER À L'URL ET NE PAS ALLER RAMASSER D'AUTRES INFOS?

        sitePlat = requests.get(urlplat, headers=entetes)
        pagePlat = BeautifulSoup(sitePlat.text,"html.parser")

        ### SON NOM
        nom = pagePlat.find("meta", attrs={"property":"og:title"})["content"]
        nom = nom.split("|")[0].strip()

        ### SA DESCRIPTION
        desc = pagePlat.find("meta", attrs={"name":"description"})["content"]

        ### SON TEMPS DE PRÉPARATION
        tousDT = pagePlat.find_all("dt")

        tempsPrep = "Inconnu"
        
        for dt in tousDT:
            if dt.text.strip() == "Préparation":
                tempsPrep = dt.find_next("dd").text.strip()

        ### SON TEMPS DE CUISSON
        tempsCuisson = "Ne s'applique pas"
        for dt in tousDT:
            if dt.text.strip() == "Cuisson":
                tempsCuisson = dt.find_next("dd").text.strip()
        
        ### SON TEMPS DE MACÉRATION
        tempsMaceration = "Ne s'applique pas"
        for dt in tousDT:
            if dt.text.strip() == "Macération":
                tempsMaceration = dt.find_next("dd").text.strip()        

        ### SON NOMBRE D'INGRÉDIENTS
        ingredients = pagePlat.find("section", id="ingredients").find_all("li")
        nbIngr = len(ingredients)

        ### LE NOMBRE DES ÉTAPES REQUISES DANS SA PRÉPARATION
        etapes = pagePlat.find("section", id="preparation").find_all("li")
        nbEtapes = len(etapes)

        ### UNE FOIS QU'ON A TOUTES CES INFOS, ON PEUT LES RANGER DANS UNE LISTE

        infosRecette = [n,urlplat,nom,desc,tempsPrep,tempsCuisson,tempsMaceration,nbIngr,nbEtapes]

        ### ET C'EST CELA QU'ON INSCRIT DANS NOTRE FICHIER CSV
        ### LES INFOS DE CHAQUE RECETTE EST UNE LIGNE

        print(infosRecette) ### POUR VÉRIFIER

        platsveges = open(fichier, "a")
        tofu = csv.writer(platsveges)
        tofu.writerow(infosRecette)

# # numeros = list(range (1, 12))
# # for numero in numeros:
#     # urlpages = url + str(numero)
#     # print("."*10)
#     # print(urlpages)
#     # print("."*10)
#     # J'ai réussi à générer 11 url fonctionnels qui amènent aux pages de plats végés de la page de Ricardo !
#     # Ce qui m'a amené à changer mon url de base ! 

# # urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
# # urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# # urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
# # urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
# # urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
# # urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
# # urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
# # urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/8"
# # urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/9"
# # urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/10"
# # urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/11"

# urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp2, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")
# # Pour chaque page, je change le chiffre de la fin de l'url (qui mène à la bonne page sur le site), l'url de requests.get, l'urlplatX et le print. 

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat2 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat2)
#     n+=1
#     # print(n, urlplat2)

# urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
# site = requests.get(urlp3, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat3 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat3)
#     n+=1
#     # print(n, urlplat3)

# urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
# site = requests.get(urlp4, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat4 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat4)
#     n+=1
#     # print(n, urlplat4)

# urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
# site = requests.get(urlp5, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat5 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat5)
#     n+=1
#     # print(n, urlplat5)

# urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
# site = requests.get(urlp6, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat6 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat6)
#     n+=1
#     # print(n, urlplat6)

# urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
# site = requests.get(urlp7, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat7 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat7)
#     n+=1
#     # print(n, urlplat7)

# urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/8"
# site = requests.get(urlp8, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat8 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat8)
#     n+=1
#     # print(n, urlplat8)

# urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/9"
# site = requests.get(urlp9, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat9 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat9)
#     n+=1
#     # print(n, urlplat9)

# urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/10"
# site = requests.get(urlp10, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat10 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat10)
#     n+=1
#     # print(n, urlplat10)

# urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/11"
# site = requests.get(urlp11, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat11 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     liste.append(urlplat11)
#     n+=1
#     # print(n, urlplat11)

# liste.append("")
# liste.append("TOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFUTOFU")
# liste.append("")

# # Maintenant que j'ai toutes les recettes classées dans "Plats végétariens" du site de Ricardo, je vais moissoner tout ceux qui contiennent le mot "tofu" (avec un t majuscule ou minuscule) dans le titre.

# urlp1 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/1"
# site = requests.get(urlp1, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# # Ici, j'ai répété ce que je faisais dans la première moitié pour moissoner les urls des recettes végés, mais en ajoutant la condition if pour les mots contenant "ofu".

# n=0
# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat1 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat1:
#         liste.append(urlplat1)
#         n+=1
#         # print(n, urlplat1)

# urlp2 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp2, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat2 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat2:
#         liste.append(urlplat2)
#         n+=1
#         # print(n, urlplat2)

# urlp3 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/3"
# site = requests.get(urlp3, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat3 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat3:
#         liste.append(urlplat3)
#         n+=1
#         # print(n, urlplat3)

# urlp4 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/4"
# site = requests.get(urlp4, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat4 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat4:
#         liste.append(urlplat4)
#         n+=1
#         # print(n, urlplat4)

# urlp5 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/5"
# site = requests.get(urlp5, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat5 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat5:
#         liste.append(urlplat5)
#         n+=1
#         # print(n, urlplat5)

# urlp6 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/6"
# site = requests.get(urlp6, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat6 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat6:
#         liste.append(urlplat6)
#         n+=1
#         # print(n, urlplat6)

# urlp7 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/7"
# site = requests.get(urlp7, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat7 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat7:
#         liste.append(urlplat7)
#         n+=1
#         # print(n, urlplat7)

# urlp8 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp8, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat8 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat8:
#         liste.append(urlplat8)
#         n+=1
#         # print(n, urlplat8)

# urlp9 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp9, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat9 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat9:
#         liste.append(urlplat9)
#         n+=1
#         # print(n, urlplat9)

# urlp10 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp10, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat10 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat10:
#         liste.append(urlplat10)
#         n+=1
#         # print(n, urlplat10)

# urlp11 = "https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien/page/2"
# site = requests.get(urlp11, headers=entetes)
# page = BeautifulSoup(site.text,"html.parser")
# plats = page.find_all("h2", class_="title")

# for plat in plats:
#     # print(plat.find("a")["href"])
#     urlplat11 = plat.find("a")["href"].replace("/recettes/", "https://www.ricardocuisine.com/recettes/")
#     if "ofu" in urlplat11:
#         liste.append(urlplat11)
#         n+=1
#         # print(n, urlplat11)

# # Il est maintenant temps de créer mon fichier csv. 

# print(liste)

# platsveges = open(fichier, "a")
# tofu = csv.writer(platsveges)
# tofu.writerows(liste)
# # Mon fichier csv met une virgule entre chaque caractère, même s'ils sont dans des listes. J'ai cherché sur internet comment les enlever mais je n'ai pas réussi. Ce n'est pas optimal mais j'ai décidé de l'envoyer quand même. Au moins j'ai réussi à générer un fichier csv. Je progresse de travail en travail ! 
# # Bref, devoir réussi, malgré un fichier csv étrange et un très très long script ! Encore une fois, ce devoir était très dur, j'ai rushé pas mal !

### À LA FIN, SI TON FICHIER N'INSCRIT QU'UNE LETTRE À LA FOIS, C'EST QUE LA FONCTION "WRITEROW" S'ATTEND À AVOIR UNE LISTE
### ELLE INSCRIT CHAQUE ÉLÉMENT DE LA LISTE DANS UNE DES COLONNES DU FICHIER CSV QUE TU CRÉES
### SI TU NE LUI DONNES QU'UN "STRING" (UNE VARIABLE TEXTE), ELLE VA DÉCORTIQUER CE TEXTE ET INSCRIRE L'ÉLÉMENT 0 DE CE TEXTE (LA PREMIÈRE LETTRE), DANS LA PREMIÈRE COLONNE, L'ÉLÉMENT 1 DANS LA DEUXIÈME, ET AINSI DE SUITE... :)