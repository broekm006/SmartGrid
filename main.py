import sys

sys.path.append('Code')
from load import Load

sys.path.append('Code/algoritmes')
from greedy import Greedy

sys.path.append('Code/classes')
from helper import Helper

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
    greedy = Greedy(load.houses, load.batteries, "output") # "output","distance", "priority"
    Helper.costs(Helper, greedy.batteries, greedy.houses)
