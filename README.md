# SmartGrid

A repository for SmartGrid group AC/DC

## Aan de slag (Getting Started)
---
### Vereisten (Prerequisites)
Deze code is geschreven in Python3.6.3. In requirements.txt staan alle benodigde packages om de code successvol te draaien.


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
