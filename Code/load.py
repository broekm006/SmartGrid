import sys
sys.path.append('Code/classes')

from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.house = self.load_houses(f"data/Huizen&Batterijen/{huis}_huizen.csv")
        self.battery = self.load_batteries(f"data/Huizen&Batterijen/{batterij}_batterijen.txt")


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

            return self.houses

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

            return self.batteries

    #
    def distance(self, house, batteries):
        '''Calculate distance between given house and each battery'''

        for battery in batteries:
            battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

        return batteries

    #
    def connect_houses(self):

        # Sort houses by max output
        self.houses = sorted(self.houses, key=lambda house: house.amp, reverse=True)

        # sort batteries based on distance to house
        for house in self.houses:

            # Get distance from current house to each battery
            self.batteries = self.distance(house, self.batteries)

            # Sort batteries based on distance to current house
            self.batteries = sorted(self.batteries, key=lambda battery: battery.distance)

            # adds sorted list to house.distance (house.distance == self.batteries)
            house.nearest(self.batteries)


            # Connect house to nearest battery with enough available capacity
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    house.connect(battery)

                    # Update battery usage & calculate cable costs
                    battery.add(house.amp)
                    house.cable_costs(battery.distance)



                    break

        # Sort houses by costs
        self.houses = sorted(self.houses, key=lambda house: house.costs, reverse=True)

        for house in self.houses:
            print("ID: " + str(house.id))
            print("House output: " + str(house.amp))
            print("Costs: " + str(house.costs))
            print()