# je crois avoir réussi l'entièreté de mon travail sauf pour une chose : la dernière balise que je devrais trouver pour pouvoir imprimer le titre des articles et non seulement les liens. Comme je suis aux jeux de la communication, je n'ai pas eu l'opportunité de le travailer plus tard que mardi le 18.

# coding : utf-8

import requests, csv 
from bs4 import BeautifulSoup

# with open('spotmini.csv', 'w', newline='') as csvfile: ### NE MARCHE PAS...

fichierCSV = "theverge-JHR.csv"

# mon objectif est de moissonner tous les articles de The Verge qui traitent du chien-robot de la firme Boston Dynamics : le Spot Mini

url = "https://www.theverge.com/tech/archives/"

entetes = {
     "User-Agent":"Félix Pedneault - ###/###-#### : requête envoyée dans le cadre d'un cours de journalisme pour un reportage numérique",
     "From":"f**.**1@**.**"}

# je dois créer un moyen de fouiller toutes les pages d'archives de la section Tech de The Verge. C'est 15 pages. La première page des archives s'appellent url/archives/ par contre, son numéro n'est donc pas 1, ce qui pourrait causer problème à mon code.
### LA PAGE 1 FONCTIONNE; TU PEUX UTILISER L'URL "https://www.theverge.com/tech/archives/1"
### MAIS ENCORE MIEUX. EN FOUILLANT UN PEU DANS LE SITE, TU AURAIS CONSTATÉ QU'ILS ONT UNE SECTION "FULL ARCHIVE" DANS LAQUELLE TU PEUX FOUILLER PAR JOUR: "https://www.theverge.com/archives/tech/2020/1/1" POUR LE 1ER JANVIER 2020.

# page = list(range(2,16))
page = list(range(1,16)) ### AJUSTONS L'INTERVALLE EN CONSÉQUENCE

n = 0
for numero in page:
    # if numero < 2: ### CONDITION QUI N'EST PLUS NÉCESSAIRE
    #     numero = "" + str(numero)
    urlpage = url + str(numero)
    print(urlpage)

# r = requests.get(url)
# section1 = BeautifulSoup(r.text, "html.parser")
# section2 = ""

# n = 0 
# numero = 1
# while section2 != section1:
#     # print(section1)
#     numero = numero +1
#     section2 = section1
    urlpage = url + str(numero)

    r = requests.get(urlpage)
    section1 = BeautifulSoup(r.text, "html.parser")

    articles = section1.find_all("h2", class_="c-entry-box--compact__title")

    #ici je cherche des caractères clés dans les titres d'articles

    for article in articles: 

        ### LE CODE CI-DESSOUS ÉTAIT INDENTÉ D'UN CRAN DE TROP À DROITE...
        n += 1
        
        articleurl = article.find("a")["href"]
        print(n, articleurl)
        # print("."*10)

        # articletitre = section1.find(, class_="c-entry-box--compact__title").text.strip() ### IL Y A UNE ERREUR, ICI. TU DOIS DÉFINIR UN ÉLÉMENT HTML À CHERCHER, SINON NE PAS METTRE DE VIRGULE SEULE DEVANT LA CLASSE
        articletitre = section1.find(class_="c-entry-box--compact__title").text.strip() ### EN OUTRE, CE CODE NE RECUEILLE QUE LE TITRE DU PREMIER ARTICLE DE LA PAGE...

        ### EN FAISANT FONCTIONNER TON SCRIPT, ON NE RECUEILLE AUCUN ARTICLE, DONC À QUOI BON NE CHERCHER QUE DES ARTICLES SUR UN SEUL SUJET QUE TU POURRAIS TROUVER AUTREMENT (VIA UNE RECHERCHE GOOGLE, PAR EXEMPLE)
        ### LE PRINCIPE DU MOISSONNAGE EST D'ALLER CHERCHER BEAUCOUP DE DONNÉES, DE DOCUMENTS, QU'IL SERAIT DIFFICILE DE RECUEILLIR AUTREMENT.
        ### DONC, MOISSONNONS TOUT LE CONTENU DES ARCHIVES DE THE VERGE.
        ### AJOUTONS SIMPLEMENT LE TITRE DE CHAQUE ARTICLE

        titreArticle = article.find("a").text.strip()

        infos = [n,titreArticle,articleurl]

        print("."*10)
        
        # if "SpotMini" in articletitre or "spotmini" in articletitre or "spot" in articletitre or "Spot" in articletitre or "Boston Dynamics" in articletitre:
        #     print(articletitre)   
        #     print("."*10)
        #     spamwriter = csv.writer(csvfile, delimiter=' ',
        #                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     spamwriter.writerow([articletitre] + [articleurl])

### JE NE SAIS PAS OÙ TU AS TROUVÉ LE CODE CI-DESSOUS, MAIS ÇA NE MARCHE PAS, MÊME EN CHANGEANT LE NOM DE LA VARIABLE QUI EST INSCRITE DANS LA FONCTION "WRITEROW"
        # spamwriter = csv.writer(csvfile, delimiter=' ',
        #                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # spamwriter.writerow(infos)

### JE VOUS AI DONNÉ UNE RECETTE. ELLE FONCTIONNE.

        felix = open(fichierCSV, "a")
        pedno = csv.writer(felix)
        pedno.writerow(infos)