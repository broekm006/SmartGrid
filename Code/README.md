# code

In deze map is de code te vinden waarmee we ons probleem oplossen. In de map alogritmes zijn de verschillende algoritmes opgeslagen in de map classes de verschillende classes.

## Verschillende algoritmes
### Greedy
Dit algoritme verbindt elk huis aan de dichtsbijzijnde batterij met voldoende capaciteit. Vanwege de capaciteit van de batterijen maakt het uit in welke volgorde de huizen worden verbonden. Huizen die vroeg worden ingedeeld kunnen bij de dichtsbijzijnde batterij worden ingedeeld, terwijl de huizen die later worden ingedeeld vanwege gebrek aan capaciteit wellicht aan een minder gunstig gelegen batterij worden verbonden. Daarom zijn er drie varianten van greedy: "output", "distance" & "priority".

- In output worden de huizen eerst gesorteerd op basis van maximale output. Huizen met een hogere output worden eerder verbonden.

- In distance worden huizen gesorteerd op basis van hun afstand tot de dichstbijzijnde batterij. Huizen waarbij deze afstand kort is worden eerder verbonden. h

- In priority wordt het greedy algoritme gebruikt op basis van een prioriteitsscore. Voor elk huis wordt gekeken wat de dichtsbijzijnde batterij is (eerste keus) en welke batterij daarna de dichtsbezijnde is (tweede keus). Hoe groter het verschil in afstand tussen huis en eerste keus, en huis en tweede keus, hoe hoger de prioriteit is om dat huis bij de dichtsbijzijnde batterij in te delen. Huizen met een hogere prioriteitsscore worden als eerste verbonden.



### Swap
Swap is eigenlijk onderdeel van greedy. Afhankelijk van de manier van sorteren en de betreffende wijk, kan het voorkomen dat aan het einde van het greedy-algoritme niet alle huizen zijn ingedeeld omdat er bij geen van de batterijen genoeg plek is om het laatste huis in te delen. Zowel in 'Brute Force' als in 'Hill Climber' worden er huizen gewisseld om er voor te zorgen dat één van de batterijen voldoende plek heeft voor het overgebleven huis.

- In Brute Force wordt er voor elke batterij één verbonden huis losgekoppeld. Daarna worden alle mogelijke switches voor deze vijf huizen afgegaan om te kijken of een andere manier van indelen voldoende plek oplevert voor het laatse huis. Indien dit niet succesvol worden de huizen weer verbonden aan hun oorspronkelijke batterij en herhaalt het proces zich met vijf andere huizen.

- In Hill Climber worden twee batterijen gekozen. De batterij met de hoogste 'current usage' (gebruikte capaciteit) en  de batterij laagste 'current usage'. Vervolgens worden steeds willekeurig twee van de aan deze batterijen verbonden huizen verwisseld.  Dit proces herhaalt zich totdat er ruimte is voor het laatste huis.

### Hill Climber
Dit algoritme kijkt naar een bestaande oplossing en zoekt steeds twee willekeurige batterijen met daarin twee willekeurige huizen en probeert deze vervolgens met elkaar te wisselen. Als de totale afstand tussen de huizen en de verbonden batterijen hierdoor vermindert (en de totale kosten dus dalen) wordt de wissel doorgezet. Anders wordt de wissel geannuleerd.
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/RandomHillClimber_Wijk1/Cost%20frequencies%20after%20Greedy%20priority%20sort%20and%201000%20runs%20of%20HillClimber%20afterwards.png"/>

### Simulated Annealing
Dit algoritme kijkt naar een bestaande oplossing en zoekt steeds twee willekeurige batterijen met daarin twee willekeurige huizen en probeert deze vervolgens te wisselen. Waar hill climber de wissel doorzet indien dit een directe verbetering oplevert, hangt het bij simulated annealing af van de temperatuur en het verschil in afstand (en dus totale kosten). Deze 'temperatuur' is hoog als het algoritme net is gestart. Naarmate het algoritme verder vordert, hoe lager de temperatuur. Een stijging van de totale afstand zal dan niet (snel) worden geaccepteerd.
<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/simulated.PNG"/>

### K Means
K-means wordt gebruikt om de batterijen te verplaatsen nadat de huizen verbonden zijn door het greedy-algoritme. Per batterij kijkt dit algoritme welke huizen eraan verbonden zijn. Vervolgens berekent het algoritme het middelpunt tussen alle verbonden huizen: de gemiddelde x- en y-as voor alle verbonden huizen. Vervolgens wordt de batterij naar dit punt verplaatst. Daarna worden alle huizen losgekoppeld en opnieuw verbonden met het greedy-algoritme. Dit proces herhaalt zich zolang het verplaatsen van de batterijen een vermindering van de totale kosten oplevert.


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
De solution class wordt in verschillende algoritmes gebruikt om tussentijdse oplossingen en de eindoplossing op te slaan. De solution class bevat een aantal methodes. 'distance_calc()' om de afstand tussen huizen en batterijen op te meten. 'Sort_houses()' om in te zien wat het duurste en wat het goedkoopste huis is voor de huidige oplossing. 'Calculate_costs()' en 'calculate_costs2()' om de totale kosten uit te rekenen. 'Calculate_costs()' wordt gebruikt in de iteratieve algoritmes. Hierbij wordt er een 'id' mee gegegeven om bij te houden bij welke iteratie de desbetreffende solution hoort. Bij 'calculate_costs2()' hoeft er geen 'id' te worden meegegeven. Deze wordt gebruikt bij de andere algoritmes. In 'houses_costs()' worden de totale kabelkosten berekend. In 'bounds()' worden de upper- en lowerbound berekend. Het is noodzakelijk om deze voor verschillende oplossing opnieuw te bereken omdat er na k-means en HAC geen gebruik meer kan worden gemaakt van de innitiële upper- en lowerbound. Bij deze algoritmes worden de batterijen immers verplaatst. Bij HAC gaat het bovendien om een variërend aantal batterijen waar verschillende batterijkosten aan vast kunnen zitten. De maximale en minimale kosten zijn daardoor veranderd.

### Helper
Een helper class die een aantal functies bevat om inzicht te geven in de werking van de algoritmes. Zoals 'battery_info()'' om informatie te printen over alle meegegeven batterijen.
