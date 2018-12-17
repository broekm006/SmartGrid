import copy
from sort import Sort

class Solution(object):

    def __init__(self, houses, batteries):
        self.houses = copy.deepcopy(houses)
        self.batteries = copy.deepcopy(batteries)
        #self.batteries = batteries


    def distance_calc(self, house, battery):
        ''' Calculate distanct house to battery '''
        return abs(battery.y - house.y) + abs(battery.x - house.x)


    def sort_houses(self, houses):
        ''' Checks which house is cheapest & most expensive '''
        sorted_houses = sorted(houses, key=lambda house: house.costs)

        #Expensive
        print("CHEAPEST & MOST EXPENSIVE HOUSE")
        print()
        battery = sorted_houses[0].connected
        print("House ID: ", sorted_houses[0].id)
        print("Output:   ", sorted_houses[0].amp)
        print("Battery:  ", battery.id)
        print("Costs:    ", sorted_houses[0].costs)
        print("Distance: ", sorted_houses[0].distance_to_battery)
        print()

        #Cheapest
        battery2 = sorted_houses[0].connected
        print("House ID: ", sorted_houses[-1].id)
        print("Output:   ", sorted_houses[-1].amp)
        print("Battery:  ", battery2.id)
        print("Costs:    ", sorted_houses[-1].costs)
        print("Distance: ", sorted_houses[-1].distance_to_battery)
        print()
        print()

    # calcuate the costs of the house to battery
    def calculate_costs(self, id):
        ''' Calculate total costs'''

        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.cost

        cable_costs = 0
        for house in self.houses:
            try:
                battery = house.connected
                house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)
                house.costs = house.distance_to_battery * 9
                cable_costs += house.costs
            except:
                print("Huis niet verbonden")
                pass

        # Total costs
        total_costs = battery_costs + cable_costs
        self.costs = total_costs
        self.id = id
        print("ID (", id, ") total costs: (", total_costs, ")")
        return total_costs

    # calcuate the costs of the house to battery
    def calculate_costs2(self):
        ''' Calculate total costs'''

        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.cost

        cable_costs = 0
        for house in self.houses:
            try:
                battery = house.connected
                house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)
                house.costs = house.distance_to_battery * 9
                cable_costs += house.costs
            except:
                print("Huis niet verbonden")
                pass

        # Total costs
        total_costs = battery_costs + cable_costs
        return total_costs


    # calculate the total cable costs for all houses
    def houses_costs(self, batteries, houses):
        ''' Calculate to total costs for houses '''
        cable_costs = 0
        for house in houses:
            cable_costs += house.costs

        return cable_costs

    def bounds(self, batteries, houses):
        ''' Upper- and lowerbounds for costs for given houses & batteries'''

        # solution class + update house.priority_list
        initial_solution = Solution(houses, batteries)
        Sort.priority_value(Sort, houses, batteries)

        lower = 0
        upper = 0
        for house in houses:
            b_close = house.priority_list[0]
            lower += initial_solution.distance_calc(house, b_close)

            b_far = house.priority_list[4]
            upper += initial_solution.distance_calc(house, b_far)

        battery_costs = 0
        for battery in batteries:
            battery_costs += battery.cost

        lowerbound = lower * 9 + battery_costs
        upperbound = upper * 9 + battery_costs

        print("LOWERBOUND: " , lowerbound)
        print("UPPERBOUND: " , upperbound)
        print()
