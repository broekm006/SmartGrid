import copy
import sys, random
sys.path.append('Code/classes')

from house import House
from battery import Battery
from brute_force import Brute_force

class Swap(object):

    # a swap algorithm that looks for houses that are not yet placed and switches houses
    # between the lowest and second lowest battery to make space for the remaining house(s).
    def swap_hill_climber(self, houses, batteries):
        # counter to see how many times the swap runs
        counter = 0

        for house in houses:
            while not house.connection:
                lowest, second = float('inf'), float('inf')
                batteries = sorted(batteries, key=lambda battery: battery.id)

                # get lowest & second lowest battery
                for battery in batteries:
                    if battery.current_usage <= lowest:
                        lowest, second = battery.current_usage, lowest
                        battery_id1 = battery
                    elif battery.current_usage < second:
                        second = battery.current_usage

                # get battery id for second
                for battery in batteries:
                    if second == battery.current_usage:
                        battery_id2 = battery

                # choose random id from battery-house list
                random1 = random.choice(batteries[battery_id1.id].connected)
                random2 = random.choice(batteries[battery_id2.id].connected)

                # # look for the amp of the randomly selected house
                for house_amp in houses:
                    if house_amp.id == random1.id:
                        random1_amp = house_amp.amp

                    if house_amp.id == random2.id:
                        random2_amp = house_amp.amp

                #remove "lowest id + update current_usage"
                batteries[battery_id1.id].remove(random1)
                batteries[battery_id2.id].remove(random2)

                max = batteries[battery_id1.id].max_amp
                currents1 = batteries[battery_id1.id].current_usage
                currents2 = batteries[battery_id2.id].current_usage

                if  max - (currents1 + random2_amp) > 0 and max - (currents2 + random1_amp) > 0:
                    #add removed house to other battery_id
                    batteries[battery_id1.id].add(random2)
                    batteries[battery_id2.id].add(random1)

                else:
                    #undo remove because the switch does not work (battery overload)
                    batteries[battery_id1.id].add(random1)
                    batteries[battery_id2.id].add(random2)

                #calculate new amp
                low_max = batteries[battery_id1.id].current_usage
                high_max = batteries[battery_id2.id].current_usage

                # check if left_over house fits in lowest value battery
                if  low_max <= batteries[battery_id1.id].max_amp - house.amp:
                    batteries[battery_id1.id].add(house)
                    house.connect(battery_id1)
                    #house.connection = True

                # check if left_over house fits in second lowest value battery
                elif high_max <= batteries[battery_id2.id].max_amp - house.amp:
                    batteries[battery_id2.id].add(house)
                    #house.connection = True
                    house.connect(battery_id2)

                #increase counter (times the swap ran)
                counter += 1

        current_usage = 0
        #print(counter)
        for battery in batteries:
            print()
            print("ID:" + str(battery.id))
            print("Current usage: " + str(battery.current_usage))
            print("Available: " + str(battery.check_amp()))

            # listy is only here to get a visual representation of the connected house ID's
            # before it was: print("Connected ID's" + str(battery.connected))

            listy = []
            for item in battery.connected:
                listy.append(item.id)
            print("Connected ID's" + str(listy))

            current_usage += battery.current_usage
            print()

        print("Total battery usage: " + str(current_usage))

    def check(self, houses, batteries):
        ''' Checks whether all houses are connected '''

        for house in houses:
            if not house.connection:
                print(house.id)
                self.swap(self, house, 0, batteries, houses)

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
