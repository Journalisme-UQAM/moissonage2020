# coding : utf-8

#1. Ligne de script afin de pouvoir lire/ travailler avec des fichiers de type .csv

import csv, requests
from bs4 import BeautifulSoup

#2. J'ai choisi de travailler à partir de la liste d'archive de la section basketball du site web ESPN.

urlDebut ="http://www.espn.com/nba/news/archive/_/month/february/year/2019"
n = 0

#3. À cette étape, je demande de me connecter au serveur des archives de ESPN afin de pouvoir en extraire les informations que je recherche (dans ce cas-ci, je veux voir la totalité des articles des archives de ESPN.)

entetes = {
#     "user-Agent":"Simon Duclos - ###-###-### : "request sent as part of a web scrapping exercise (journalism class)" ### ERREUR ICI: TU DOIS ENLEVER LES GUILLEMETS SE TROUVANT AU MILIEU DE LA VALEUR QUE TU DONNES À LA CLÉ "USER-AGENT" + UN SEUL "P" À SCRAPING :)
    "user-Agent":"Simon Duclos - ###-###-### : request sent as part of a web scraping exercise (journalism class)" 
}

# req = requests.get(url,headers=entetes) ### ICI, LA VARIABLE "URL" N'EXISTE PAS...
req = requests.get(urlDebut,headers=entetes)

# print(req)

#4. J'utilise cette fonction afin de trouver le «block» d'archive au sein du code html

# articles = page.find_all("archive", class_="archive-block") ### ICI PAGE N'EXISTE PAS ENCORE... IL FAUT AUPARAVANT UTILISER BEAUTIFUL SOUP!

page = BeautifulSoup(req.text,"html.parser")

# articles = page.find_all("archive", class_="archive-block") ### ES-TU ALLÉ VOIR LE CODE HTML DE LA PAGE? IL N'Y A AUCUN ÉLÉMENT HTML ARCHIVE, NI AUCUN ÉLÉMENT DONT LA CLASSE EST "ARCHIVE-BLOCK"!
articles = page.find("ul", class_="inline-list").find_all("li")

#5. J'utilise en suite cette fonction pour localiser tous les urls présents au sein des archives de la section basketball de ESPN.

# for articles in articles: ### TU ÉCRIS "FOR *ARTICLES* ..." -> CETTE VARIABLE DOIT ÊTRE ÉCRITE AU SINGULIER...
for article in articles: 
        n += 1 ### BONNE IDÉE DE SE SERVIR D'UN COMPTEUR... ENCORE FAUT-IL L'INITIALISER AVANT LA BOUCLE...
        #print(article)
#ERREUR D'INTENTATION À LA LIGNE 33 - JE NE SUIS PAS EN MESURE DE LA CORRIGER - 
### J'AI PLUTÔT UNE ERREUR DE SYNTAXE, DE MON CÔTÉ
        # urlarticle= article.find"a"["href"] ### IL MANQUE LES PARENTHÈSES AUTOUR DU "a"
        urlarticle = article.find("a")["href"]
        # print(n, urlArticle) ### ICI, LE "A" MAJUSCULE FAIT EN SORTE QUE CE NOM DE VARIABLE EST INCONNU ET NE FONCTIONNE PAS...
        print(n, urlarticle)
        # print("."=10) ### CE N'EST PAS =10, MAIS *10 (FOIS 10)
        print("."*10)

#6. Cette fonction suivante sera utilisée pour trouver diverses informations au sein des articles (urls) EX: Nom de l'auteur
        
        # siteArticle = requests.get(urlarticle),headers=entetes
        siteArticle = requests.get(urlarticle,headers=entetes)
        # pageArticle = BeautifulSoup(siteArticle.text, "htmlParser")
        pageArticle = BeautifulSoup(siteArticle.text, "html.parser")

        # print(pageArticle) ### POUR FAIRE UN TEST

        # nomAuteur = pageArticle.find("div", class_="author-listing").text, strp) ### ICI ENCORE, IL N'Y A AUCUN ÉLÉMENT DE CLASSE "AUTHOR-LISTING" DANS LES PAGES DES ARTICLES... AUSSI, "STRP" N'EXISTE PAS...
        nomAuteur = pageArticle.find("span", class_="author").text.strip()
        # nomAuteur = pageArticle.find("ul", class_="authors")
        # print(nomAuteur)
#         try:
#             Titre = pageArticle.find("h1", class_="short".text.strip)
#             except:
#                 try:
#         Titre = pageArticle.find("h1", class_="medium".text.strip)
#         except:
        titreArticle = pageArticle.find("title").text
        # print(titreArticle)

        ### ON POURRAIT AUSSI AJOUTER UNE DESCRIPTION DU TEXTE ET LE MOMENT DE PUBLICATION

        desc = pageArticle.find("meta", attrs={"property":"og:description"})["content"]
        moment = pageArticle.find("meta", attrs={"name":"DC.date.issued"})["content"]

        ### ET ON VA METTRE TOUTES CES INFOS DANS UNE LISTE QU'ON VA APPELER... INFOS

        infos = [n,titreArticle,nomAuteur,desc,moment,urlarticle]
        print(infos)

# #7. À partir de cette étape je dois trouver ma donné HTML EX : «p» à l'intérieur de ma page web HTML me permettant de générer ma boucle contenant tous les urls.
# #*DANS MON CAS CETTE DONNÉE SEMBLE ÊTRE «title»; elle regroupe chaque url (article) de la section basketball de l'année 2019.
#               titre ="title"

#               print(Titre)

# #*Adevenant que le script fonctionnerait j'obtiendrait une boucle contenant tous les urls des articles de la section basketball de l'année 2019 du site web d'ESPN.

# #9. Pour terminer je dois maintenant produire un fichier .csv en faisant la fonction suivante
#         nba = open(fichier,"Devoir3.py") ### POURQUOI ÉCRIS-TU LE NOM DE TON SCRIPT, ICI???
#         archives =  csv.writer(nba)
#         archives.writerow(infos) ### TA VARIABLE "infos" N'EST PAS CRÉÉE PLUS HAUT...

                ### BEL EFFORT, MAIS JE VOUS AI DONNÉ LA "RECETTE" POUR CRÉER UN CSV. C'EST CELLE-CI:

        nba = open("archivesNBA-JHR.csv", "a")
        archives = csv.writer(nba)
        archives.writerow(infos)
