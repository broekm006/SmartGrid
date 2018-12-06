# SmartGrid

A repository for SmartGrid group AC/DC

## Aan de slag (Getting Started)
### Vereisten (Prerequisites)
Deze code is geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code successvol te draaien.

## Probleem
Groene energie is de energie van de toekomst, en zelf produceren is de mode van nu. Veel huizen hebben tegenwoordig zonnepanelen, windmolens of andere installaties om zelf energie mee te produceren. Fortuinlijk genoeg produceren die installaties vaak meer dan voor eigen consumptie nodig is. Het overschot zou kunnen worden terugverkocht aan de leverancier, maar de infrastructuur is daar veelal niet op berekend. Om de pieken in consumptie en produktie te kunnen managen moeten er batterijen geplaatst worden.

Voor een feasibility study zijn drie woonwijken opgesteld, met daarin vijf batterijen.

### Wat maakt het probleem moeilijk
Algemeen:  
Het lastige aan deze opdracht is niet dat alle huizen aan een batterij meten worden verbonden. Dat op zichzelf is prima te doen, maar het zo optimaal mogelijk verbinden legt een hoge lat. Zeker omdat, de batterijen een limiet hebben waardoor in totaal de speling per batterij op ongeveer 15 ampere neer komt. Hiermee blijft weinig tot geen speling om huizen te verwisselen of anders te verbinden. Daarnaast kost het tijd om de verschillende algoritmes die hiervoor nodig zijn te leren en uit te schrijven. Daarbij behoud zich altijd het probleem dat de beste manier ook bewezen moet worden als de beste oplossing.

Per wijk:  
Voor wijk 1 staan de batterijen erg slecht gepositioneerd. Zo staan er 4 op minimale afstand van elkaar waardoor indelen van huizen altijd veel extra kabel kosten. Daarnaast is het wisselen van huizen en batterij lastig door de verschillende grote van de huizen. De ampere van de huizen kan oplopen tot een verschil van ~50,

Voor wijk 2 ligt de ampere per huis veel dichter bij elkaar dan die van wijk 1. Hierdoor is het moeilijker huizen heen en weer te verplaatsen om ruimte vrij te maken.

Voor wijk 3 ligt de ampere per huis op ~5 verschil van elkaar af. Hierdoor is indelen beter te doen en kan er gemakkelijker worden gewisselt.

Constraint gevoelig:  
Daarnaast kunnnen de batterijen in onze constraints ook nog een andere capaciteit krijgen en een ongelimiteerd aantal. Hiermee wordt het probleem weer een stuk gecompliceerder doordat hiervoor een optimale positie en aantal moet worden gevonden zonder de kosten verder op te voeren.

### Structuur
Alle python scripts staan in de folder Code. In de map Code is onderscheid gemaakt tussen algoritmes, classes en algemene code. In de map data zitten alle input waardes en in de map resultaten worden alle resultaten opgeslagen door de code.

### Test (Testing)
Om de code te draaien met de standaard configuratie gebruik de instructie:

```
python main.py
```

## Auteurs (Authors)
* Anne Hoogerduijn Strating
* Marc van den Broek
* Thomas Franx

## Dankwoord (Acknowledgments)
* StackOverflow
* Koffie

---
### eventueel logboek
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
