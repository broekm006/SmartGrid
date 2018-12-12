#done
# kies random battery
# kies random huis

#not done
# swap > check distance
# if beter > keep
# else > swap back

import random, csv, copy
from solution import Solution

class Hill_climber(object):

    def __init__(self, houses, batteries, number_of_times, number_of_runs):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.number_of_times = number_of_times
        self.n = number_of_runs
        self.results = []
        self.multi_results = []
        self.ice_climbers()

    def ice_climbers(self):

        swaps_made = 0

        for count in range(self.n):
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses = copy.deepcopy(self.houses)

            swap_counter = 0

            while True:
                swap_list = self.possible_swaps(temp_houses, temp_batteries)

                random_swap = random.choice(swap_list)

                random_house_in_battery = random_swap[0]
                random_house_in_battery2 = random_swap[1]

                random_battery = random_house_in_battery.connected
                random_battery2 = random_house_in_battery2.connected

                # look for the amp of the randomly selected house
                # for house_amp in self.houses:
                #     if house_amp.id == random_house_in_battery.id:
                #         random1_amp = house_amp.amp
                #
                #     if house_amp.id == random_house_in_battery.id:
                #         random2_amp = house_amp.amp


                    # max = temp_batteries[random_battery.id].max_amp
                    # currents1 = temp_batteries[random_battery.id].current_usage
                    # currents2 = temp_batteries[random_battery2.id].current_usage

                    # calculate distance
                #print("random battery:", random_battery)
                #print("random battery2:", random_battery2)

                solution = Solution(temp_houses, temp_batteries)

                old_distance = solution.distance_calc(random_house_in_battery, random_battery)
                old_distance2 = solution.distance_calc(random_house_in_battery2, random_battery2)

                new_distance = solution.distance_calc(random_house_in_battery, random_battery2)
                new_distance2 = solution.distance_calc(random_house_in_battery2, random_battery)

                #print("total:  ", old_distance + old_distance2)
                #print("total2: ", new_distance + new_distance2)
                # check if swap is possible
                #if  max - (currents1 + random_house_in_battery2.amp) > 0 and max - (currents2 + random_house_in_battery.amp) > 0:
                    #add removed house to other battery_id
                if old_distance + old_distance2 > new_distance + new_distance2:
                    print("Swap reduces cable costs!")

                    #remove "lowest id + update current_usage"
                    temp_batteries = sorted(temp_batteries, key=lambda battery: battery.id)
                    temp_batteries[random_battery.id].remove(random_house_in_battery)
                    temp_batteries[random_battery2.id].remove(random_house_in_battery2)

                    temp_batteries[random_battery.id].add(random_house_in_battery2)
                    temp_batteries[random_battery2.id].add(random_house_in_battery)
                    random_house_in_battery.connect(temp_batteries[random_battery2.id])
                    random_house_in_battery2.connect(temp_batteries[random_battery.id])

                    temp_houses[random_house_in_battery.id] = random_house_in_battery
                    temp_houses[random_house_in_battery2.id] = random_house_in_battery2


                #     else:
                #         #undo remove because the switch does not work (battery overload)
                #         temp_batteries[random_battery.id].add(random_house_in_battery)
                #         temp_batteries[random_battery2.id].add(random_house_in_battery2)
                #
                # else:
                #     #undo remove because the switch does not work (battery overload)
                #     temp_batteries[random_battery.id].add(random_house_in_battery)
                #     temp_batteries[random_battery2.id].add(random_house_in_battery2)


                # Save solution & append costs to self.results
                    solution = Solution(temp_houses, temp_batteries)
                    self.results.append(solution.calculate_costs())
                    swaps_made += 1

                else:
                    print("Swap does not reduce cable costs!")

                swap_counter += 1

                if swap_counter == self.number_of_times:
                    print(swap_counter)
                    break

            # EINDE HILL CLIMBER
            eind_oplossing = Solution(temp_houses, temp_batteries)
            self.multi_results.append(eind_oplossing.calculate_costs())



    def possible_swaps(self, houses, batteries):

        # list of connected houses for each battery
        b0, b1, b2, b3, b4 = batteries[0].connected, batteries[1].connected, \
                                batteries[2].connected, batteries[3].connected, \
                                batteries[4].connected

        battery_lists = [b0, b1, b2, b3, b4]

        possible_swaps = []

        for index, battery in enumerate(batteries):
            for house in battery.connected:
                counter = 0
                for list in battery_lists[(index + 1):-1]:
                    counter += 1
                    for swap_house in list:

                        # append swap if enough capacity
                        if (battery.check_amp() + house.amp) >= swap_house.amp and (batteries[index + counter].check_amp() + swap_house.amp) >= house.amp:
                                possible_swaps.append([house, swap_house])

        return possible_swaps
