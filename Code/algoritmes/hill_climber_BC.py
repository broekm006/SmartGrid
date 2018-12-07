#done
# kies random battery
# kies random huis

#not done
# swap > check distance
# if beter > keep
# else > swap back
import csv, copy, random
from solution import Solution

class Hill_climber_BC(object):

    def __init__(self, houses, batteries, number_of_runs):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        self.results = []
        self.multi_results = []
        self.n = number_of_runs
        self.best_choice()

    def best_choice(self):

        for count in range(self.n):
            # TEMP
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses = copy.deepcopy(self.houses)
            print("COUNT: ", count)
            while True:

                # list of connected houses for each battery
                b0, b1, b2, b3, b4 = temp_batteries[0].connected, temp_batteries[1].connected, \
                                        temp_batteries[2].connected, temp_batteries[3].connected, \
                                        temp_batteries[4].connected

                battery_lists = [b0, b1, b2, b3, b4]

                possible_swaps = []

                for i, battery in enumerate(temp_batteries):
                    for house in battery.connected:
                        counter = 0
                        for list in battery_lists[(i + 1):-1]:
                            counter += 1
                            for swap_house in list:

                                # append swap if enough capacity
                                if (battery.check_amp() + house.amp) >= swap_house.amp and (temp_batteries[i + counter].check_amp() + swap_house.amp) >= house.amp:
                                    house.distance(battery)
                                    swap_house.distance(temp_batteries[i+counter])

                                    # house.distance_to_battery???
                                    score1 =  house.distance_to_battery - Solution.distance_calc(Solution, house, temp_batteries[i + counter])
                                    score2 = swap_house.distance_to_battery - Solution.distance_calc(Solution, swap_house, battery)
                                    score = score1 + score2
                                    # print("Score: ", score)

                                    if score > 0:
                                        possible_swaps.append([house, swap_house, score])

                # BREAK IF NO SWAPS POSSIBLE
                if len(possible_swaps) == 0:
                    break

                # sort possible swaps --> best swap?
                def takeThird(elem):
                    return elem[2]

                possible_swaps.sort(key=takeThird, reverse=True)
                for swap in possible_swaps:

                    house1 = swap[0]
                    # print("HOUSE1 ID: ", house1.id)
                    bat1 = house1.connected
                    # print("B1: ", b1.id
                    house2 = swap[1]
                    bat2 = house2.connected

                    # battery_house1 = house1.connected
                    # distance = (abs(battery_house1.x - house1.x) + abs(battery_house1.y - house1.y))
                    # print("DISTANCE BEFORE: ", distance)

                    # swap
                    bat1.remove(house1)
                    bat2.remove(house2)

                    # connect
                    bat1.add(house2)
                    house2.connect(bat1)

                    bat2.add(house1)
                    house1.connect(bat2)

                    # battery_house1 = house1.connected
                    # distance = (abs(battery_house1.x - house1.x) + abs(battery_house1.y - house1.y))
                    # print("DISTANCE AFTER: ", distance)

                    # replace houses in self.houses with swapped houses
                    temp_houses = sorted(temp_houses, key=lambda house: house.id)
                    temp_houses[house1.id] = house1
                    temp_houses[house2.id] = house2

                    # start over after swap
                    break

                # Save solution & append total costs to self.results
                oplossing = Solution(temp_houses, temp_batteries)
                self.results.append([oplossing.calculate_costs()])

            # EINDE HILL CLIMBER
            eind_oplossing = Solution(temp_houses, temp_batteries)
            self.multi_results.append([eind_oplossing.calculate_costs()])

        # change when done
        self.batteries = copy.deepcopy(temp_batteries)
        self.houses = copy.deepcopy(temp_houses)
