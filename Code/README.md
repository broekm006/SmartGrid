# code

In deze map is de code te vinden waarmee ons probleem oplossen. In de map alogritmes is het algoritme opgeslagen in de map classes de verschillende classes.

## Verschillende algoritmes
### Greedy
Dit algoritme pakt de op het moment beste keuze en koppelt zo alle huizen aan een batterij. Dit algoritme zoals wij deze gebruiken kent 3 varianten "output", "distance" & "priority".

- In output wordt het greedy algoritme gebruikt op basis van de opgeslagen ampere van elk huis. De huizen worden op grootte gesoorteerd en daarna aan de dichtsbijzijnde batterij gekoppeld.

- In distance wordt het greedy algoritme gebruikt op basis van de afstand tussen elk huis en de dichtsbijzijnde batterij. Deze worden ingedeel op de korste afstand en daarna aan de batterij verbonden.

- In priority wordt het greedy algoritme gebruikt op basis van een prioriteits waarde. Deze waarde wordt bepaald op basis van de afstand tot een batterij en de hoeveelheid opgeslagen ampere.

### Swap
Dit algoritme is een uitbreiding op de greedy oplossing. Deze kijkt naar de oplossing zoals deze is gegenereerd in greedy en zoekt naar overgebleven huizen. Wanneer één of meerdere huizen niet zijn ingedeeld wordt een van onze swap functies aangeroepen: Brute Force of Hill Climber

- In Brute Force worden de laatste x aantal huizen terug gehaald van de batterijen en daarna worden deze opnieuw ingedeeld om te kijken of zo plek onstaat voor de overige huizen.

- In Hill Climber worden twee batterijen gekozen. De gene met de hoogste usage en met de laagste usage. Binnen deze twee worden twee huizen (willekeurig) gewisselt om zo ruimte vrij te maken voor de overige huizen.

### Hill Climber
Dit algoritme kijkt naar een bestaande oplossing. Deze zoekt twee willekeurige batterijen met daarin twee willekeurige huizen. Het algoritme probeert daarna deze te wisselen met elkaar. Als de afstand tussen de huizen en batterijen hier beter op word dan wordt de wissel doorgezet. Mocht dit niet beter worden dan wordt de wissel geannuleerd.

### Simulated Annealing
Dit algoritme kijkt naar een bestaande oplossing. Deze zoekt twee willekeurige batterijen met daarin twee willekeurige huizen. Daarna kijkt deze naar de distance en bepaald op basis van temperatuur of deze wisseling mag worden uitgevoerd. Hierbij kan het resultaat eerst slechter worden voor het weer beter wordt.
<img src="https://https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/simulated.PNG"/>

### K Means
Dit algoritme kijkt naar een nieuwe wijk en gaat zoeken naar een cluster van huizen. Hierbij probeert het algoritme de huizen zoveel mogelijk te groeperen en daarna plaatst deze een batterij in het midden. 

### Algoritme score
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/all_algorithms.png"/>

## Verschillende classes


### House


### Battery


### Helper


### Solution
