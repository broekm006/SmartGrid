import copy
import sys, random
sys.path.append('Code/classes')

from house import House
from battery import Battery
from brute_force import Brute_force

class Swap(object):

    def swap(self, unconnected_house, int, batteries, houses):
        ''' Swap houses '''

        # copy batteries & houses
        temp_batteries = copy.deepcopy(batteries)
        temp_houses = copy.deepcopy(houses)

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
                house_1 = connected_houses[int + 1]
            elif battery.id == 1:
                house_2 = connected_houses[int]
                house_3 = connected_houses[int + 1]
            elif battery.id == 2:
                house_4 = connected_houses[int]
                house_5 = connected_houses[int + 1]
            elif battery.id == 3:
                house_6 = connected_houses[int]
                house_7 = connected_houses[int + 1]
            elif battery.id == 4:
                house_8 = connected_houses[int]
                house_9 = connected_houses[int + 1]

            battery.remove(connected_houses[int])
            battery.remove(connected_houses[int + 1])

        # Materix??
        materix = {house_0.id: [house_1, house_2, house_3, house_4, house_5, house_6, house_7, house_8, house_9],
                house_1.id: [house_0, house_2, house_3, house_4, house_5, house_6, house_7, house_8, house_9],
                house_2.id: [house_0, house_1, house_3, house_4, house_5, house_6, house_7, house_8, house_9],
                house_3.id: [house_0, house_1, house_2, house_4, house_5, house_6, house_7, house_8, house_9],
                house_4.id: [house_0, house_1, house_2, house_3, house_5, house_6, house_7, house_8, house_9],
                house_5.id: [house_0, house_1, house_2, house_3, house_4, house_6, house_7, house_8, house_9],
                house_6.id: [house_0, house_1, house_2, house_3, house_4, house_5, house_7, house_8, house_9],
                house_7.id: [house_0, house_1, house_2, house_3, house_4, house_5, house_6, house_8, house_9],
                house_8.id: [house_0, house_1, house_2, house_3, house_4, house_5, house_6, house_7, house_9],
                house_9.id: [house_0, house_1, house_2, house_3, house_4, house_5, house_6, house_7, house_8]}

        removed_houses = [house_0, house_1, house_2, house_3, house_4, house_5, house_6, house_7, house_8, house_9]

        working = []
        not_working = []

        # get all permutations with current house assigned to battery 0
        for house in removed_houses:
            options = Brute_force.bfs(Brute_force, materix, house)

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
                self.swap(Swap, unconnected_house, int, batteries, houses)
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
