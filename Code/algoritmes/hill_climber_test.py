#done
# kies random battery
# kies random huis

#not done
# swap > check distance
# if beter > keep
# else > swap back

import random
from solution import Solution

class Hill_climber_test(object):

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

            # choose 2 random houses from the batteries
            random_house_in_battery = random.choice(random_battery.connected)
            random_house_in_battery2 = random.choice(random_battery2.connected)

            # look for the amp of the randomly selected house
            for house_amp in self.houses:
                if house_amp.id == random_house_in_battery.id:
                    random1_amp = house_amp.amp

                if house_amp.id == random_house_in_battery.id:
                    random2_amp = house_amp.amp

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
            if  max - (currents1 + random2_amp) > 0 and max - (currents2 + random1_amp) > 0:
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


    def best_choice(self):
        #while len(possible_swaps) > 0 ???

        # list of connected houses for each battery
        b0, b1, b2, b3, b4 = self.batteries[0].connected, self.batteries[1].connected, \
                                self.batteries[2].connected, self.batteries[3].connected, \
                                self.batteries[4].connected

        battery_lists = [b0, b1, b2, b3, b4]

        possible_swaps = []
        for i, battery in enumerate(self.batteries):
            for house in battery.connected:
                counter = 0
                for list in battery_lists[(i + 1):-1]:
                    counter += 1
                    for swap_house in list:

                        # append swap if enough capacity
                        if battery.check_amp() + house.amp >= swap_house.amp and self.batteries[i + counter].check_amp() + swap_house.amp >= house.amp:

                            house.distance(battery)
                            swap_house.distance(self.batteries[i+counter])
                            score1 =  house.distance_to_battery - Solution.distance_calc(Solution, house, self.batteries[i + counter])
                            score2 = swap_house.distance_to_battery - Solution.distance_calc(Solution, swap_house, battery)
                            score = score1 + score2

                            if score > 0:
                                possible_swaps.append([house, swap_house, score])
        def takeThird(elem):
            return elem[2]

        # sort possible swaps --> best swap?
        possible_swaps.sort(key=takeThird, reverse=True)
        print(possible_swaps)

        for swap in possible_swaps:
            house1 = swap[0]
            b1 = house1.connected
            print("B1:")
            print(b1)
            house2 = swap[1]
            b2 = house2.connected

            for house in b2.connected:
                print("ID: ", house.id)
            print("House2: ", house2.id)
            print()
            # swap
            self.batteries[b1.id].remove(house1)
            self.batteries[b2.id].remove(house2)




            b1.add(house2)
            house2.connect(b1)

            b2.add(house1)
            house1.connect(b2)
