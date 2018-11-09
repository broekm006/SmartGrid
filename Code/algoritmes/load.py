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


    def connect_houses(self):

        # Sort houses
        self.houses = sorted(self.houses, key=lambda house: house.amp, reverse=True)

        # connect each house to a battery (keep track of usage, max etc.)
        for house in self.houses[1:]:
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    battery.connect(house.id)
                    battery.add(house.amp)
                    house.connect(battery.id)
                    print(battery)
                    print()
                    print(house)
                    break


        # TEST
        current_usage = 0

        for battery in self.batteries:
            print("ID:" + str(battery.id))
            print("Current usage: " + str(battery.current_usage))
            print("Available: " + str(battery.check_amp()))
            print("Connected ID's" + str(battery.connected))
            current_usage += battery.current_usage

        print("Total" + str(current_usage))


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
    load.connect_houses()
