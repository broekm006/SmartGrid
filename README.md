# SmartGrid

A repository for SmartGrid group AC/DC

## Aan de slag (Getting Started)
### Vereisten (Prerequisites)
Deze code is geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code successvol te draaien.

### Test (Testing)
Om de code te draaien volgens de standaardconfiguratie kunnen de volgende instructies gegeven worden:

```
python main.py

-w: 1,2,3
-a: greedy_output, greedy_distance, greedy_priority, k_means_output, k_means_distance, k_means_priority, HAC
-b: Hill_climber, Simulated_annealing
-i: Iterations (int)
-v: True / False
```

Na het command '-w' kan gekozen worden voor de getallen '1', '2' en '3'. Elk getal staat voor een wijk met een bepaalde startopstelling (zie de uitleg onder de kop "Probleem"). De startopstellingen zijn te vinden in de map SmartGrid/data/Huizen&Batterijen. Na het command '-a' kan gekozen worden voor de woorden 'greedy_output', 'greedy_distance', 'greedy_priority', 'k_means_output', 'k_means_distance', 'k_means_priority' en 'HAC'. Ieder van deze woorden staat voor een bepaald primair algoritme. Na het command '-b' kan gekozen worden voor de woorden 'Hill_climber' en 'Simulated_annealing', welke staan voor een bepaald secundair algoritme. Een uitgebreidere omschrijving van de algoritmes is te vinden in SmartGrid/code/README.md. Na het command '-i' kan het aantal iteraties gekozen worden die het HillClimber algoritme moet gaan maken. Na het command '-v' kan gekozen worden voor 'True' of 'False'. Indien gekozen wordt voor 'True' zal na het draaien van de algoritmes een visualisatie verschijnen van de gekozen wijk, waarop zichtbaar is aan welke batterij de huizen zijn verbonden. Op de visualisatie staat een stip voor een huis en een kruis voor een batterij. Indien een stip een en kruis dezelfde kleur hebben, betekent dit dat beide aan elkaar verbonden zijn.

Voor hulp bij het runnen van het algoritme kan het volgende command gegeven worden:

```
python main.py -h
```

Tijdens het runnen van het algoritme zal in de terminal aangegeven worden als een bepaald algoritme is gestart. Na het runnen van de algoritmes zullen ook de totale kosten verschijnen van de gevonden oplossing.

## Probleem
Groene energie is de energie van de toekomst, en zelf produceren is de mode van nu. Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelfstandig energie mee te produceren. Vaak produceren die installaties zelfs meer energie dan voor eigen consumptie nodig is. Het overschot zou kunnen worden terugverkocht aan een energieleverancier, maar de benodigde infrastructuur is daarvoor veelal niet in woonwijken aanwezig. Om de pieken in consumptie en productie van energie te managen kan daarom het beste een netwerk aangelegd worden, een zogenaamd "SmartGrid". Het SmartGrid is een netwerk van batterijen waarop huizen in een woonwijk met kabels zijn aangesloten, zodat een eventuele overproductie aan energie kan worden opgeslagen. Deze case richt zich op de vraag hoe een dergelijk SmartGrid netwerk zo goedkoop mogelijk kan worden aangelegd.

Voor een feasibility study zijn drie woonwijken (Wijk 1, Wijk 2 en Wijk 3) opgesteld, met in elke wijk vijf batterijen.

### Wat maakt het probleem moeilijk? (Exploration)
Algemeen:  
Het lastige aan deze opdracht is niet zozeer gelegen in het feit dat alle huizen aan een batterij moeten worden verbonden, maar eerder in de optimalisatie van het Smartgrid. Eerder al werd duidelijk dat het Smartgrid zo goedkoop mogelijk moet worden aangelegd. Ieder huis verbinden met een eigen batterij (ter waarde van 5000 euro) is daarom geen realistische optie. In plaats daarvan zal het vanuit kostenoptimalisatie wenselijk zijn om meerdere huizen op een batterij aan te sluiten. Idealiter liggen de huizen die op een batterij zijn aangesloten daarnaast ook in de buurt van die batterij. Het aansluiten van een huis op een batterij gaat namelijk door middel van een kabel die 9 euro per gridsegment kost. Het aantal gridsegementen tussen twee punten dient te worden berekend via de Manhattan Distance.

Vanzelfsprekend hebben de batterijen een limiet voor wat betreft de hoeveelheid engergie die daarin kan worden worden opgeslagen. Wanneer meerdere huizen op een batterij worden aangesloten, is het belangrijk om deze capaciteit in de gaten te houden. De maximale hoeveelheid energie die de huizen kunnen leveren mag de capaciteit van de batterijen namelijk niet overschrijden. Wanneer alle huizen van de woonwijken op vijf batterijen worden aangesloten, bedraagt de nog beschikbare opslagcapaciteit per batterij nog ongeveer 15 ampère. Dat maakt het lastig om de huizen die op batterijen zijn aangesloten om te wisselen of anders te verbinden. Voor het maken van kostenverlagende wisselingen of "swaps", hebben wij enkele algoritmes en heuristieken bedacht.

Naast het optimaliseren van de wijken met vaste posities voor de huizen en batterijen, bestaat ook nog de mogelijkheid de batterijen te verplaatsen. Ook bestaat nog de mogelijkheid om batterijen met verschillende capaciteiten te verwijderen of toe te voegen, waarbij een batterij met een hogere opslagcapaciteit duurder is in de aanschaf. Al deze opties bieden een groot scala aan mogelijkheden om de wijken verder te optimaliseren, en dat is tegelijkertijd ook wat het probleem moeilijk maakt. Juist omdat zoveel keuzes gemaakt kunnen worden, is het lastig om te bepalen welke combinatie van keuzes uiteindelijk de meeste kostenbesparing oplevert. Anders dan bij het verdelen van huizen over batterijen, is het lastig om voor dit probleem algoritmes en heuristieken te bedenken omdat met zoveel factoren rekening gehouden moet worden. Het uiteindelijke aantal verschillende mogelijkheden is dan ook bijzonder groot. In het bijzonder is het daarom moeilijk om te bepalen hoe een gevonden oplossing zich verhoudt tot de meest efficient mogelijke oplossing. Een manier om de kwaliteit van een oplossing te beoordelen is om de kosten van die oplossing te vergelijken met de laagst mogelijk kosten voor een bepaalde batterijopstelling (lowerbound). Later meer over het aantal mogelijkheden van dit probleem en de lowerbound.

Specifieke problemen per wijk:  
In wijk 1 zijn de batterijen in eerste instantie erg ongelijkmatig verdeeld over het SmartGrid. Zo staan er vier batterijen op minimale afstand van elkaar, waardoor voor het aansluiten van huizen op de batterijen altijd een grote hoeveelheid aan kabels nodig is. Daarnaast kan bij deze wijk het verschil tussen de maximale hoeveelheid energie die huizen kunnen leveren oplopen tot 50 ampère. Zo levert het huis met de kleinste output maximaal 26,20 ampère aan het SmartGrid, terwijl het huis met de grootste maximale output wel 76,15 ampère. Doordat de maximale output zo sterk varieert, is het wisselen van huizen tussen batterijen bij wijk 1 extra lastig. De kans is dan namelijk groot dat bij een wisselpoging de capaciteit van één van de twee baterijen zal worden overschreden.

In wijk 2 ligt de maximale hoeveel output van ieder huis veel dichter bij elkaar dan het geval is bij wijk 1. Zo levert het huis met de kleinste maximale output 35,44 ampère aan het SmartGrid en het huis met de grootste maximale output 64,79 ampère. Hierdoor kunnen de huizen makkelijker aan elkaar verbonden worden dan bij wijk 1 het geval is en kunnen er daarna relatief makkelijk kostenbesparende wisselingen worden gemaakt.

In wijk 3 verschillen de outputs van de huizen gemiddeld tien ampère van elkaar. Zo levert het huis met de kleinste maximale output 45,17 ampère aan het SmartGrid en het huis met de grootste maximale output 64,79 ampère.
Het is daardoor makkelijker om huizen te wisselen, maar dit zal in veel gevallen te weinig capaciteit bij de batterij vrijmaken om een eventueel overbleven huis alsnog aan die batterij te verbinden. Daardoor kan het in sommige gevallen lang duren tot een swap gevonden die het gewenste resultaat oplevert.

### StateSpace
Eerder werd al duidelijk dat de grote hoeveelheid aan mogelijkheden één van de aspecten is die de SmartGrid case lastig maakt. Maar hoeveel verschillende mogelijkheden of 'toestanden' zijn er nou eigenlijk? Die vraag is een vraag naar de toestandsruimte van het probleem, ook wel "StateSpace" genoemd. De StateSpace bestaat uit de ruimte tussen een upperbound (bovengrens) en een lowerbound (ondergrens). Door zowel de upperbound als de lowerbound te berekenen, kan men daarom achter de StateSpace van een probleem komen.

Upperbound mogelijkheden:
Het maximaal aantal mogelijke manieren om de huizen aan te sluiten op de batterijen in de standaardsituatie met vijf batterijen, kan als volgt berekend worden:

```
               150!
               ---
(30! * 30! * 30! * 30! * 30! * 5!)
```

De teller van de formule is 150! omdat de huizen op 150 * 149 * 148... * n manieren kunnen worden gesorteerd alvorens deze aangesloten worden op de verschillende batterijen. De batterijen hebben in de standdaardsituatie een maximumcapaciteit van 1507 ampère en de huizen hebben gemiddeld een maximale output van 50 ampère. Uitgaande van deze gemiddeldes kunnen daarom 30 huizen op één batterij aangesloten worden, hetgeen per batterij op 30! verschillende manieren kan. De noemer is daarom 30! * 30! * 30! * 30! * 30!. Tenslotte moet de noemer nog eens vermenigvuldigd worden met 5!, omdat de volgorde van de baterijen niet uitmaakt. De upperbound voor het aantal mogelijkheden komt dan totaal in de buurt van de 1,57572 * 10^164. Het valt te betwijfelen of het wel correct is om het gemiddelde aantal huizen per batterij als uitgangspunt te nemen bij het berekenen van de upperbound. Het aantal huizen per batterij kan namelijk wat afwijken, met name als het verschil in maximale output tussen verschillende huizen groter is. Een alternatief zou kunnen zijn om bij het bereken van het aantal mogelijkheden het huis met de kleinste maximale uitput als uitgangspunt te nemen. Voor wijk 1 zou het gevolg dan zijn dat maximaal 57 huizen aangesloten kunnen worden op iedere batterij. Wanneer bij het vaststellen van de noemer uitgegaan zou worden van vijf batterijen met ieder maximaal 57 batterijen, overschrijdt het totaal aantal huizen in de noemer (5 * 57 = 285) het werkelijke aantal huizen (150). Ook dit alternatief levert daarom een vreemde situatie op. Ons inziens is het berekenen van de upperbound van het aantal mogelijkheden met name relevant om een indruk te krijgen van de enorme hoeveelheid aan mogelijkheden die bestaan voor onze case. Voor het meten van de resultaten zijn met name de upperbound en lowerbound van de kosten voor de aanleg van het SmartGrid relevant. Beiden zullen in het vervolg met meer precisie worden uitgewerkt.

Upperbound kosten:
Om de batterijen aan te sluiten op de huizen moeten in de standdaardsituatie met vijf batterijen maximaal de volgende kosten gemaakt worden:

```
5 * €5000 batterij + 150 * 9 * (afstand tussen huis en verste batterij)
```

Zoals gezegd kosten de batterijen ieder 5000 euro in aanschaf, en kost een kabel 9 euro per grid segment. Voor de aanschaf van de batterijen bedragen de vaste kosten daarom in ieder geval 25000 euro. Voor het berekenen van de maximaal mogelijke kabelkosten wordt voor ieder huis gekeken wat de verste batterij is, en op basis van die afstand (Manhattan distance) worden de kabelkosten berekend. De resultaten van deze berekening zijn te vinden in de onderstaande tabel.

Lowerbound kosten:
Om de batterijen aan te sluiten op de huizen moeten in de standdaardsituatie met vijf batterijen maximaal de volgende kosten gemaakt worden:

```
5 * €5000 batterij + 150 * (afstand tussen huis en dichtbijzijnde batterij)
```

De vaste kosten bedragen bij het berekenen van de lowerbound vanzelfsprekend ook 5000. Voor het berekenen van de minimaal mogelijke kabelkosten wordt voor ieder huis gekeken wat de dichtbijzijnde batterij is, en op basis van die afstand (Manhattan distance) worden de kabelkosten berekend. De resulaten van deze berekening zijn te vinden in de onderstaande tabel.

Wijk | Lowerbound | upperbound
-----|------------|-----------
1|53188|103030
2|45268|96253
3|42757|101491

##### Opmerking omtrent de StateSpace na het verplaatsen van batterijen
Inherent aan de methode die gekozen is om de Upperbound en Lowerbound te berekenen, is dat de StateSpace wijzigt nadat één of meer batterijen verplaatst zijn. Na het verplaatsen van de batterijen is het namelijk mogelijk dat de kortste of langste afstand tussen een huis en een batterij anders is dan voorheen. Bij enkele oplossingen die zijn gevonden met het Hierarchical Agglomerative Clustering algoritme, zijn de totale kosten voor aanleg van het SmartGrid gelijk aan de lowerbound. Alle huizen zijn dan verbonden aan de meest dichtsbijzijnde batterij. Wel is het mogelijk dat bij een andere batterij-opstelling een lagere lowerbound geldt.

### Structuur Repository
Alle python scripts staan in de folder Code. In de map Code is onderscheid gemaakt tussen algoritmes, classes en algemene code. In de map data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

## Auteurs (Authors)
* Anne Hoogerduijn Strating
* Marc van den Broek
* Thomas Franx

## Dankwoord (Acknowledgments)
* Quinten van der Post
* StackOverflow
* Koffie

---
### logboek
**7-11-2018:**
De huizen gesorteerd van groot naar klein, vervolgens over de huizen heen gelopen
en steeds de batterij gekozen die het meest dichtbij is. Werkt voor wijk1 en wijk 3,
bij wijk2 blijft een huis over. Opgeslagen als main.

**14-11-2018:**
Poging gedaan om vanuit de batterijen de meest dichtbije huizen te verbinden totdat batterij vol is. Vervolgens door met de volgende batterij. Werkt voor wijk 2, maar bij
wijk1 en wijk3 blijft een huis over. Opgeslagen als branch test.

**15-11-2018:**
Huizen gesorteerd op basis van prioriteit. Bij alle wijken blijft één huis over maar de kabel kosten zijn lager dan bij de andere twee. Daarnaast zijn de 3 sorteer methodes in één class gezet (sort.py), en is het greedy algoritme, dat gebruikt wordt om een eerste oplossing te formuleren, in een aparte class gezet (greedy.py). In de helper class staat voor nu alleen de kosten-functie.

**21-11-2018**
Gredy uitgebreid met een swap (hill cliber) functie waardoor deze altijd een valide oplossing kan vinden. Daarnaast
