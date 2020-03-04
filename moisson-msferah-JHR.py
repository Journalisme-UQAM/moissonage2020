# coding: utf-8
# importer les modules dont j'ai besoin
import csv
import requests
from bs4 import BeautifulSoup

fichier = "goodfood-JHR.csv"

# je m'intéresse au site web de la compagnie Goodfood, je veux afficher toutes les recettes/ingrédients disponibles

url = "https://www.makegoodfood.ca/fr/recipes/"

# annoncer ma présence sur le serveur

entetes = {
    "User-Agent": "Mayssa Ferah, journalism student UQAM",
    "from":"m**.f**@**.**"
}

# placer le contenu de ma page web dans une variable + analyse (parse) 

pages = list(range(1,200)) ### POURQUOI SE LIMITER À 199? :)

for url1 in pages:
    # url1= url + str(pages) ### ERREUR: ICI, TU AJOUTES UNE LISTE ("PAGES") À UN TEXTE...
    urlNumerote = url + str(url1) ### "URL1" EST UN NOMBRE, ISSU DE LA LISTE "PAGES", DONC C'EST CE QUE TU VEUX PLUTÔT AJOUTER À LA VARIABLE "URL"
    print(urlNumerote)

    contenu = requests.get(urlNumerote, headers=entetes)
    page = BeautifulSoup(contenu.text,"html.parser")

    recettes = page.find_all("div",class_="recipeofweek-title")
    # print(recettes)
    # print(len(recettes)) ### AVEC CETTE COMMANDE, JE RÉALISE QU'IL Y A 11 RECETTES PAR PAGE

    for recette in recettes: ### EXCELLENT

        urlrecette = recette.find("a")["href"]
        print(urlrecette)
        contenu = requests.get(urlrecette, headers=entetes)
        pagerecette = BeautifulSoup(contenu.text,"html.parser")

        ingredients = pagerecette.find_all("li", class_="ingred")

        # titres = page.find("h1", class_="name-of-dish-size")
        titre = pagerecette.find("div", class_="name-of-dish").text.strip() ### EN FAIT, ON A UN NOM PLUS COMPLET AINSI + IL N'EST PAS NÉCESSAIRE DE LE METTRE AU PLURIEL
        titre = titre.replace("\n"," ").replace("  "," ").strip() ### POUR RETRANCHER DES "RETURN" DANS LES NOMS DE RECETTE

    #     for titre in titres: ### CETTE BOUCLE EST INUTILE, CAR IL N'Y A QU'UN TITRE POUR CHAQUE RECETTE...
    #         # print(titre)

        for ingredient in ingredients: ### CETTE BOUCLE-CI EST PARFAITE: SI TU VEUX UN INGRÉDIENT SUR CHACUNE DES LIGNES DE TON CSV, C'EST LA FAÇON DE FAIRE
            i = ingredient.text.strip().split("\n") #\n = séparer en fonction du return
            # print(ingredient.text.strip())
        # print(i)
            try:
                ingr = i[1].strip()
                qute = i[0].strip()
            except: ### POUR LES CAS, RARES, OÙ IL N'Y A PAS DE QUANTITÉ D'UN INGRÉDIENT DONNÉ
                ingr = i[0].strip()
                qute = ""

            ### J'AJOUTE CES DEUX PETITES CONDITIONS POUR LES CAS OÙ L'UNITÉ DE MESURE DE L'INGRÉDIENT EST PLACÉE AVEC LE NOM DE L'INGRÉDIENT ET NON DE LA QUANTITÉ
            if "c.à.s" in ingr:
                ingr = ingr.replace("c.à.s.","").replace("c.à.s","").strip()
                qute = qute + " c. à s."
            elif "c. à s." in ingr:
                ingr = ingr.replace("c. à s. ","").strip()
                qute = qute + " c. à s."
            elif "c.à.t" in ingr:
                ingr = ingr.replace("c.à.t.","").replace("c.à.t","").strip()
                qute = qute + " c. à t."
            
            infos = [ ### ICI, IL FALLAIT INDENTER CETTE VARIABLE, PLUS LE CODE QUI SUIT, D'UN CRAN VERS LA DROITE
                url1,
                titre, 
                qute, 
                ingr
            ]

            print(infos) ### J'AIME TOUJOURS AFFICHER DANS LE TERMINAL CE QUI SERA ÉCRIT DANS LE CSV.

            harry = open(fichier,"a")
            potter = csv.writer(harry)
            potter.writerow(infos)
        
        print("&"*25) ### PETIT SÉPARATEUR QUI S'AFFICHERA ENTRE CHAQUE RECETTE
                
    #         # print(qute)
    #         # <h1 class="name-of-dish-size">Côtelettes de porc poêlées</h1>
