# coding: utf-8

import csv, requests
from bs4 import BeautifulSoup 

fichier = "articles-lemonde-JHR.csv"
articleS = []
#je vais tenter d'en faire une liste car mon fichier csv que ca imprime est en désordre...

# url = "https://www.lemonde.fr/archives-du-monde/01-01-2020/"

entetes = {
    "User-Agent":"Eliane Gosselin, étudiante en journalisme au Québec"
}

dates = (range(1,32))
n = 0
for jour in dates:
    if jour < 10:
        jour = "0"+ str(jour)
    url = "https://www.lemonde.fr/archives-du-monde/{}-01-2020/".format(jour)
    # urlDuJour = url + str(jour)
    # print(urlDuJour)
    # print(url)

    ### JUSQU'ICI, ÇA VA TRÈS BIEN!
    ### IL FAUT AUSSI TENIR COMPTE DU FAIT QUE LES ARCHIVES DU MONDE PEUVENT TENIR SUR PLUSIEURS PAGES PAR JOUR.
    ### JE VAIS DONC MODIFIER TON URL EN CONSÉQUENCE DANS UNE BOUCLE QUI VA DE 1 À 10 (10 ÉTANT LE MAXIMUM DE PAGES POSSIBLES POUR LES ARCHIVES D'UNE JOURNÉE)

    for p in range(1,11):
        url = "https://www.lemonde.fr/archives-du-monde/{}-01-2020/{}/".format(jour,str(p))
        # print(url)

        ### ENSUITE, ON VA N'UTILISER QUE LES PAGES QUI EXISTENT (QUI RÉPONDENT 200 QUAND ON TENTE DE S'Y CONNECTER)

        site = requests.get(url, headers=entetes)
        print(site.status_code,url)

        if site.status_code == 200:
            
            page = BeautifulSoup(site.text, "html.parser")
    
            articles = page.find_all("section", class_="teaser") ### ÇA MARCHE SUPER BIEN!
            
            for article in articles: ### CETTE BOUCLE AUSSI FONCTIONNE À MERVEILLE
                # print(article.find("a")["href"])
                n += 1 ### BONNE IDÉE D'INSÉRER UN COMPTEUR
                
                urlArticle = article.find("a")["href"]
                print(n, urlArticle)
                # print("."*10)
                
                siteArticle = requests.get(urlArticle, headers=entetes)
                pageArticle = BeautifulSoup(siteArticle.text, "html.parser")
                
                titreArticle = article.find("h3", class_="teaser__title").text.strip() ### JE VOIS CE QUI NE FONCTIONNE PAS: TU VAS CHERCHER LE TITRE DE L'ARTICLE TEL QU'IL APPARAÎT DANS LA PAGE DES ARCHIVES
                try:
                    titreArticle = pageArticle.find("h1", class_="article__title").text.strip() ### VOICI LE CODE QUI CORRESPOND AU TITRE DE L'ARTICLE TEL QU'IL APPARAÎT DANS LA PAGE DE L'ARTICLE... ET ENCORE, IL EST PARFOIS DANS DES ÉLÉMENTS HTML DIFFÉRENTS
                except:
                    try:
                        titreArticle = pageArticle.find("h1", class_="entry-title").text.strip()
                    except:
                        titreArticle = "?"

                # print(titreArticle)
                # articleS.append(titreArticle)
        
# #         #je suis vraiment proche de trouver le titre, et de les isoler pour chaque article, mais tout ce que j'essaie ne fonctionne pas même si je le vois dans mon code html!!! arghhh ### VOIR COMMENTAIRES AUX LIGNES PRÉCÉDENTES :)

                ### PROFITONS-EN POUR ALLER CHERCHER D'AUTRES INFOS

                try: ### ON ESSAIE AVEC UN "TRY", CAR DANS CERTAINS ARTICLES, IL N'Y A PAS DE "CHAPEAU"
                    chapo = pageArticle.find("p", class_="article__desc").text.strip()
                except:
                    chapo = "?"

                try: ### ON A BESOIN DE FAIRE UN "TRY" ICI AUSSI POUR PALLIER TOUS LES CAS OÙ LA DATE APPARAÎT DANS UNE PAGE STRUCTURÉE UN PEU DIFFÉREMMENT
                    date = pageArticle.find("span", class_="meta__date").text.strip()
                except:
                    try:
                        date = pageArticle.find("p", class_="meta__publisher").text.strip()
                    except:
                        date = "? - "
                
                date = date.split(" - ")[0].strip()
                date = date.replace("Publié le ","").strip()

                # print(titreArticle,chapo,date) ### PETIT TEST À MI-CHEMIN

# #         # nomAuteur = article.find("a", class_="article__author-link").text.strip()
# #         # print(nomAuteur)
# #         # ca m'imprime juste le premier nom et JE SAIS PAS POURQUOI CA IMPRIME PAS LES AUTRES
                try: ### PARFOIS, DES ARTICLES N'ONT PAS DE NOM D'AUTEUR; IL FAUT DONC PRÉVOIR LE COUP AVEC UN "TRY"
                    nomAuteur = pageArticle.find("span", class_="meta__author").text.replace("Par ","").strip()
                except:
                    try: ### DANS D'AUTRES CAS, LE NOM D'AUTEUR EST DANS UN SPAN DONT LE NOM DE CLASSE EST LÉGÈREMENT DIFFÉRENT
                        nomAuteur = pageArticle.find("span", class_="meta__authors").text.replace("Par ","").strip()
                    except:
                        nomAuteur = "?"
        
# #         # dateArticle = <meta property="og:article:published_time" content="2020-01-01T20:36:14+00:00">
        
# #         dateArticle = article.find("span", class_="meta__date").text.strip()
# #         print(dateArticle)
# #         articleS.append(dateArticle)
# #         # nomAuteur = pageArticle.find("section", class_="article_author-link")text.strip()
# #         # print(nomAuteur)

        
# #         try:
# #             nomAuteur = pageArticle.find("span", class_="meta__author").text.strip()
# #         except:
# #             nomAuteur = "aucun"
# #         print(nomAuteur)
# #         articleS.append(nomAuteur)

# # #toutes les infos que je veux s'imprime, reste à voir si le fichier créer sera en ordre
                infosArticle = [n,titreArticle,nomAuteur,date,chapo,urlArticle]
                print(infosArticle)
                print("<~>"*10) ### UN PEU DE DÉCO MET TOUJOURS DU PEP DANS UN SCRIPT

                dead = open(fichier,"a")
                obies = csv.writer(dead)
                obies.writerow(infosArticle)

# #         # j'ai eu de la difficulté à trouver quoi mettre comme variable après mon writerow... 
# # #Ma liste dans mon terminal imprime super bien mais pas mon fichier csv et je ne sais pas pourquoi
        
