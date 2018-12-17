import sys, random, copy
sys.path.append('Code/classes')

from house import House
from battery import Battery
from brute_force import Brute_force

class Swap(object):

    def swap_hill_climber(self, houses, batteries):
        ''' A swap algorithm that looks for houses that are not yet placed and switches
            between the lowest and second lowest battery to make space for the remaining house(s)
        '''
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

                #remove "lowest id + update current_usage"
                batteries[battery_id1.id].remove(random1)
                batteries[battery_id2.id].remove(random2)

                max = batteries[battery_id1.id].max_amp
                currents1 = batteries[battery_id1.id].current_usage
                currents2 = batteries[battery_id2.id].current_usage

                if  max - (currents1 + random2.amp) > 0 and max - (currents2 + random1.amp) > 0:
                    #add removed house to other battery_id
                    batteries[battery_id1.id].add(random2)
                    batteries[battery_id2.id].add(random1)
                    random1.connect(batteries[battery_id2.id])
                    random2.connect(batteries[battery_id1.id])

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


    def check(self, houses, batteries):
        ''' Checks whether all houses are connected '''

        for house in houses:
            if not house.connection:
                print(house.id)
                self.swap(self, house, batteries, houses)



    def swap(self, unconnected_house, old_batteries, old_houses):
        ''' Swap houses based on brute force '''

        # copy batteries & houses
        temp_batteries = copy.deepcopy(old_batteries)
        temp_houses = copy.deepcopy(old_houses)

        counter = 0

        while counter < 100000:
            counter += 1

            for house in temp_houses:
                if house.id == unconnected_house:
                    unconnected_house = copy.deepcopy(house)
                    break

            print("UNCONNECTED: " + str(unconnected_house.id))

            # sort batteries (0 - 4)
            temp_batteries = sorted(temp_batteries, key= lambda battery: battery.id)

            # choose random house
            house_0 = random.choice(temp_batteries[0].connected)
            house_1 = random.choice(temp_batteries[1].connected)
            house_2 = random.choice(temp_batteries[2].connected)
            house_3 = random.choice(temp_batteries[3].connected)
            house_4 = random.choice(temp_batteries[4].connected)

            # disconnect
            temp_batteries[0].remove(house_0)
            temp_batteries[1].remove(house_1)
            temp_batteries[2].remove(house_2)
            temp_batteries[3].remove(house_3)
            temp_batteries[4].remove(house_4)

            # create materix
            materix = {house_0.id: [house_1, house_2, house_3, house_4],
                    house_1.id: [house_0, house_2, house_3, house_4],
                    house_2.id: [house_0, house_1, house_3, house_4],
                    house_3.id: [house_0, house_1, house_2, house_4],
                    house_4.id: [house_0, house_1, house_2, house_3]}

            removed_houses = [house_0, house_1, house_2, house_3, house_4]

            working = []
            not_working = []

            # get all permutations with current house assigned to battery
            for house in removed_houses:
                options = Brute_force.bfs(Brute_force, materix, house)

                # Categorize if swap is not possible
                for option in options:
                    for i, house in enumerate(option):
                        if house.amp > temp_batteries[i].check_amp():
                            not_working.append(option)
                            continue

                # Categorize if swap is possible
                for option in options:
                    if option not in not_working:
                        working.append(option)

            # loop through if a possible solution gives room for the unconnected_house
            possible = []
            for option in working:
                for i, house in enumerate(option):
                    if unconnected_house.amp < (temp_batteries[i].check_amp() - house.amp):
                        possible.append(option)

                # try all possible solutions
                for solution in possible:
                    combination = solution
                break

            # Try again with second most expensive house (int + 1)
            if len(possible) == 0:
                print("Try again")

                # reconnect
                temp_batteries[0].add(house_0)
                temp_batteries[1].add(house_1)
                temp_batteries[2].add(house_2)
                temp_batteries[3].add(house_3)
                temp_batteries[4].add(house_4)

            else:
                # swap houses according to combination
                for house in combination:
                    print("House ID COMBI: ", house.id)

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
                break
