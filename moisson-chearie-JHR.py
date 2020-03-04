# coding : utf-8
# Bonjour! Ici je tenterai de recenser toutes les espèces menacées au Québec ainsi que la date à laquelle elles ont été ajoutées à la liste. 

import requests, csv
from bs4 import BeautifulSoup

fichier = "especesMenacees-JHR.csv"

url = "https://mffp.gouv.qc.ca/la-faune/especes/liste-especes-vulnerables/"

entete = {
    "User-Agent" : "Ariane Chevrier, étudiante en journalisme à l'UQAM. Cette requête est envoyée dans le cadre d'un cours de journalisme de données."
}

contenu = requests.get(url, headers=entete)

page = BeautifulSoup(contenu.text, "html.parser")

# print(page) Le HTML de la page imprime bien

### QUAND ON REGARDE COMMENT LA PAGE EST STRUCTURÉE,
### ON SE REND COMPTE QU'IL N'EST PAS UTILE D'ALLER CHERCHER CELA
# nomsFaune = page.find_all("div", class_="table-container")
# print(nomsFaune) # Ce print me permet d'imprimer le contenu de tous les tableaux des espèces menacées ou vulnérables.

### DONC, J'ENLÈVE CETTE BOUCLE
# for nom in nomsFaune:

### CE SONT LES ESPÈCES MENACÉES ET VULNÉRABLES QUI T'INTÉRESSENT,
### DONC, IL FAUT D'ABORD TROUVER LES H2 QUI CONTIENNENT CES DEUX SURTITRES DE TABLEAU

surtitres = page.find_all("h2")

for surtitre in surtitres:
    # print(surtitre.text) ### TEST

    ### ON NE RECUEILLERA DES INFOS QUE DANS LE CAS OÙ LE SURITITRE SERA "ESPÈCES MENACÉES" OU "ESPÈCES VULNÉRABLES"
    if surtitre.text.strip() == "Espèces menacées" or surtitre.text.strip() == "Espèces vulnérables":

        # print(surtitre) ### TEST

        ### ET C'EST ICI QU'ON VA TROUVER LES H3 AVEC LES GRANDES CLASSES D'ANIMAUX (MAMMIFÈRES, OISEAUX, ETC.)
        ### CES H3 SE TROUVENT À L'INTÉRIEUR D'UN DIV QU'ON TROUVE EN UTILISANT FIND_NEXT À PARTIR DU SURTITRE OÙ ON EST RENDU
        ### TU T'ES SERVI D'UN FIND_NEXT PLUS BAS, DONC JE SAIS QUE TU CONNAISSAIS CETTE FONCTION :)
        classes = surtitre.find_next("div").find_all("h3")
        # print(classes)

        for classe in classes:

            # print(classe.text)

            ### ET C'EST ICI QUE TON CODE EST BON, À UN SEUL DÉTAIL PRÈS:
            ### J'UTILISE ENCORE FIND_NEXT POUR NE PRENDRE QUE LES NOMS D'ESPÈCES DE LA CLASSE OÙ ON EST RENDU
            ### CES NOMS SONT DANS UNE TABLE, DONC: FIND_NEXT("TABLE")

    # especes = nom.find_all("h3")
    # for espece in especes:
    #     print("*"*10)
    #     print(espece.text)
        # especesFinales = espece.text
        # J'ai pu sortir tous les types d'animaux menacés.
    
            animaux = classe.find_next("table").find_all("a")
    #     # print(animaux)
    #     # Ce print me permet de générer le contenu des tableaux en-dessous des espèces. Mammifères [a href=https://>Alose savoureuse</a>, <a href=https: .... etc]
            for animal in animaux:
                # print(animal)
                nomEspece = animal.text
    #         # print(prenom)
    #     prenomsFinaux = prenom

                profil = animal["href"]

                ### PROFITONS-EN POUR RAMASSER LE NOM LATIN DE L'ANIMAL, TOUJOURS UTILE

                nomLatin = animal.find_next("td").text.strip()
    #         # print(profil)
    #         # print("*"*10)
    #         # Jusqu'ici, j'ai réussi à sortir tous les noms des animaux avec l'URL vers leur profil. Les types d'animaux séparent également les différentes espèces. J'ai une section mammifères, une section poissons, une section tortues, etc. 
    #         # Ma prochaine étape, assez corsée pour moi, serait de travailler dans chaque URL pour aller chercher leur statut. Ils sont menacés/vulnérables depuis quand?
                ### TU L'AS BIEN RÉUSSIE! :)

                url2 = profil
                entete2 = {
                        "User-Agent" : "Ariane Chevrier, étudiante en journalisme à l'UQAM. Ces requêtes sont envoyées dans le cadre de mon cours de journalisme de données."
                    }
                contenu2 = requests.get(url2, headers=entete2)
                page2 = BeautifulSoup(contenu2.text, "html.parser")

    #     presqueStatut = pages2.find_all("table", id="AutoNumber2")
    #         # print(presqueStatut)
    #     for statut in presqueStatut:
    #         # print(statut)
    #         enfinStatut = statut.find_next("a")
    #         # print(enfinStatut.text)
    #         unJourStatut = enfinStatut.find_next("a")
    #         # print(unJourStatut)
    #         momentDonneStatut = unJourStatut.find_next("a")
    #             # print(momentDonneStatut.text)
    #             # (print("*"*10))
    #         statutFinal = momentDonneStatut.text

    #             # Tous ces find_next m'ont permis d'aller chercher le texte du statut. Comme chaque balise "a" avait un "onclick" qui portait le nom de l'espèce, j'ai dû me fier à la position de la balise pour ressortir le statut.
    #             # Je ne pouvais me fier au "onlick", car il ne fonctionnait que pour une espèce à la fois. 

                ### TA FAÇON DE FAIRE PEUT FONCTIONNER
                ### JE T'EN PROPOSE UNE AUTRE
                ### TU SAIS QUE TOUS LES TABLEAUX DANS LESQUELS TU VAS ALLER CHERCHER DES DONNÉES ONT LA MÊME STRUCTURE
                ### ET QUE L'INFO QUI T'INTÉRESSE SE TROUVE TOUJOURS DANS LA TROISIÈME LIGNE
                ### TU PEUX DONC DEMANDER TOUS LES TR

                lignesDuTableau = page2.find("table", id="AutoNumber2").find_all("tr")
                # print(lignesDuTableau)

                ### PUIS, PRENDRE LE 3e ÉLÉMENT DE CETTE LISTE

                statut = lignesDuTableau[2].find("a").text.strip()

                ### EN FAIT, IL Y A DEUX INFORMATIONS DANS CE TEXTE: LE STATUT, ET LE MOMENT OÙ CE STATUT A ÉTÉ DÉCLARÉ. ON PEUT DONC FAIRE UN SPLIT POUR LES SÉPARER

                deuxInfos = statut.split(",")

                statutAuQuebec = deuxInfos[0].strip()
                depuisQuand = deuxInfos[1].strip()

                ### C'EST UNE BONNE IDÉE DE RECUEILLIR L'URL DE LA PHOTO DE L'ESPÈCE
                ### TU PEUX Y ARRIVER PLUS SIMPLEMENT AINSI:

                photo = "https://www3.mffp.gouv.qc.ca/faune/especes/menacees/" + page2.find("p", class_ = "credits").find("img")["src"]

    #         images = pages2.find_all("p", class_="credits")
    #         for image in images:
    #             photos = image.find("img")
    #             photo = photos["src"]
    #                 # print("*"*10)
    #                 # print(photo)

    #         infos = [prenomsFinaux, statutFinal, profil, photo]

                infos = [profil, nomEspece, nomLatin, classe.text, statutAuQuebec, depuisQuand, photo]
                print(infos)

            # Je suis allée chercher le fichier de l'image, mais comme il ne s'affiche pas et n'est pas un URL, je ne suis pas certaine que ce soit pertinent.
            # Je vois sur internet qu'il faudrait installer quelque chose dans python pour traiter les images. Je vais m'en tenir qu'au nom de fichier, en imaginant les images! ;-)
            # Il me reste donc à créer mon fichier csv. 

                enfin = open(fichier, "a")
                fini = csv.writer(enfin)
                fini.writerow(infos)

            # J'ai dû laissé tombé la variable "espècesFinales", car elle ne s'associait pas au bon animal. Chaque type d'animal (poissons, mammifères, insectes) s'imprimait
            # une fois pour chaque animal, puis on passait à la 2e qui s'imprimait pour chaque animal...