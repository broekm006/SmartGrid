import sys
sys.path.append('Code/algoritmes')
from sort import Sort
from swap import Swap
from helper import Helper
import copy

class Greedy(object):

    def __init__(self, houses, batteries, variant):
        self.houses = houses
        self.batteries = batteries
        self.variant = self.type(variant)

    # welke variant van greedy?
    def type(self, type):

        if type == "output":
            self.output()
        elif type == "distance":
            self.distance()
        elif type == "priority":
            self.pv()
        else:
            print("Greedy type error")

    # MAX_OUTPUT
    def output(self):
        ''' Connect house to nearest battery with available capacity'''

        self.houses = Sort.max_output(Sort, self.houses)

        for house in self.houses:
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    house.connect(battery)

                    # update battery usage and connected list
                    battery.add(house)

                    # cable costs
                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
                    house.cable_costs(battery.distance)

                    break;

        #Swap.swap_hill_climber(Swap, self.houses, self.batteries)
        self.check()


    # DISTANCE
    def distance(self):
        ''' Connect house to nearest battery with available capacity'''

        for battery in self.batteries:

            # sorts houses based on distance to current battery
            self.houses = Sort.distance(Sort, self.houses, battery)

            # connect battery to nearest house that isn't connected
            for house in self.houses:
                if battery.check_amp() > house.amp and not house.connection:

                    # distance
                    distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                    # Update battery usage & calculate cable costs
                    battery.add(house)
                    house.connect(battery)
                    house.cable_costs(distance)

        #Swap.swap_hill_climber(Swap, self.houses, self.batteries)
        self.check()


    # PRIORITY VALUE
    def pv(self):
        ''' Connect house to nearest battery with available capacity'''

        # sorts houses based on priority value
        self.houses = Sort.priority_value(Sort, self.houses, self.batteries)

        for house in self.houses:

            # sorts batteries based on distance from current house --> kan nog apart
            for battery in self.batteries:
                battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            # connect house to nearest available battery
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    house.connect(battery) # Dubbel, nog aanpassen!

                    # Update battery usage & calculate cable costs
                    battery.add(house)
                    house.cable_costs(battery.distance)
                    break;

        #Swap.swap_hill_climber(Swap, self.houses, self.batteries)

        # check
        self.check()

    def check(self):
        ''' Checks whether all houses are connected '''

        for house in self.houses:
             if not house.connection:
                 print(house.id)
                 self.swap(house, 0)

    def swap(self, unconnected_house, int):
        ''' Swap houses '''

        # copy batteries & houses
        temp_batteries = copy.deepcopy(self.batteries)
        temp_houses = copy.deepcopy(self.houses)

        for house in temp_houses:
            if house.id == unconnected_house:
                unconnected_house = copy.deepcopy(house)
                break

        print("UNCONNECTED: " + str(unconnected_house.id))

        # sort batteries (0 - 4)
        temp_batteries = sorted(temp_batteries, key= lambda battery: battery.id)

        # test, meer ruimte
        # temp_batteries[0].max_amp +=  100

        # disconnect most expensive house from each battery
        available = []
        for battery in temp_batteries:
            connected_houses = sorted(battery.connected, key=lambda house: house.costs, reverse=True)

            if battery.id == 0:
                house_0 = connected_houses[int]
            elif battery.id == 1:
                house_1 = connected_houses[int]
            elif battery.id == 2:
                house_2 = connected_houses[int]
            elif battery.id == 3:
                house_3 = connected_houses[int]
            elif battery.id == 4:
                house_4 = connected_houses[int]

            battery.remove(connected_houses[int])

        # Materix??
        materix = {house_0.id: [house_1, house_2, house_3, house_4],
                house_1.id: [house_0, house_2, house_3, house_4],
                house_2.id: [house_0, house_1, house_3, house_4],
                house_3.id: [house_0, house_1, house_2, house_4],
                house_4.id: [house_0, house_1, house_2, house_3]}

        removed_houses = [house_0, house_1, house_2, house_3, house_4]

        working = []
        not_working = []

        # get all permutations with current house assigned to battery 0
        for house in removed_houses:
            options = self.bfs(materix, house)

            # categoriseer als niet werkende indien één van de gewisselde huizen niet past
            # kan volgens mij niet removen in for-loop? --> options.remove(option)
            for option in options:
                for i, house in enumerate(option):
                    if house.amp > temp_batteries[i].check_amp():
                        not_working.append(option)
                        continue

            # categoriseer als werkende als swap wel mogelijk is
            for option in options:
                if option not in not_working:
                    working.append(option)

        # categoriseer als mogelijke oplossing indien één van de batterijen plaats heeft voor unconnected_house
        possible = []
        for option in working:
            for i, house in enumerate(option):
                if unconnected_house.amp < (temp_batteries[i].check_amp() - house.amp):
                    possible.append(option)

        # voer eerste oplossing uit
        for solution in possible:
            combination = solution
            break

        # Probeer opnieuw met één naar duurste huis (int + 1) indien laatste huis niet geplaats kan worden
        if len(possible) == 0:
            print("Try again")
            int += 1
            if int > 25:
                print("GEEN OPLOSSING GEVONDEN")
            else:
                self.swap(unconnected_house, int)
        else:
            # swap houses according to combination
            for i, house in enumerate(combination):
                house.connect(temp_batteries[i])
                temp_batteries[i].add(house)

            # place last house
            for battery in temp_batteries:
                if battery.check_amp() > unconnected_house.amp:
                    unconnected_house.connect(battery)
                    battery.add(unconnected_house)
                    break

            for battery in temp_batteries:
                connected = []
                count = 0
                for house in battery.connected:
                    count += 1
                    connected.append(house.id)
                print("Connected: " + str(connected))
                print("Count: " + str(count))
                print("Current_usage: " + str(battery.current_usage))
                print("Available: " + str(battery.check_amp()))
                print()

    # BRUTE FORCE
    def bfs(self, materix, start, visited=[]):
        visited = visited+[start]
        paths = []
        list = materix.get(start.id)

        if len(visited) == 5:
            return[visited]
        else:
            for house in list:
                if house not in visited:
                    newpaths = self.bfs(materix, house, visited)
                    for newpath in newpaths:
                        paths.append(newpath)
        return paths
