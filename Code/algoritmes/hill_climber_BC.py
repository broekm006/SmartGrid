#done
# kies random battery
# kies random huis

#not done
# swap > check distance
# if beter > keep
# else > swap back
import copy
import random
from solution import Solution

class Hill_climber_BC(object):

    def __init__(self, houses, batteries):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)

    def best_choice(self):
        count = 0

        while True:
            count += 1
            print("COUNT: ", count)

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

            # BREAK IF NO SWAPS POSSIBLE
            if len(possible_swaps) == 0:
                break

            # sort possible swaps --> best swap?
            def takeThird(elem):
                return elem[2]

            possible_swaps.sort(key=takeThird, reverse=True)
            print(possible_swaps)

            for swap in possible_swaps:
                house1 = swap[0]
                print("HOUSE1 ID: ", house1.id)
                b1 = house1.connected
                print("B1: ", b1.id)
                print(*b1.connected)
                house2 = swap[1]
                b2 = house2.connected

                print("HOUSE 1: ", house1.id)
                print("BATTERY CONNECTED")
                for house in b1.connected:
                    print(house.id)

                # swap
                b1.remove(house1)
                b2.remove(house2)

                b1.add(house2)
                house2.connect(b1)

                b2.add(house1)
                house1.connect(b2)

        # Save solution & append to HC_solution(list)
        solution = Solution(Solution, self.houses, self.batteries)
        solution.hc_solution()
