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
            try:
                battery = house.connected
                house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)
                house.cable_costs(house.distance_to_battery)
                cable_costs += house.costs
            except:
                print("Huis niet verbonden")
                pass

        # Total costs
        total_costs = battery_costs + cable_costs
        return total_costs

        # TEST: costs
        print("COSTS")
        print()
        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))
        print()
        print()

    def houses_costs(self, batteries, houses):
        cable_costs = 0
        for house in houses:
            cable_costs += house.costs

        return cable_costs

    def sort_houses(self, houses):
        sorted_houses = sorted(houses, key=lambda house: house.costs)
        '''
        ALLE HUIZEN
        for house in sorted_houses:
            battery = house.connected
            print("House ID: ", house.id)
            print("Costs:    ", house.costs)
            print("Output:   ", house.amp)
            try:
                print("Battery:  ", battery.id)
            except:
                print("NIET VERBONDEN")
            print()
        '''
        print("CHEAPEST & MOST EXPENSIVE HOUSE")
        print()
        battery = sorted_houses[0].connected
        print("House ID: ", sorted_houses[0].id)
        print("Output:   ", sorted_houses[0].amp)
        print("Battery:  ", battery.id)
        print("Costs:    ", sorted_houses[0].costs)
        print("Distance: ", sorted_houses[0].distance_to_battery)
        print()
        battery2 = sorted_houses[0].connected
        print("House ID: ", sorted_houses[-1].id)
        print("Output:   ", sorted_houses[-1].amp)
        print("Battery:  ", battery2.id)
        print("Costs:    ", sorted_houses[-1].costs)
        print("Distance: ", sorted_houses[-1].distance_to_battery)
        print()
        print()

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
        print()

    def battery_info(self, batteries):
        print("BATTERIES")
        print()
        for battery in batteries:
            print("ID: ", battery.id)
            print("Usage: ", battery.current_usage)
            print("X: ", battery.x)
            print("Y: ", battery.y)
            print("Connected: ", *battery.connected)
            print()
