# coding : utf-8

# Ici, je vais importer les modules nécessaires

### TRÈS BONNE IDÉE QUE DE PUISER DANS UN API PEU CONNU

import csv
import json
import requests
from canlii import cle ### J'AI RECOURS À CETTE MÉTHODE POUR NE PAS RÉVÉLER PUBLIQUEMENT TA CLÉ D'API;
### EN OUTRE, LE FICHIER DANS LEQUEL JE L'AI PLACÉ EST DANS le .gitignore POUR ÉVITER QU'IL SOIT RENDU PUBLIC DANS GITHUB

# Création du fichier

fichier = "jugementsassurance-JHR.csv"

# Création de la première requête envoyée à l'API de la CANLII. 

url = "https://api.canlii.org/v1/caseBrowse/fr/?api_key={}".format(cle)

entetes = {
    "User-Agent":"Charles Mathieu - ### : requête envoyée dans le cadre d'une démarche journalistique", 
    "From":"###@#.com"
}

r = requests.get(url,headers=entetes)

# print(r)

# En fait, cette première requête permet d'obtenir les différents codes des tribunaux du Canada.

if r.status_code == 200:
    tribunaux = r.json()
    # print(tribunaux)
    listeID = [] ### TU CRÉAIS CETTE LISTE DANS TA BOUCLE. CE FAISANT, ELLE NE CONTIENAIT TOUJOURS QU'UN SEUL ÉLÉMENT, LE DERNIER. JE L'AI PLACÉ AVANT TA BOUCLE
    for tribunal in tribunaux["caseDatabases"]:
        if tribunal["jurisdiction"] == "qc":
            
            # J'ai décidé d'aller chercher les codes des différents tribunaux du Québec seulement, afin de limiter la quantité de jugements que je vais obtenir. 
            # Ici je vais créer une liste des codes afin de pouvoir l'utiliser plus tard lors d'une deuxième requête. 
            # listeID = [] ### IL FAUT CRÉER TA LISTE AVANT D'ENCLENCHER TA BOUCLE, SINON, ELLE NE CONTIENDRA TOUJOURS QU'UN SEUL ÉLÉMENT, LE DERNIER
            # Définition de la variable IDtribunaux afin de pouvoir l'ajouter dans une liste. 
            IDtribunaux = tribunal["databaseId"]
            listeID.append(IDtribunaux)
    # print(listeID)
            # for i in listeID: ### UNE FOIS QUE TA LISTE INITIALE EST CRÉÉE, TU DOIS SORTIR DE CETTE BOUCLE-CI POUR FAIRE UNE ITÉRATION DANS TA LISTE
    for i in listeID: ### DONC ICI PLUTÔT
                
        # Création d'une boucle permettant de formater le deuxième URL utilisé pour la prochaine requête. 

        # url1 = "https://api.canlii.org/v1/caseBrowse/fr/{}/?offset=0&resultCount=10000&&decisionDateAfter=2018-12-31&api_key={}"
        url1 = "https://api.canlii.org/v1/caseBrowse/fr/{}/?offset=0&resultCount=10000&&decisionDateAfter=2018-12-31&api_key={}".format(i,cle)
        # url2 = url1.format(i) ### 2E ÉTAPE NON NÉCESSAIRE
        
        # Ici, j'ai envoyé la deuxième requête, qui me permet d'aller chercher les différentes décisions, leur titre, une "citation" et le code de chaque décision qui a été déposé sur la CANLII. 

        r2 = requests.get(url1,headers=entetes)

        if r2.status_code == 200:
            decisions = r2.json()
            # print(decisions)
            for decision in decisions["cases"]:
                if "surance" in decision["title"]:
                    
                    # Cette condition me permet d'aller chercher les décisions qui contiennent uniquement le mot "surance" pour aller chercher les décisions ayant les mots "assurance" et "insurance" dans le titre. 
                    
                    listejugements = [] 
                    
                    # Création d'une liste et des variables qui seront mises dans la liste. 
                    
                    tribunal1 = decision["databaseId"]
                    titre = decision["title"]
                    citation = decision["citation"]
                    # IDdossier = decision["caseId"] ### ÉVITE LES MAJUSCULES COMME PREMIÈRE LETTRE DU NOM D'UNE VARIABLE
                    iDdossier = decision["caseId"] ### ÉVITE LES MAJUSCULES COMME PREMIÈRE LETTRE DU NOM D'UNE VARIABLE
                        
                    listejugements.append(titre)
                    listejugements.append(citation)
                    listejugements.append(tribunal1)
                    
                    # # Parce que des fois, le code est dans IDdossier["fr"] ou dans IDdossier["en"], j'ai dû créer une condition afin que lorsque c'Est en "fr", il l'ajoute à une certaine liste, et que lorsque c'est en "en", il l'ajoute aussi. 
                    ### ICI, TA SOLUTION EST BONNE:

                    # for e in IDdossier:
                    #     listeidcase = []
                    #     if "fr" in e:
                    #         idf = IDdossier["fr"]
                    #     elif "en" in e:
                    #         idf = IDdossier["en"]
                    #     listejugements.append(idf)

                    ### MAIS CELLE-CI EST PEUT-ÊTRE PLUS SIMPLE:

                    try:
                        iDdossier = decision["caseId"]["fr"]
                    except:
                        iDdossier = decision["caseId"]["en"]
                    listejugements.append(iDdossier)

                    # print(listejugements)
                        
                    #     # Pour être en mesure de cibler toutes les décisions, j'ai créé une nouvelle liste avec tous les codes des différents jugements. 
                        
                    #     listeidcase.append(idf)
                        
                    #     # Création d'une nouvelle boucle afin d'ajouter toutes les décisions dans le troisième URL utilisé pour la troisième requête. 

                    #     for c in listeidcase:

                    ### CETTE DERNIÈRE BOUCLE, CI-DESSUS, N'EST PAS NÉCESSAIRE
                    ### TU AS DÉJÀ LE CODE DU JUGEMENT. IL SE TROUVE DANS LA VARIABLE iDdossier.
                    ### DONC, TU PEUX IMMÉDIATEMENT T'EN SERVIR POUR COMPLÉTER LES INFORMATIONS

                    #         # Je vais formater les différents URL, dans lesquels j'ai ajouté des accolades afin de pouvoir aller cibler tous les codes des jugements et tous les codes des tribunaux. 

                    #         url3fin = "/{}/?api_key=###".format(c)
                    #         url3debut = "https://api.canlii.org/v1/caseBrowse/fr/{}".format(i)
                    #         url3 = url3debut + url3fin

                    url3 = "https://api.canlii.org/v1/caseBrowse/fr/{}/{}/?api_key={}".format(i,iDdossier,cle)
                    # print(url3)
                    r3 = requests.get(url3,headers=entetes)
                    #         # La troisième requête me permet d'aller chercher la date de décision et les "keywords", qui indiquent ce dont il a été question dans la décision en question. Je crois que je vais tenter de filtrer tous les jugements en fonction des "keywords" la prochaine fois que je vais fouiller dans cet API. 
                    if r3.status_code == 200:
                        detailsJ = r3.json()
                    #             # Création des variables et ajout de celles-ci à la liste des jugements utilisée pour créer le fichier CSV. 
                        datedecision = detailsJ["decisionDate"]
                        sujets = detailsJ["keywords"]
                        listejugements.append(datedecision)
                        # listejugements.append(sujets)

                        ### ICI, AVEC LES MOTS-CLÉ, JE TE PROPOSE QUELQUE CHOSE
                        ### IL Y EN A TOUJOURS CINQ
                        ### DONC TU PEUX FAIRE UNE LIGNE PAR MOT-CLÉ, CE QUI TE PERMETTRA ENSUITE DE FAIRE UN TABLEAU DYNAMIQUE AFIN DE VOIR QUEL MOT-CLÉ REVIENT LE PLUS FRÉQUEMMENT

                        sujets = sujets.split("—")

                        # listefinale = []

                        for sujet in sujets:                            

                            listefinale = [listejugements[0],listejugements[1],listejugements[2],listejugements[3],listejugements[4]]
                            listefinale.append(sujet.strip())
                            print(listefinale)

                            # Création du fichier CSV. J'ai utilisé mon nom et celui de ma copine pour lui montrer que je l'aime. Vive la Saint-Valentin..! ### AWWW

                            charles = open(fichier, "a")
                            lea = csv.writer(charles)
                            lea.writerow(listefinale)
