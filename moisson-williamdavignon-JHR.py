# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

### BRAVO! SCRIPT DANS LEQUEL L'EFFORT EST MANIFESTE! AVEC UN 2E SCRIPT POUR PERMETTRE AU PUBLIC DE CONNAÎTRE LE SIGNE DE LEURS DÉPUTÉ(E)S! BRAVO, MÊME SI L'INTÉRÊT PUBLIC AVOISINE ZÉRO :) !

# but 1: obtenir liste des noms de députés

#le csv est la liste produite
#input2.py permet de naviguer le csv. Pour des raisons de conflits entre l'encondage du .csv et des accents français (je crois), vous ne pouvez pas entrer de nom complets si le nom contient des accents. Par exemple, "Manon" va donner un résultat, mais "Manon Massé" non.

entetes = {
    "User-Agent":"William d'Avignon, étudiant en journalisme UQAM. Contact: w**.d**@**.**"
}

url = "http://assnat.qc.ca/fr/deputes/index.html"

fichier = "signe-JHR.csv"

# nb = list(range(1, 126))   <-- pas important finalement

#Url de base
site = requests.get(url, headers=entetes)
page = BeautifulSoup(site.text, "html.parser")

noms = page.find_all("a", class_="depute")
test = page.find("div")
urlprefix = "http://www.assnat.qc.ca"
urls = []

for url in page.find_all('a'):
    if "html" in str(url.get("href")):
        urlFull = (urlprefix + url.get("href"))
        urlFullStrip = urlFull
        urls.append(urlFull)
        # print(urlFullStrip, sep='\n')
print("*"*20)
# print(urls)
# print(type(urls))

# date de naissance
#ex: 'http://www.assnat.qc.ca/fr/deputes/boutin-joelle-18561/index.html
n= 0
x = 0
for dep in urls:
    if "deputes" in dep:
        n += 1
        if n >21:                   #  <-- les 21 premières adresses ne concernent pas des députés
            x += 1
            bio = dep.replace("index", "biographie")
            print(x, bio)
            # BeautifulSoup(site.text, "html.parser")
            urldep = requests.get(bio, headers=entetes)
            depu = BeautifulSoup(urldep.text, "html.parser")
            text = depu.find("div", class_="colonneImbriquee imbGauche")
            fete = text.find("p")
            h1 = depu.find_all("h1")
            h1strip = str(h1[1])                            # <-- modification du nom pour rendre le CSV visuellement plaisant
            displayn = h1strip.replace("<h1>", "")
            displayna = displayn.replace('<span class="nomDepute">', "")
            displayname = displayna.replace("</span></h1>", "")
            print(displayname)
            
            nom0 = bio.rsplit('/')[-2]
            nom1 = nom0.rsplit("-")
            nom2 = nom1[1] + (" ") + nom1[0]

            print(nom0)
            print(nom1)
            print(nom2)

            urlEtFete = [bio]
            urlEtFete.append(fete)
            urlEtFete.append(nom2)
            nomEtFete = [nom2]
            # nomEtFete.append(fete)            Les variables créées dans ce bloc ne sont plus tant pertinentes
            
            print(fete)
            if "19" in str(fete):         #Certaines biographiques de députés n'ont pas de dates de naissances. Assumant que tout les députés sont nés avant 2000, ce test s'assure que le str 19xx soit contenu dans leur bio

            #     dead = open(fichier, "a")# <-- csv test
            #     obies = csv.writer(dead)
            #     obies.writerow(nomEtFete)
            #     print("good")
            # else:
            #     dead = open(fichier, "a")
            #     obies = csv.writer(dead)
            #     obies.writerow(["No data"])
            #     print("no")

                stats = str(fete)
                # print(type(fete))     ##test
                #probleme quand 1er du mois V
                if "<sup>" in stats:
                    sup1 = stats.find("<sup>")
                    sup2 = stats.find("</sup>")
                    # print(sup1)
                    # print(sup2)
                    stats = stats[0:sup1] + stats[sup2 + 6::]
                print(stats)

                ###Vérifier si la date est donnée, pas just le mois ( Saul Polo (Sa bio dit simplement "né en juin" impossibilité de donner le signe astrologique)
                ls = list(range(1,32))
                jours = []
                check = 0
                for nb in ls:
                    nb = (" " + str(nb) + " ")
                    jours.append(nb)
                    # print(n)
                    if nb in stats:
                        check += 1
                
                print(jours)
                if check > 0:       #relié au dernier commentaire
                    if "p;" in stats:
                        stats = stats.replace("p;"," ") 
                    if "\xa0" in stats:
                        stats = stats.replace("\xa0", " ")  #certains lorsque "le" est précédé d'un char au lieu d'un " " problème avec Unicode
                    print(stats)
                    short = (stats.split(" le "))
                    print(short)
                    short2 = short[1]
                    nb19 = short2.count("19")
                    pos = (short2.rfind("19"))
                    print(short2)
                    print(pos)
                    oppos = str("-"+str(pos))
                    opposch = int(oppos)
                    print(oppos)
                    print(opposch)
                    annee = short2[pos:pos + 4]

                    #trouver jour
                    # posle = short2.find("le")   <-- plus nécéssaire
                    date1 = short2[0]
                    date2 = short2[1]
                    date = (date1 + date2).strip()
                    print(date)

                    #trouver mois               Remplace le str du mois par un int()
                    if "janvier" in short2:
                        mois = 1
                    if "février" in short2:
                        mois = 2
                    if "mars" in short2:
                        mois =3
                    if "avril" in short2:
                        mois = 4
                    if "mai" in short2:
                        mois = 5
                    if "juin" in short2:
                        mois = 6
                    if "juillet" in short2:
                        mois = 7
                    if "août" in short2:
                        mois = 8
                    if "aout" in short2:
                        mois = 8
                    if "septembre" in short2:
                        mois = 9
                    if "octobre" in short2:
                        mois = 10
                    if "novembre" in short2:
                        mois = 11
                    if "décembre" in short2:
                        mois = 12

                    #rajouter un zéro si simple chiffre   pour améliorer la lisibilité
                    if len(str(mois)) == 1:
                        moisZ = ("0"+ str(mois))
                    else:
                        moisZ = str(mois)
                    print(annee, type(annee))
                    print(mois, type(mois))
                    print(date, type(date))
                    datefull = (annee + "-" + moisZ + "-" + date)
                    print(datefull)

                    ## trouver SIGNE ##

                    # Aries.svg	♈	Aries	March 21 – April 20	Mars	Mars
                    # Taurus.svg	♉	Taurus	April 21 – May 21	Venus with Earth	Venus
                    # Gemini.svg	♊	Gemini	May 22 – June 21	Mercury	Mercury
                    # Cancer.svg	♋	Cancer	June 22 – July 22	Moon	Moon
                    # Leo.svg	♌	Leo	July 23 – August 22	Sun	Sun
                    # Virgo.svg	♍	Virgo	August 23 – September 23	Mercury	Earth
                    # Libra.svg	♎	Libra	September 24 – October 23	Venus	Venus
                    # Scorpio.svg	♏	Scorpio	October 24 – November 22	Pluto	Mars
                    # Sagittarius.svg	♐	Sagittarius	November 23 – December 21	Jupiter	Jupiter
                    # Capricorn.svg	♑	Capricorn	December 22 – January 20	Saturn	Saturn
                    # Aquarius.svg	♒	Aquarius	January 21 – February 19	Uranus	Saturn
                    # Pisces.svg	♓	Pisces	February 20 – March 20	Neptune	Jupiter

                    date = int(date)
                    print(int(date))

                    #trouver le signe astrologique

                    #Bélier
                    if mois == 3 and int(date) > 20 or mois == 4 and int(date) < 19:
                        signe = "Bélier"
                    #Taureau
                    if mois == 4 and int(date) > 20 or mois == 5 and int(date) < 22:
                        signe = "Taureau"
                    #Gemeau
                    if mois == 5 and int(date) > 21 or mois == 6 and int(date) < 22:
                        signe = "Gémeau"
                    #Cancer
                    if mois == 6 and int(date) > 21 or mois == 7 and int(date) < 23:
                        signe = "Cancer"
                    #Lion
                    if mois == 7 and int(date) > 22 or mois == 8 and int(date) < 23:
                        signe = "Lion"
                    #Vierge
                    if mois == 8 and int(date) > 22 or mois == 9 and int(date) < 24:
                        signe = "Vierge"
                    #Balance
                    if mois == 9 and int(date) > 22 or mois == 10 and int(date) < 24:
                        signe = "Balance" 
                    #Scorpion
                    if mois == 10 and int(date) > 23 or mois == 11 and int(date) < 23:
                        signe = "Scorpion" 
                    #Sagittaire
                    if mois == 11 and int(date) > 22 or mois == 12 and int(date) < 22:
                        signe = "Balance"
                    #Capricorn
                    if mois == 12 and int(date) > 21 or mois == 1 and int(date) < 21:
                        signe = "Capricorne" 
                    #Verseau
                    if mois == 1 and date > 20 or mois == 2 and date < 20:
                        signe = "Verseau"
                    #Poisson
                    if mois == 2 and date > 19 or mois == 3 and date < 21:
                        signe = "Poisson"

                        #création du .csv
                    print(signe)
                    # print(signe)
                    row = []
                    row.append(displayname)
                    row.append(datefull) ### J'ajoute la date de naissance, si elle est connue
                    row.append(signe)
                    dead = open(fichier, "a")
                    obies = csv.writer(dead)
                    obies.writerow(row)
                    print("good")

                        # bio2 = bio.get("div", class_="colonneImbriquee imbGauche")
                        # print(bio2)
                        #en cas d'erreur, VV on ajoute le nom du dep et "NoData" dans le csv
                else:
                    row = []
                    row.append(displayname)
                    row.append("Inconnue")
                    # row.append("No data") ### EN FRANÇAIS S'IL VOUS PLAÎT
                    row.append("Inconnu")
                    dead = open(fichier, "a")
                    obies = csv.writer(dead)
                    obies.writerow(row)
                    # print("No data") ### EN FRANÇAIS S'IL VOUS PLAÎT
                    print("Inconnu")
            else:
                row = []
                row.append(displayname)
                row.append("Inconnue")
                # row.append("No data")
                row.append("Inconnu")
                dead = open(fichier, "a")
                obies = csv.writer(dead)
                obies.writerow(row)
                # print("No data")
                print("Inconnu")

