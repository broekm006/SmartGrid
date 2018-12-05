#done
# kies random battery
# kies random huis

#not done
# swap > check distance
# if beter > keep
# else > swap back

import random
from solution import Solution

class Hill_climber(object):

    def __init__(self, houses, batteries, number_of_times):
        self.houses = houses
        self.batteries = batteries
        self.number_of_times = number_of_times

    def ice_climbers(self):
        counter = 0
        self.batteries = sorted(self.batteries, key=lambda battery: battery.id)
        # loop throug algorithm for number_of_times
        for i in range(self.number_of_times):
            random_battery = random.choice(self.batteries)
            random_battery2 = random.choice(self.batteries)

            # make sure 2 different batteries are chosen
            while random_battery == random_battery2:
                random_battery2 = random.choice(self.batteries)

            #choose 2 random houses from the batteries
            random_house_in_battery = random.choice(random_battery.connected)
            random_house_in_battery2 = random.choice(random_battery2.connected)

            # look for the amp of the randomly selected house
            # for house_amp in self.houses:
            #     if house_amp.id == random_house_in_battery.id:
            #         random1_amp = house_amp.amp
            #
            #     if house_amp.id == random_house_in_battery.id:
            #         random2_amp = house_amp.amp

            #remove "lowest id + update current_usage"
            self.batteries[random_battery.id].remove(random_house_in_battery)
            self.batteries[random_battery2.id].remove(random_house_in_battery2)

            max = self.batteries[random_battery.id].max_amp
            currents1 = self.batteries[random_battery.id].current_usage
            currents2 = self.batteries[random_battery2.id].current_usage

            # calculate distance
            solution = Solution(self.houses, self.batteries)
            solution.distance_calc(random_house_in_battery, random_battery)

            old_distance = solution.distance_calc(random_house_in_battery, random_battery)
            old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)

            new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
            new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)

            #print("total:  ", old_distance + old_distance2)
            #print("total2: ", new_distance + new_distance2)
            # check if swap is possible
            if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
                #add removed house to other battery_id
                if old_distance + old_distance2 < new_distance + new_distance2:
                    self.batteries[random_battery.id].add(random_house_in_battery2)
                    self.batteries[random_battery2.id].add(random_house_in_battery)

                else:
                    #undo remove because the switch does not work (battery overload)
                    self.batteries[random_battery.id].add(random_house_in_battery)
                    self.batteries[random_battery2.id].add(random_house_in_battery2)

            else:
                #undo remove because the switch does not work (battery overload)
                self.batteries[random_battery.id].add(random_house_in_battery)
                self.batteries[random_battery2.id].add(random_house_in_battery2)

            counter += 1

        '''
        # check connected id vs amp available > to fix
        current_usage = 0
        print(counter)
        for battery in self.batteries:
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
        '''
        #print("total distance1: ", solution.total_distance())
        #print(counter)
