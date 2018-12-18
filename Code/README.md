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
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/RandomHillClimber_Wijk1/Cost%20frequencies%20after%20Greedy%20priority%20sort%20and%201000%20runs%20of%20HillClimber%20afterwards.png"/>

### Simulated Annealing
Dit algoritme kijkt naar een bestaande oplossing. Deze zoekt twee willekeurige batterijen met daarin twee willekeurige huizen. Daarna kijkt deze naar de distance en bepaald op basis van temperatuur of deze wisseling mag worden uitgevoerd. Hierbij kan het resultaat eerst slechter worden voor het weer beter wordt.
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/simulated.PNG"/>

### K Means
Dit algoritme kijkt naar een nieuwe wijk en gaat zoeken naar een cluster van huizen. Hierbij probeert het algoritme de huizen zoveel mogelijk te groeperen en daarna plaatst deze een batterij in het midden.

### Hierarchical Agglomerative Clustering (HAC)
Dit algoritme maakt voor ieder huis in de wijk een batterij aan met de kleinste capaciteit (450 ampère) en plaatst deze batterij op dezelfde coordinaten als het betreffende huis. Vervolgens kijkt het algoritme welke batterijen het dichtst bij elkaar staan. Deze batterijen worden samengevoegd tot één batterij mits de huizen die op dat moment aan één van beide batterijen zijn aangesloten op één batterij kunnen worden aangesloten: ze overschrijden gezamenlijk niet de maximale capaciteit van 1800 ampère. De capaciteit van de nieuwe samengevoegde batterij is de kleinst mogelijke capaciteit waarbij alle huizen kunnen worden aangesloten (450, 900 of 1800 ampère).De nieuwe batterij wordt in het midden tussen de oude batterijen geplaatst en de oude batterijen verwijderd. Daarna worden alle connecties verbroken en worden de huizen en batterijen op nieuw verbonden op basis van greedy (output) en k-means. De nieuwe oplossing wordt opgeslagen. Het voorgenoemde proces herhaalt zich tot geen 'merges' meer mogelijk zijn. Aan het einde van het algoritme wordt er gekeken welke oplossing er het goedkoopst was.

### Algoritme score
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/all_algorithms.png"/>

## classes

### House
Voor alle huizen in de 'WijkN_huizen.csv' bestanden worden een House-Object aangemaakt. De huizen hebben een ID, X-coordinaat, Y-coordinaat en output('amp'), welke data afkomstig is uit het csv bestand voor de betreffende wijk. Ook hebben de huizen  een 'distance_to_battery' variabele om de afstand tot de aangesloten batterij in op te slaan, en een 'costs' variabele om de kabelkosten voor de aansluiting op die batterij in op te slaan. Daarnaast beschikken de House-Oject's in over een 'priority_list' om de prioriteitsscores van de Greedy met Priority-Sort in op te slaan. Tot slot hebben House-Object's nog een "connected" variabele om de aangesloten batterij in op te slaan en een "connection" variabele om de aanssluitingsstatus ('True'/'False') in op te slaan.

House-Objecten hebben een 'connect' methode om verbinding te maken met een batterij, een 'cable_costs' methode om de kabelkosten voor de aansluiting op een batterij te berekenen en een 'distance' methode om de afstand tot een batterij te berekenen.

### Battery
Voor alle batterijen in de 'WijkN_batterijen.txt' bestanden worden een Battery-Object aangemaakt. De batterijen hebben een ID, X-coordinaat, Y-coordinaat en maximale capaciteit('max_amp'), welke data afkomstig is uit het csv bestand voor de betreffende wijk.


### Solution
De solution class wordt in verschillende algoritmes gebruikt om tussentijdse oplossingen en de eindoplossing op te slaan door de configuratie van huizen en batterijen mee te geven. De solution class bevat een aantal methodes. 'distance_calc()' om de afstand tussen huizen en batterijen op te meten. 'sort_houses()' om in te zien wat het duurste en wat het goedkoopste huis is voor de huidige oplossing. Het gaat daarbij om de aan het huis gelinkte kabelkosten. 'calculate_costs()' en 'calculate_costs2()' om de totale kosten uit te rekenen. 'Calculate_costs()' wordt gebruikt in de iteratieve algoritmes. Hierbij wordt er een 'id' mee gegegeven om bij te houden bij welke iteratie de desbetreffende solution hoort. Bij 'calculate_costs2()' hoeft er geen 'id' te worden meegegeven. Deze wordt gebruikt bij de andere algoritmes. In 'houses_costs()' worden de totale kabelkosten berekend. In 'bounds()' worden de upper- en lowerbound berekend. Het is noodzakelijk om deze voor verschillende oplossing opnieuw te bereken omdat er na k-means en HAC geen gebruik meer kan worden gemaakt van de innitiële upper- en lowerbound. Bij deze algoritmes worden de batterijen immers verplaatst. Bij HAC gaat het bovendien om een varierend aantal batterijen waar verschillende batterijkosten aan vast zitten. De maximale en minimale kosten zijn daardoor veranderd.

### Helper
Een helper class die een aantal functies bevat om inzicht te geven in de werking van de algoritmes. Zoals 'battery_info()'' om informatie te printen over alle meegegven batterijen.
