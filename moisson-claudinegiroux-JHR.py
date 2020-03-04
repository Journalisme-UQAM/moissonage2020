#coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

url = "https://www.pbo-dpb.gc.ca/fr/blog/news/archive"

fichier ="rapportFinal-JHR.csv"
# rapportFinal=[] ### CETTE VARIABLE VA ÊTRE UTILE, MAIS SEULEMENT À L'INTÉRIEUR DES BOUCLES CI-DESSOUS
#J'ai tenté d'aller chercher les rapports sur le site du Directeur parlementaire du budget

### EXCELLENTE IDÉE! MAIS ENTRAVÉE PAR PLUSIEURS PROBLÈMES.

entetes ={
    "User-Agent": "Claudine Giroux, étudiante en journalisme"
    }

# annee = list(range(2012,2021)) ### SUPER!
annees = list(range(2012,2021)) ### VAS-Y AVEC UN NOM DE VARIABLE AU PLURIEL
# rapportFinal.append(annee) ### IL N'EST PAS UTILE D'AJOUTER LE CONTENU DE TA LISTE "ANNEES" À "RAPPORTFINAL"

# mois= list(range(1,13))
lesMois= list(range(1,13)) ### AUTRE FAÇON DE DISTINGUER "MOIS" AU PLURIEL
# rapportFinal.append(mois)
#J'ai créé des listes de range pour le mois et l'année. Les archives débutent en 2012, j'ai donc débuté ma recherche en 2012

n=0

# for date in annee: ### EXCELLENTE PREMIÈRE BOUCLE
for annee in annees: ### QUE JE REBAPTISE AVEC MES VARIABLES
    # date= str(date)

    # for dates in mois:
    for mois in lesMois:
        if mois < 10:
            mois = "0" + str(mois)
        # urlDuJour= url+ str(date) +"/"+str(dates)
        urlDuMois = "{}/{}/{}".format(url, str(annee), str(mois)) ### JE DONNE JUSTE UN NOM DE VARIABLE QUI CORRESPOND DAVANTAGE À CE QU'ON FAIT: AU DPB, IL Y A UNE PAGE D'ARCHIVES PAR MOIS
        print(urlDuMois) ### PETIT TEST -- CONCLUANT

        site = requests.get(urlDuMois, headers=entetes)
        # print(site.status_code)

        page = BeautifulSoup(site.text, "html.parser")

        # #J'ai réussi à imprimer chacune des url des archives

        # # print(page)

        # rapports= page.find_all("h2", class_="post-title") ### CHOISIS PLUTÔT L'ÉLÉMENT QUI REGROUPE LE PLUS D'INFORMATIONS QUI T'INTÉRESSENT
        rapports = page.find_all("div", class_="r")
        # #Je veux imprimer chacune des url qui se trouve dans la section d'un mois et d'une année spécifique

        for rapport in rapports:

            n += 1 ### J'AI VU QUE TU AVAIS INITIALISÉ UNE VARIABLE "N" À ZÉRO, UN PEU PLUS HAUT; IL FAUT S'EN SERVIR :)

            rapportFinal = [] ### C'EST ICI QU'ON PEUT INITIALISER NOTRE LISTE "RAPPORTFINAL"

            ### ON VA TOUT DE SUITE Y CONSIGNER QUELQUES INFORMATIONS FONDAMENTALES POUR NOUS AIDER À REPRENDRE NOTRE MOISSONNAGE SI NOTRE SCRIPT PLANTE

            rapportFinal.append(n)
            rapportFinal.append(mois)
            rapportFinal.append(annee)

            urlRapp = rapport.find("a")["href"]
        #     #j'ai réussi à imprimer les url. Je veux ensuite imprimer la date de la publication du rapport, le résumé et ses auteurs
            rapportFinal.append(urlRapp)

            date = rapport.find("div", class_="date").text.strip()
            # print(date)
            rapportFinal.append(date)

            extrait = rapport.find("div", class_="post-abstract").text.strip()
            # print(extrait)
            ### DANS LES EXTRAITS, ON VEUT RETRANCHER CERTAINS CARACTÈRES SPÉCIAUX QUI NUISENT À L'ÉCRITURE DANS NOTRE CSV
            extrait = extrait.replace("\n"," ").replace("\xa0"," ").replace("  "," ").strip()
            rapportFinal.append(extrait)

            auteur=rapport.find("div", class_="author").text.strip()
            ### DANS LES NOMS D'AUTEURS, ON VEUT RETRANCHER UN CARACTÈRE SPÉCIAL QUI FAIT UN SAUT DE LIGNE DANS NOTRE CSV...
            auteur = auteur.replace("\n", " ")
            ### DANS LES NOMS D'AUTEURS, ON VEUT AUSSI RETRANCHER LE "PUBLIÉ PAR"
            auteur = auteur.replace("Publié par:","").strip()
        #     print(auteur)
        #     print()
            rapportFinal.append(auteur)

        #     #J'ai réussi à imprimer toutes les informations voulues, il me reste seulement à créer un fichier csv
            print(rapportFinal) ### TESTOUNET
            print("-|"*10)

            dead= open(fichier,"a")
            obies=csv.writer(dead)
            obies.writerow(rapportFinal)
