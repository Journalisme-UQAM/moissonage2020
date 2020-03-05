# moissonage2020
Quelques exemples des scripts de moissonnage (_scraping_) de données réalisés par les étudiant(e)s de la session d'hiver 2020.

-----

### Amélie Brissette
Amélie a moissonné tous les articles publiés par le quotidien [_La Presse_ en janvier 2020](https://www.lapresse.ca/archives/2020.php).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-amebrissette-JHR.py)

### Clémence Bouquerod
Clémence s'intéresse aux articles sur les féminicides publiés dans [_Le Monde_ en novembre 2019](https://www.lemonde.fr/recherche/?search_keywords=f%C3%A9minicide&start_at=01/11/2019&end_at=01/12/2019&search_sort=date_desc&page=1).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-clemyaaa-JHR.py)

### Catherine Savoie
Après avoir remarqué que les URL des articles de l'hebdo de sa région, [_L'Œil régional_](https://www.oeilregional.com), possédaient tous un numéro unique, Catherine a voulu voir ce qu'elle recueillerait si elle testait une étendue de ces numéros.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-catherinesavoie-JHR.py)

### Charles Mathieu
Charles s'est servi de l'[API de CanLII](https://github.com/canlii/API_documentation/blob/master/FR.md) pour recueillir des informations sur tous les jugements relatifs aux assurances rendus par tous les tribunaux du Québec depuis le début de l'année 2019.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-charlesmathieu19-JHR.py)

### Ariane Chevrier
Ariane recueille des infos sur [les espèces menacées et vulnérables au Québec](https://mffp.gouv.qc.ca/la-faune/especes/liste-especes-vulnerables/).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-chearie-JHR.py)
   
### Claudine Giroux
Claudine moissonne tous les [rapports du Directeur parlementaire du budget](https://www.pbo-dpb.gc.ca/fr/blog/news) (à Ottawa) depuis 2012.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-claudinegiroux-JHR.py)
   
### François-Alexis Favreau
Saviez-vous que le site [*Actualités UQAM*](https://www.actualites.uqam.ca/) contenait plus de 8500 articles? François-Alexis a recueilli des infos de base sur chacun d'entre eux.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-CPTNPatenaude-JHR.py)
   
### Éliane Gosselin
Éliane s'intéresse elle aussi aux articles du *Monde*, mais pour [le mois de janvier 2020](https://www.lemonde.fr/archives-du-monde/01-01-2020/) seulement. Il y en a quand même plus de 3&nbsp;000!<br>
   :point_right::point_right::point_right: [**Son script**](moisson-ElianeGo-JHR.py)
   
### Félix Desjardins
Il n'était pas interdit aux étudiant(e)s de choisir des sites commerciaux pour faire leur exercice de moissonnage. Ce fut le cas de Félix qui, pour des raisons qui lui appartiennent, a recueilli des informations à propos d'[articles de mariage sur le site de Dollarama](https://www.dollarama.com/fr-CA/activite/evenements-fetes-et-organisation-de-mariages).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-flixgardener-JHR.py)

### David Massé
David est allé chercher tous les [procès-verbaux de la municipalité de Saint-Léon-le-Grand](https://municipalite.saint-leon-le-grand.qc.ca/documents/proces-verbaux.html) pour l'année 2019. J'ai ajouté à son script des fonctionnalités pour extraire le texte des fichiers PDF des procès verbaux à l'aide du module [Tika](https://github.com/chrismattmann/tika-python).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-MacNFox-JHR.py)

### Jessica Potsou
Amatrice de sport, Jessica a moissonné les plus de 500 [articles que *La Presse* a consacrés à sa couverture des Jeux Olympiques d'hiver de 2010](https://www.lapresse.ca/sports/vancouver-2010/). *#nostalgie*<br>
   :point_right::point_right::point_right: [**Son script**](moisson-MadSkater-JHR.py)

### Maude Faucher
De son côté, Maude a recueilli des infos sur toutes les [recettes végétariennes de Ricardo](https://www.ricardocuisine.com/recettes/plats-principaux/vegetarien).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-maudefaucher-JHR.py)
   
### Mayssa Ferah
Maïssa s'intéresse elle aussi à des recettes, mais à toutes celles proposées par le [service de livraison GoodFood](https://www.makegoodfood.ca/fr/recipes/1). Le CSV qu'elle produit donne la liste de tous les ingrédients utilisés dans les recettes qu'on peut retrouver dans les 200 premières pages du site (près de 32&nbsp;000 ingrédients!).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-msferah-JHR.py)

### Nicholas Pereira
Nicholas a remarqué que les articles du [site de RDS](https://www.rds.ca/) étaient tous suivis d'un numéro. Par exemple, cet article ([https://www.rds.ca/soccer/europe/ligue-des-champions/ligue-des-champions-barcelone-sauve-par-griezmann-a-naples-gnabry-brille-encore-a-londres-1.7256225](https://www.rds.ca/soccer/europe/ligue-des-champions/ligue-des-champions-barcelone-sauve-par-griezmann-a-naples-gnabry-brille-encore-a-londres-1.7256225)) se termine avec le numéro **1.7256225**. Nicholas s'est demandé ce qui se passerait s'il réduisait l'URL au numéro ([https://www.rds.ca/1.7256225](https://www.rds.ca/1.7256225)). Eh bien ça fonctionne! Il a donc testé un intervalle pour voir ce qu'il obtiendrait. Avec un intervalle de 100 nombres, il a recueilli trois articles. Avec 1000, il en obtient douze.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-nickpereira-JHR.py)

### Félix Pedneault
Félix s'est intéressé aux archives de [la section tech du magazine en ligne *The Verge*](https://www.theverge.com/tech/archives/).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-Pedno-JHR.py)

### Sandrine Vieira
C'est aux [338 député(e)s siégeant à la Chambre des communes](https://www.noscommunes.ca/Members/fr/recherche) que Sandrine s'est intéressée.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-sandrinevieira-JHR.py)

### Simon Duclos
Pour sa part, Simon est allé chercher [tous les articles relatifs à la NBA publiés sur le site web d'ESPN en février 2019](http://www.espn.com/nba/news/archive/_/month/february/year/2019).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-SimonDuclos-JHR.py)
   
### William d'Avignon
C'est un exercice de moissonnage et tous les sujets étaient permis. William a conçu un script qui moissonne la [liste des député(e)s de l'Assemblée nationale](http://www.assnat.qc.ca/fr/deputes/index.html). Lorsque la date de naissance d'un(e) élu(e) est disponible, le script détermine son signe astrologique. Un second script vous permet de demander le signe astrologique de votre député. Comme je l'ai indiqué dans les commentaires&nbsp;: intérêt public zéro, mais effort excellent.<br>
   :point_right::point_right::point_right: [**Son script principal**](moisson-williamdavignon-JHR.py), et son [**second**](input2-JHR.py)
   
### Lina Heckenast
Costaud travail de la part de Lina! Elle a écrit un script qui peut théoriquement recueillir des infos sur [tous les utilisateurs de SoundCloud](https://soundcloud.com/people/directory/)! Je dis *théoriquement*, car les utilisateurs de cette plateforme se comptent par millions. Juste ceux dont le pseudonyme commence par «&nbsp;A&nbsp;» sont 2&nbsp;144&nbsp;989!!! Faire rouler son script prendrait des jours, sans compter que SoundCloud nous débranche régulièrement. Mais tout est complet.<br>
   :point_right::point_right::point_right: [**Son script**](moisson-linaheckenast-JHR.py)

### Alexandra Lauzon
Alexandra s'est elle aussi attaquée au site de [Ricardo](https://www.ricardocuisine.com), mais pour en extraire TOUTES les quelque 7&nbsp;000 recettes (seulement les URL).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-alexandralauzon-JHR.py)

### Éloi Fournier
Éloi s'intéresse aux [vols pas chers offerts par Air Transat](https://www.airtransat.com/fr-CA/vols-pas-chers-du-canada?ici=footerlink&icn=cheap-flights_french).<br>
   :point_right::point_right::point_right: [**Son script**](moisson-eloifournier-JHR.py)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Journalisme-UQAM/moissonage2020/master)
