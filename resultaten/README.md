# resultaten

In deze map zijn de resultaten te vinden, alle onderstaande resultaten zijn voor Wijk 1.

## Resultaten Greedy (output, distance, priority)
In de onderstaande staafgrafiek staan drie oplossingen weergeven die zijn gegenereerd door het Greedy algoritme. Iedere staaf staat voor een bepaalde sorteermethode. Duidelijk is dat de "priority" methode de meest efficiente oplossing geeft. Deze methode bepaalt voor ieder huis wat de afstand tot de meest dichtbijzijnde batterij is en de batterij die daarna het meest dichtbij is. Als het verschil tussen deze twee afstanden groot is, krijgt het huis een hoge prioriteitsscore en zal het huis eerder worden ingedeeld door het Greedy algoritme.

Uit de grafiek blijkt dat het Greedy Algoritme kan leiden tot resultaten in het onderste kwart van de StateSpace.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/greedy%20comparison.png"/>

## Resultaten Hill_climber
In de onderstaande staafgrafiek staan 1000 uitkomsten van het HillClimber algoritme na 1000 iteraties. Voorafgaand aan het HillClimber Algoritme zijn de huizen gesorteerd op prioriteitscore en aangesloten op de batterijen met het Greedy algoritme.

Uit de grafiek blijkt dat de oplossingen die deze algoritmes genereren veelal rond de 58500 kosten.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/Cost%20frequencies%20after%20Greedy%20priority%20sort%20and%201000%20runs%20of%20HillClimber%20afterwards.png"/>

## Resultaten Simulated_annealing
In de onderstaande grafiek is het verloop van tien runs van het Simulated Annealing algoritme te zien. De oplossingen van dit algoritme varieren voor wijk 1 over het algemeen tussen de 57000 en 60000.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/simulated_10times.PNG"/>

## Resultaten K_means
In de onderstaande grafiek is een overzicht te vinden van de batterijen en de huizen die daarop aangesloten zijn, na afloop van de K-Means en Simulated Annealing algortimes. De huizen zijn aangeduid met een stip en de batterijen met een kruis. Als een stip en een kruis dezelfde kleur hebben, betekent dit dat een huis en batterij op elkaar aangesloten zijn.

De totale kosten voor de onderstaande oplossing bedragen 41632.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/K-means/kmeansAndSimulated.png"/>

## Resultaten Hierarchical Agglomerative Clustering
In de onderstaande grafiek is een overzicht te vinden van de batterijen en de huizen die daarop aangesloten zijn, na afloop van de Hierarchical Agglomerative Clustering en Simulated Annealing algortimes. De huizen zijn aangeduid met een stip en de batterijen met een kruis. Als een stip en een kruis dezelfde kleur hebben, betekent dit dat een huis en batterij op elkaar aangesloten zijn.

De totale kosten voor de onderstaande oplossing bedragen 23364.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/Hierarchical_Agglomerative_Clustering_V2.png"/>

## Score algoritmes
In de onderstaande staafgrafiek zijn dat de resultaten van enkele (combinaties van) algoritmes tegen elkaar afgezet. Te zien is dat de priority sorteermethode in dit geval de laagste kosten heeft oplevert. Uit deze en voorgaande grafieken blijkt ook dat het HillClimber algoritme en het Simulated Annealing algoritme in veel gevallen vergelijkbare oplossingen kunnen opleveren.

<img src="https://github.com/broekm006/SmartGrid/blob/master/resultaten/visualisaties/all_algorithms.png"/>
