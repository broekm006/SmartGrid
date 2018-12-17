import copy, math, random
# import hcluster
import numpy as np
from battery import Battery
from greedy import Greedy
from grid_visualizer import Grid_visualizer
from k_means2 import K_means2
from helper import Helper
from solution import Solution
from sort import Sort

class Cluster_merge(object):

    def __init__(self, houses):
        self.houses = houses
        self.costs = float('Inf')
        self.counter = 0
        self.innitialize()
        self.merge()

    def innitialize(self):
        self.batteries = []

        # innitialize batteries
        for i, house in enumerate(self.houses):
            battery = Battery(i, house.x, house.y, 450)
            battery.costs = 900 # Later via Battery()?
            self.batteries.append(battery)

    def linkage(self, battery1, battery2):

        distance = abs(battery1.x - battery2.x) + abs(battery1.y - battery2.y)
        return distance

    def single_linkage(self, battery1, battery2):
        ''' Distance between the closest houses of the two batteries'''

        shortest_distance = float('inf')
        for house1 in battery1.connected:
            for house2 in battery2.connected:
                distance = Solution.distance_calc(Solution, house1, house2)

                if distance < shortest_distance:
                    shortest_distance = distance

        return shortest_distance

    def merge(self):
        # single linkage: distance between the closest members of the two clusters
        # complete linkage: distance between the members farthest apart
        # average linkage: distances between all pairs and averages of all of these distances
        # minmax: ?

        # Make distance dictionary where key is (b1, b2) and value is distance
        solutions = []
        count = 0
        # Continue while merges possible
        distance_dict = {}
        distance_dict[0] = 0

        while len(distance_dict) > 0:

            # Continue while merges possible
            distance_dict = {}
            distance_dict[0] = 0

            # k_means = K_means2(self.houses, self.batteries, "priority", "0")
            k_means = K_means2(self.houses, self.batteries, "output", "0")
            self.houses = copy.deepcopy(k_means.houses)
            self.batteries = copy.deepcopy(k_means.batteries)

            # calculate costs
            count += 1
            # print("Count: ", count)
            solution = Solution(self.houses, self.batteries)
            solutions.append(solution)

            # total_cost = solution.calculate_costs()
            # print("Total costs: ", total_cost)
            # print()

            # Make distance dictionary where key is (b1, b2) and value is distance
            distance_dict = {}
            for i, battery1 in enumerate(self.batteries):
                for battery2 in self.batteries[i+1:]:
                    if battery1.current_usage + battery2.current_usage > 1800:
                        print("Merge not possible")
                        break
                    else:
                        # DISTANCE
                        distance = self.linkage(battery1, battery2)
                        distance = abs(battery1.x - battery2.x) + abs(battery1.y - battery2.y)
                        distance_dict[(battery1, battery2)] = distance

            for distance in distance_dict:
                # Get two batteries with smallest distance
                smallest_distance = min(distance_dict, key=lambda x: distance_dict.get(x))
                battery_1 = smallest_distance[0]
                battery_2 = smallest_distance[1]

                # Determine coordinates merged battery
                mean_x = int((battery_1.x + battery_2.x)/2)
                mean_y = int((battery_1.y + battery_2.y)/2)

                # Determine merged battery_size & cost
                merged_usage = battery_1.current_usage + battery_2.current_usage
                if (merged_usage < 450):
                    capacity = 450
                    cost = 900
                elif (merged_usage < 900):
                    capacity = 900
                    cost = 1350
                elif (merged_usage < 1800):
                    capacity = 1800
                    cost = 1800

                # Create new battery (merged)
                merged_battery = Battery(battery_1.id, mean_x, mean_y, capacity)
                merged_battery.cost = cost

                # Disconnect houses from batteries
                for battery in self.batteries:
                    for house in battery.connected:
                        battery.remove(house)

                # Add & remove old batteries
                self.batteries.remove(battery_1)
                self.batteries.remove(battery_2)
                self.batteries.append(merged_battery)
                break


        greedy = Greedy(self.houses, self.batteries,"output")

        for battery in greedy.batteries:
            print("ID: ", battery.id)
            print("Capacity: ", battery.max_amp)
            print("Current usage", battery.current_usage)
            print("Cost: ", battery.cost)
            print("Connected", *battery.connected)
            print()

        solution = Solution(greedy.houses, greedy.batteries)
        total_cost = solution.calculate_costs(count)
        # print("Total costs: ", total_cost)

        helper = Helper()
        helper.bounds(greedy.batteries, greedy.houses)

        cost = float('inf')
        for i, sol in enumerate(solutions):
            print("Cost solution " + str(i) + ": " + str(sol.calculate_costs2()))
            print("Cheapest so far: " + str(cost))
            if sol.calculate_costs2() < cost:
                print("goedkoper")
                print()
                cost = sol.calculate_costs2()
                best_solution = sol

        for i, battery in enumerate(best_solution.batteries):
            connections = []
            connection_count = 0
            battery.id = i
            for house in battery.connected:
                connections.append(house.id)
                connection_count += 1


            print("ID: ", battery.id)
            print("Max: ", battery.max_amp)
            print("Cost: ", battery.cost)
            print("Coordinates: (" + str(battery.x) + "," + str(battery.y) + ")")
            print("Current usage: ", battery.current_usage)
            print("Connected", connections)
            print("Connection count: ", connection_count)
            print()

        best_solution.calculate_costs2()
        helper = Helper()
        helper.bounds(best_solution.batteries, best_solution.houses)

        self.houses = copy.deepcopy(best_solution.houses)
        self.batteries = copy.deepcopy(best_solution.batteries)
