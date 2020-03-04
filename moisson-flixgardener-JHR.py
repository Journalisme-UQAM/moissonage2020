# coding : utf-8
import requests, csv, json
from bs4 import BeautifulSoup

fichier = "articlesmariage-JHR.csv"

# Mon objectif est de créer un fichier csv avec tous les articles de mariage disponibles à l'achat en ligne
# sur le site de Dollarama... ### OK! ORIGINAL! :)

entete = {
	"User-Agent":"Félix Desjardins",
	"From":"F***@***.com"
}

for x in range(1,9):
	url = "https://www.dollarama.com/fr-CA/activite/evenements-fetes-et-organisation-de-mariages?page="+str(x)
	contenu = requests.get(url,headers=entete)
	# print(contenu)
	page = BeautifulSoup(contenu.text, "html.parser")
	print()
	articles = page.find_all("div", class_="product-tile-text")
	
	for article in articles:
		print ((article.find("a", class_="js-display-name")).text)
		print ("_"*50)
		print ((article.find("div", class_="product-tile-price")).text)
	
	# dead = open(fichier,"a") ### TOUT D'ABORD, IL FAUT SIMPLEMENT QUE L'ÉCRITURE DES ITEMS QUE TU RECUEILLES SE FASSE UN ITEM À LA FOIS, ET DONC, IL FAUT L'INDENTER DANS LA BOUCHE "FOR ARTICLE IN ARTICLES"
	# obies = csv.writer(dead)
	# obies.writerow(articles) ### CE QUE TU ÉCRIS, ICI, C'EST TOUTE TA VARIABLE "ARTICLES", QUI CONTIENT TOUS LES ARTICLES SE TROUVANT DANS UNE PAGE DONNÉE. ÉCRIS PLUTÔT UNE LISTE DES INFOS QUE TU RECUEILLES, À SAVOIR LE NOM ET LE PRIX

		nom = article.find("a", class_="js-display-name").text
		prix = article.find("div", class_="product-tile-price").text

		### ET POURQUOI NE PAS IMMÉDIATEMENT TRANSFORMER LES PRIX EN NOMBRES

		prix = float(prix.replace("$/unité","").replace(",",".").strip())

		infos = [nom,prix,url]

		dead = open(fichier,"a")
		obies = csv.writer(dead)
		obies.writerow(infos)

		### ENFIN, IL MANQUAIT UN FICHIER CSV À CE QUE TU AS REMIS DANS GITHUB...