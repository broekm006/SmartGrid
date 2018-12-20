import sys, copy
sys.path.append('Code/algoritmes')

from sort import Sort
from swap import Swap
from helper import Helper
from solution import Solution

from frequency_visualizer import Frequency_visualizer

class Greedy(object):

    def __init__(self, houses, batteries, variant):
        self.houses = houses
        self.batteries = batteries
        self.variant = self.type(variant)

    def type(self, type):
        ''' Checks which version of greedy will be used'''

        if type == "output":
            self.output()
        elif type == "distance":
            self.distance()
        elif type == "priority":
            self.pv()
        else:
            print("Greedy type error")


    def output(self):
        ''' Connect house to nearest battery with available capacity'''

        self.results = []
        for i in range(1000):

            temp_houses = copy.deepcopy(self.houses)
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses= Sort.max_output(Sort, temp_houses)

            for house in temp_houses:
                for battery in temp_batteries:
                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                temp_batteries = sorted(temp_batteries, key=lambda battery: battery.distance)

                for battery in temp_batteries:
                    if battery.check_amp() > house.amp:
                        house.connect(battery)

                        # update battery usage and connected list
                        battery.add(house)

                        # cable costs
                        battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)
                        house.cable_costs(battery.distance)

                        break;

            # HILL CLIMBER SWAP
            Swap.swap_hill_climber(Swap, temp_houses, temp_batteries)

            # Save solution
            solution = Solution(temp_houses, temp_batteries)
            solution.calculate_costs(i)
            self.results.append([solution.id, solution.costs])
            print("ID: " + str(solution.id) + ", COST: " + str(solution.costs))

        self.houses = copy.deepcopy(temp_houses)
        self.batteries = copy.deepcopy(temp_batteries)
        Frequency_visualizer.write_csv(Frequency_visualizer, self.results, "Greedy_output1000")



    def distance(self):
        ''' Connect house to nearest battery with available capacity'''

        self.results = []
        for i in range(1000):

            temp_houses = copy.deepcopy(self.houses)
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses= Sort.max_output(Sort, temp_houses)

            for battery in temp_batteries:

                # sorts houses based on distance to current battery
                temp_houses = Sort.distance(Sort, temp_houses, battery)

                # connect battery to nearest house that isn't connected
                for house in temp_houses:
                    if battery.check_amp() > house.amp and not house.connection:

                        # distance
                        distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                        # Update battery usage & cable costs
                        battery.add(house)
                        house.connect(battery)
                        house.cable_costs(distance)

            # HILL CLIMBER SWAP
            Swap.swap_hill_climber(Swap, temp_houses, temp_batteries)

            # Save solution
            solution = Solution(temp_houses, temp_batteries)
            solution.calculate_costs(i)
            self.results.append([solution.id, solution.costs])
            print("ID: " + str(solution.id) + ", COST: " + str(solution.costs))

        self.houses = copy.deepcopy(temp_houses)
        self.batteries = copy.deepcopy(temp_batteries)
        Frequency_visualizer.write_csv(Frequency_visualizer, self.results, "Greedy_distance1000")

    def pv(self):
        ''' Connect house to nearest battery with available capacity'''

        self.results = []
        for i in range(1):

            # sorts houses based on priority value
            temp_houses = copy.deepcopy(self.houses)
            temp_batteries = copy.deepcopy(self.batteries)
            temp_houses = Sort.priority_value(Sort, temp_houses, temp_batteries)

            for house in temp_houses:

                # sorts batteries based on distance from current house --> kan nog apart
                for battery in temp_batteries:

                    battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

                temp_batteries = sorted(temp_batteries, key=lambda battery: battery.distance)

                # connect house to nearest available battery
                for battery in temp_batteries:
                    if battery.check_amp() > house.amp:

                        # Update connections, current usage & cable costs
                        house.connect(battery)
                        battery.add(house)
                        house.cable_costs(battery.distance)
                        break;

            # HILL CLIMBER SWAP
            Swap.swap_hill_climber(Swap, temp_houses, temp_batteries)

            # Swap.check(Swap, self.houses, self.batteries)
            solution = Solution(temp_houses, temp_batteries)
            solution.calculate_costs(i)
            self.results.append([solution.id, solution.costs])
            print("ID: " + str(solution.id) + ", COST: " + str(solution.costs))

        self.houses = copy.deepcopy(temp_houses)
        self.batteries = copy.deepcopy(temp_batteries)
        # Frequency_visualizer.write_csv(Frequency_visualizer, self.results, "Greedy_priority1000")
