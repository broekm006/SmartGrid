class Helper(object):

    def costs(self, batteries, houses):
        ''' Calculate total costs'''

        battery_costs = 0
        for battery in batteries:
            battery_costs += battery.cost

        # Cable cable costs
        cable_costs = 0
        for house in houses:
            cable_costs += house.costs

        # Total costs
        total_costs = battery_costs + cable_costs

        # TEST: print houses sorted by costs
        houses = sorted(houses, key=lambda house: house.costs, reverse=True)
        for house in houses:
            print("House id: " + str(house.id))
            print("House output: " + str(house.amp))
            print("House costs: " + str(house.costs))
            print()

        # TEST: costs
        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))
