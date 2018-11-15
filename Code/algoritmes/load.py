import sys
sys.path.append('../classes')

from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.house = self.load_houses(f"../../data/Huizen&Batterijen/{huis}_huizen.csv")
        self.battery = self.load_batteries(f"../../data/Huizen&Batterijen/{batterij}_batterijen.txt")


    def load_houses(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_houses = []
            self.houses = []

            for i in content:
                i = i.strip()
                innitial_houses.append(i.split(","))

            # load houses into list (id, x, y, max_amp)
            for i, house in enumerate(innitial_houses[1:]):
                self.houses.append(House(i, int(house[0]), int(house[1]), float(house[2])))


    def load_batteries(self, filename):
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_batteries = []
            self.batteries = []

            for i in content:

                i = i.replace("\t", " ")
                i = i.replace(",", "")
                i = i.replace("[", "")
                i = i.replace("]", "")

                i = i.strip('\n')
                innitial_batteries.append(i.split())

            for i, battery in enumerate(innitial_batteries[1:]):
                self.batteries.append(Battery(i, int(battery[0]), int(battery[1]), float(battery[2])))


    def distance(self, house, batteries):
        '''Calculate distance between given house and each battery'''

        for battery in batteries:
            battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

        return batteries

    def connect_houses(self):

        # get priority value for each house
        for house in self.houses:

            # Get distance and sort batteries based on distance to current house
            self.batteries = self.distance(house, self.batteries)
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)
            house.prioritize(self.batteries)

            # Priority Value
            first_distance = self.batteries[0].distance
            second_distance = self.batteries[1].distance
            house.priority_value(first_distance, second_distance)

        # sort houses based on priority value
        self.houses = sorted(self.houses, key=lambda house: house.pv, reverse=True)

        for house in self.houses:

            # Sorteer opnieuw voor huis
            self.batteries = self.distance(house, self.batteries)
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(battery.distance)
                    break;



            ''''
            # TEST: volgorde batterijen per huis
            print("House ID: " str(house.id))
            for battery in house.distance:
                print(battery.id)
            '''

            # Connect house to nearest battery with enough available capacity
            for battery in self.batteries:
                if not house.connected and battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(battery.distance)
                    break

                    '''
                    TEST: cable_costs (battery_distance * 9)
                    print(house.connected)
                    print(battery.distance)
                    print(house.costs)
                    '''

                    '''
                    # TEST: afstand batterij - huis + gekozen batterij
                    print("HOUSE ID: " + str(house.id))
                    print("House coördinates: " + str(house.x) + "," + str(house.y))
                    print("Battery ID: " + str(battery.id))
                    print("Battery coördinates: " + str(battery.x) + "," + str(battery.y))
                    print("Distance house-battery: " + str(battery.distance))
                    print()
                    '''



        '''
        # TEST: alle batterijen aangesloten?
        # Batterijen totaal = 7 535
        # Huizen totaal = 7 500
        current_usage = 0
        for battery in self.batteries:
            print("ID:" + str(battery.id))
            print("Current usage: " + str(battery.current_usage))
            print("Available: " + str(battery.check_amp()))
            print("Connected ID's" + str(battery.connected))
            current_usage += battery.current_usage
        print("Total battery usage: " + str(current_usage))
        '''



        # TEST: overzicht huizen gesorteert op basis van kosten
        # Sort houses by costs
        self.houses = sorted(self.houses, key=lambda house: house.costs, reverse=True)
        for house in self.houses:
            print("ID: " + str(house.id))
            print("House output: " + str(house.amp))
            print("Costs: " + str(house.costs))
            print()



    def costs(self):
        # Battery battery battery costs
        battery_costs = 0
        for battery in self.batteries:
            battery_costs += battery.cost

        # Cable cable costs
        cable_costs = 0
        for house in self.houses:
            cable_costs += house.costs
            # print(cable_costs)

        # Total costs
        total_costs = battery_costs + cable_costs


        # TEST: costs
        print("Battery costs: " + str(battery_costs))
        print("Cable costs: " + str(cable_costs))
        print("Total costs: " + str(total_costs))


if __name__ == "__main__":
    load = Load("wijk2", "wijk2")
    load.connect_houses()
    load.costs()
