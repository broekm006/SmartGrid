class Helper(object):

    #
    def costs(self, batteries, houses):
        # Battery battery battery costs
        battery_costs = 0
        for battery in batteries:
            battery_costs += battery.cost

        # Cable cable costs
        cable_costs = 0
        for house in houses:
            cable_costs += house.costs
            # print(cable_costs)

        # Total costs
        total_costs = battery_costs + cable_costs


        # TEST: costs

        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))
        
