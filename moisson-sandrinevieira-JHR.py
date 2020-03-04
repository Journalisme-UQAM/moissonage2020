#coding: utf-8

#Salut Jean-Hugues! J'ai choisi de "moissonner" la page de la Chambre des communes du Canada, qui contient les informations des 338 députés fédéraux.
#Je chercherai à obtenir quatre (parfois cinq) informations pour chacun de ces 338 députés : leur nom, parti politique, circonscription et la provincipe de cette dernière.
#Je dis parfois cinq, car dans certains cas, des députés ont des titres tel que "L'honorable" ou "Le très honorable" (dans le cas de Justin Trudeau).
#C'est parti! 

### EXCELLENT SCRIPT! HORMIS CERTAINS DÉTAILS... ET UN PROBLÈME PLUS IMPORTANT À LA FIN :)
### EN OUTRE, TON SCRIPT RECUEILLE UNE INFORMATION QUI EST FACILEMENT TÉLÉCHARGEABLE EN CSV DIRECTEMENT SUR LE SITE DES COMMUNES ("https://www.noscommunes.ca/Members/fr/search/csv")
### IL AURAIT ÉTÉ BIEN QU'IL AILLE CHERCHER D'AUTRES INFOS SUR CHACUN(E) DES DÉPUTÉ(E)S

import requests, csv
from bs4 import BeautifulSoup

#Création du futur fichier csv qui contiendra les données.
#Le w+ est pour s'assurer que les données ne s'accumulent pas à chaque fois que le script roule. 
# fichier = "députésfédéraux.csv" ### ÉVITE LES ACCENTS DANS LES NOMS DE FICHIERS
fichier = "deputesfederaux-JHR.csv"
HarryPotter = open(fichier, "w+")

#Ceci est le lien vers la page des députés de la Chambre des communes
url= "https://www.noscommunes.ca/Members/fr/recherche"

#Je m'identifie par politesse!
entetes= {
    "User-Agent":"Sandrine Vieira; étudiante en journalisme à l'UQAM"
}

#Requête pour aller moissonner la page
contenu = requests.get(url, headers=entetes)
print(contenu.status_code)

page = BeautifulSoup(contenu.text, "html.parser")
#print (page) 

#print(page.find("tr"))
#Cela m'indique les quatre variables principales que je recherche: Nom, parti politique, circonscription et province. J'ai noté qu'elles se trouvaient à l'intérieur des balises "tr". 

#print((page.find_all("div", class_="col-lg-4 col-md-6 col-xs-12"))
#Cela me donne les informations groupées de tous les députés. Lors d'anciennes tentatives, je cherchais seulement la classe des noms, ce qui me donnait une liste des 338 noms, mais pas toutes des autres informations propres à chaque député. 
#J'ai ensuite analysé plus longuement la structure de la page HTML pour remarquer que ce que les 338 députés ont en commun est la classe "col-lg-4 col-md-6 col-xs-12".
#Ainsi, cette fonction me permet d'avoir toutes les informations de chaque député, embriquées dans des balises. 

#print(len(page.find_all("div", class_="col-lg-4 col-md-6 col-xs-12")))
#Vérification que tout concorde jusqu'à date : cela me confirme bien qu'il y a 338 députés dans la liste. On peut continuer. 

#Je place mon contenu dans une variable que je nomme "députés"
deputes = page.find_all("div", class_="col-lg-4 col-md-6 col-xs-12") 

#Je crée une boucle pour aller chercher tout ce qu'il me faut et je définie les variables après les avoir tester avec un print. 
for depute in deputes:
    # Statut = depute.find(class_="ce-mip-mp-honourable").text.strip() ### ÉVITE ÉGALEMENT DE DÉBUTER LES NOMS DE VARIABLES AVEC DES MAJUSCULES
    statut = depute.find(class_="ce-mip-mp-honourable").text.strip() 
    nomDepute = depute.find(class_="ce-mip-mp-name").text.strip()
    partiPolitique = depute.find(class_="ce-mip-mp-party").text.strip()
    circonscription = depute.find(class_="ce-mip-mp-constituency").text.strip()
    province = depute.find(class_="ce-mip-mp-province").text.strip()

    #Créer la liste
    infos = [statut,nomDepute,partiPolitique,circonscription,province]
    #print(Infos)

    #Un problème: un espace s'affiche devant les noms des députés qui n'ont pas de statut spécial. Je vais donc les retirer, afin de bien ordonner les données. 
    ### EN FAIT, CE N'EST PAS UN PROBLÈME
    ### LE CODE DES DEUX PROCHAINES LIGNES CRÉE UN PROBLÈME PLUS GRAVE QUE CELUI QU'IL PERMET DE RÉGLER
    ### IL FAIT EN SORTE QUE LES INFORMATIONS SONT MAL ALIGNÉES DANS LE CSV QUI EST PRODUIT PAR TON SCRIPT
    ### C'EST AINSI QUE LA PREMIÈRE COLONNE, QUI DOIT NORMALEMENT CONTENIR LE STATUT, CONTIENT PARFOIS UN TITRE COMME "L'HONORABLE", ET PARFOIS... LE NOM DE L'ÉLU(E)
    ### PAR SOUCI DE COHÉRENCE, JE VAIS DONC METTRE LES DEUX PROCHAINES LIGNES EN COMMENTAIRE POUR NE PAS QU'ELLES SOIENT EXÉCUTÉES
    # infosDeputesCompletes = list(filter(None, infos))
    # print(infosDeputesCompletes)

    #Les valeurs vides sont maintenant retirées. Tout est prêt pour la création du fichier csv.
    Dumbledore = csv.writer(HarryPotter)
    Dumbledore.writerow(infos)