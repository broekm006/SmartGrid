import sys, random
sys.path.append('Code/classes')

from house import House
from battery import Battery

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
                        battery_id1 = battery.id
                    elif battery.current_usage < second:
                        second = battery.current_usage

                # get battery id for second
                for battery in batteries:
                    if second == battery.current_usage:
                        battery_id2 = battery.id

                # choose random id from battery-house list
                random1 = random.choice(batteries[battery_id1].connected)
                random2 = random.choice(batteries[battery_id2].connected)

                # # look for the amp of the randomly selected house
                for house_amp in houses:
                    if house_amp.id == random1.id:
                        random1_amp = house_amp.amp

                    if house_amp.id == random2.id:
                        random2_amp = house_amp.amp

                #remove "lowest id + update current_usage"
                batteries[battery_id1].remove(random1)
                batteries[battery_id2].remove(random2)

                max = batteries[battery_id1].max_amp
                currents1 = batteries[battery_id1].current_usage
                currents2 = batteries[battery_id2].current_usage

                if  max - (currents1 + random2_amp) > 0 and max - (currents2 + random1_amp) > 0:
                    #add removed house to other battery_id
                    batteries[battery_id1].add(random2)
                    batteries[battery_id2].add(random1)

                else:
                    #undo remove because the switch does not work (battery overload)
                    batteries[battery_id1].add(random1)
                    batteries[battery_id2].add(random2)

                #calculate new amp
                low_max = batteries[battery_id1].current_usage
                high_max = batteries[battery_id2].current_usage

                # check if left_over house fits in lowest value battery
                if  low_max <= batteries[battery_id1].max_amp - house.amp:
                    batteries[battery_id1].add(house)
                    house.connection = True

                # check if left_over house fits in second lowest value battery
                elif high_max <= batteries[battery_id2].max_amp - house.amp:
                    batteries[battery_id2].add(house)
                    house.connection = True

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

    def swap_dfs(self):
        pass
