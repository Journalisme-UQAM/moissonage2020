# coding : utf-8

# Un script de Jessica Potsou
### BRAVO POUR UN SCRIPT TRÈS BIEN DOCUMENTÉ

# Dans ce script, je vais faire une recherche dans les archives de La Presse
# Je vais sortir les urls des articles de février 2010 qui parlent des Jeux Olympiques de Vancouver

# Je dois en premiers lieux importer les extensions requests, csv et beautifulSoup
import requests
import csv
from bs4 import BeautifulSoup

# Je donne tout de suite le nom au fichier que je veux générer
fichier = "article_jo-JHR.csv"

# Voici la constante de l'url qui me mène à la page d'une journée dans les archives (lorsque je la modifie, ce que je ferai plus tard)
# Cette variable ne sera pas réutilisée mais me servira de rappel
urldebut = "https://www.lapresse.ca/archives/2010/2/.php"

# Voici l'entête qui accompagnera ma requête
entetes = {
    "User-Agent": "Jessica Potsou - requête envoyée dans le cadre d'un cours de journalisme de données",
    "From":"p***.J***@c***.u***.ca"
}

# Je fais une liste qui contient mon range de date (en 2010, le mois de février comptait 28 jours)
### JE RESTREINT TA CUEILLETTE AUX JOURS DURANT LESQUELS LES JEUX ONT EU LIEU
jours = list(range(12,29))

# Je fais une liste de vide dans laquelle je vais ajouter plus tard mes urls d'articles
liste = []

# Je fais une boucle pour générer les urls qui mènent à la page d'une journée d'archive
for jour in jours:
    # Comme mes urls seront des dates du mois de février, je modifie mon url de la façon suivante: 
    # J'utilise la fonction .format, car je dois inséré mon jour à l'intérieur de mon url et non à la fin
    urljours = "https://www.lapresse.ca/archives/2010/2/{}.php".format(jour)
    # J'ai fait un print pour voir que j'arrive bien à générer mes urls de journée... j'ai mis le print en commentaire
    # print (urljours)
    # Je fais une requête pour pouvoir moissonner mes donnés dans toutes les pages de journée
    contenu = requests.get(urljours, headers=entetes)

    # Je vais analyser mes donner avec l'aide de BeautifulSoup et sa fonction « parse »
    page = BeautifulSoup(contenu.text, "html.parser")

    # Je forme une seconde boucle pour trouver mes urls d'article pour chaque journée du mois de février 2010
    # J'ai trouver la formule suivante (les deux prochaines lignes) sur internet... elle me permet de sortir l'url de chaque article du mois
    for article in page.find("ul", class_="square square-spread").find_all("a") :
        urlarticle = article.get('href')
        # J'ai fait un print pour vérifier que ma formule fonctionne... J'ai mis le print en commentaire
        # print (urlarticle)

        # J'ai fait une condition pour trouver les urls de tous les articles qui parlent des JO de Vancouver
        # Il y a une constance dans tous ces urls... ils contiennent tous la chaine de caractères « vancouver-2010 »
        if "vancouver-2010" in urlarticle:
            print(urlarticle) ### POUR VÉRIFIER EN CAS DE PLANTAGE

            ### C'EST ICI QUE ÇA SE COMPLIQUE
            ### TON CODE NE FAIT QU'AJOUTER LES URLS UN À LA SUITE DES AUTRES
            ### ON VA LE CHANGER

            # jo = urlarticle
            # # J'ai fait un print pour m'assurer que ma condition fonctionne, je l'ai mis en commentaire
            # # print (jo)
            # # J'ai utilisé la fonction .split pour séparer chaque url
            # jeux = jo.split(',')
            # # J'ai ajouté mes urls séparés à ma liste de vide en utilisant la fonction .append
            # liste.append(jeux)

            ### IL SERAIT BIEN D'ALLER CHERCHER D'AUTRES INFOS DANS CES ARTICLES, COMME LE TITRE, LA DATE ET LE NOM D'AUTEUR(TRICE)
            ### POUR ÇA, IL FAUT OUVRIR CHACUN DES ARTICLES EN S'Y CONNECTANT AVEC REQUESTS ET EN LES ANALYSANT AVEC BEAUTIFULSOUP

            contenuArticle = requests.get(urlarticle, headers=entetes)
            pageArticle = BeautifulSoup(contenuArticle.text, "html.parser")

            auteur = pageArticle.find("p", class_="author").text.strip().replace("\n"," ") ### ON AJOUTE UN "REPLACE" POUR ENLEVER LES "RETURN" OU "ENTER" QUI SE TROUVENT DANS CERTAINS NOMS D'AUTEUR
            titre = pageArticle.find("span", class_="title").text.strip()
            j = urlarticle[urlarticle.find("201002")+7:urlarticle.find("201002")+9]
            date = "{} février 2010".format(j)

            infos = [urlarticle,auteur,titre,date]
            print(infos)

# J'ai créé mon fichier csv à partir de ma liste contenant mes urls d'articles sur les Jeux Olympiques de Vancouver 2010
# c1 = open(fichier, "a")
# c2 = csv.writer(c1)
# c2.writerow (liste)

### TOUT CE QU'IL MANQUAIT, C'ÉTAIT D'INDENTER LE CODE D'ÉCRITURE DANS TON FICHIER CSV DE QUELQUES CRANS VERS LA GAUCHE POUR QU'IL SE TROUVE À L'INTÉRIEUR DE TA BOUCLE
            c1 = open(fichier, "a")
            c2 = csv.writer(c1)
            c2.writerow (infos)