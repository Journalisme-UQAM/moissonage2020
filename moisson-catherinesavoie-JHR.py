# coding : utf-8 
#faire dérouler le code HTML de la page d'accueil de l'hebdo : l'oeil régional 

from bs4 import BeautifulSoup 
import requests

#faire ensuite dérouler dans le terminal les urls des articles écrits par les journalistes de l'oeil régional dernièrement. 

import csv 
import requests 
from bs4 import BeautifulSoup

### BONJOUR CATHERINE : J'AI FAIT PLUSIEURS AJUSTEMENTS À TON SCRIPT, TOUS EXPLIQUÉS PAR LE BIAIS DE COMMENTAIRES PRÉCÉDÉS DE ###
### IL Y AVAIT TROIS TENTATIVES DIFFÉRENTES DE SE CONNECTER AU SITE DU JOURNAL DANS TON SCRIPT
### J'EN AI CONSERVÉ QU'UNE SEULE, CELLE SE TROUVANT DANS LA BOUCLE

fichier = "loeil_regional-JHR.csv"
urlDebut = "https://www.oeilregional.com/?p="
nombres = list(range(20000,20900)) ### PARFAIT!

entetes = {"User-Agent" : "Catherine Savoie - requête acheminée dans le cadre d'un cours de journalisme de données",
"From":"###@###.com" 
}

for nombre in nombres: 
    urlarticle = urlDebut + str(nombre)
    print(urlarticle)
    contenu = requests.get(urlarticle,headers=entetes)
    page = BeautifulSoup(contenu.text, "html.parser") ### IL MANQUAIT UN POINT ENTRE "HTML" ET "PARSER"

    # print(page) ### CE PRINT DOIT ÊTRE INDENTÉ À L'INTÉRIEUR DE LA BOUCLE
    
    # print(page.find("div", class_="author").text) ### CETTE COMMANDE NE FONCTIONNE PAS...

    try:
        titre = page.find("div", class_ = "title").text.strip()
        date = page.find("div", class_ = "date").text.strip()
        auteur = page.find("div", class_ = "author").text.replace("Par: ","").replace("Par ","").strip() ### L'AUTEUR EST PRÉCÉDÉ D'UN "PAR:", ON S'EN DÉBARRASSE AVEC UN "REPLACE"

        infos = [urlarticle,titre,date,auteur]
        print(infos)

        ### IL MANQUAIT LE CODE POUR ÉCRIRE LES INFOS QUE TU MOISSONNES DANS UN CSV

        riviere = open(fichier,"a")
        richelieu = csv.writer(riviere)
        richelieu.writerow(infos) 
    except:
        print("Pas un article....")


    
    print("*"*33)
    

