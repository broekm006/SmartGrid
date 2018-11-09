import sys, os
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
                self.houses.append(i.split(","))

            # load houses into list (x, y, max_amp)
            for i, house in enumerate(innitial_houses[1:]):
                self.houses.append(House(i, int(house[0]), int(house[1]), float(house[2])))
                print(house)

            print()
            print()

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

                    # print(battery)

    def connect_houses():
        # connect & keep track of current battery usage
        for house in self.houses:
            for battery in self.batteries:
                if battery.check_amp() > house.amp:
                    print(battery)
                    battery.connect(house.id)
                    battery.add(house.amp)
                    house.connect(battery.id)
                    break



if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
