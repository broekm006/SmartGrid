import sys
sys.path.append('Code/classes')

from house import House
from battery import Battery

class Load():

    def __init__(self, huis, batterij):
        self.house = self.load_houses(f"data/Huizen&Batterijen/{huis}_huizen.csv")
        self.battery = self.load_batteries(f"data/Huizen&Batterijen/{batterij}_batterijen.txt")


    def load_houses(self, filename):
        ''' Load houses file to pyhton '''
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_houses = []
            self.houses = []

            # loop through contents and seperate the values
            for i in content:
                i = i.strip()
                innitial_houses.append(i.split(","))

            # load houses into list (id, x, y, amp)
            for i, house in enumerate(innitial_houses[1:]):
                self.houses.append(House(i, int(house[0]), int(house[1]), float(house[2])))

            return self.houses

    def load_batteries(self, filename):
        ''' Load batteries file to python '''
        with open(filename, "r") as f:
            content = f.readlines()

            innitial_batteries = []
            self.batteries = []

            # loop through and replace all the "bad" characters with nothing. After that split values
            for i in content:
                i = i.replace("\t", " ")
                i = i.replace(",", "")
                i = i.replace("[", "")
                i = i.replace("]", "")

                i = i.strip('\n')
                innitial_batteries.append(i.split())

            # load batteries into list (id, x, y, max_amp)
            for i, battery in enumerate(innitial_batteries[1:]):
                self.batteries.append(Battery(i, int(battery[0]), int(battery[1]), float(battery[2])))

            return self.batteries
