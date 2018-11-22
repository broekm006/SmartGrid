from solution import Solution
from sort import Sort

class Helper(object):

    def costs(self, batteries, houses):
        ''' Calculate total costs'''

        battery_costs = 0
        for battery in batteries:
            battery_costs += battery.cost

        # # Cable cable costs
        # cable_costs = 0
        # for house in houses:
        #     cable_costs += house.costs

        cable_costs = 0
        for house in houses:
            battery = house.connected
            house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)
            house.costs = house.distance_to_battery * 9
            cable_costs += house.costs

        # Total costs
        total_costs = battery_costs + cable_costs

        '''
        # TEST: print houses sorted by costs
        houses = sorted(houses, key=lambda house: house.costs, reverse=True)
        for house in houses:
            print("House id: " + str(house.id))
            print("House output: " + str(house.amp))
            print("House costs: " + str(house.costs))
            print()
        '''

        # TEST: costs
        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))

    def houses_costs(self, batteries, houses):
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

        lowerbound = lower * 9 + (batteries[0].cost * len(batteries))
        upperbound = upper * 9 + (batteries[0].cost * len(batteries))

        print("LOWERBOUND: " , lowerbound)
        print("UPPERBOUND: " , upperbound)
