import sys

sys.path.append('Code')
from load import Load

sys.path.append('Code/algoritmes')
from greedy import Greedy

sys.path.append('Code/classes')
from helper import Helper

if __name__ == "__main__":
    load = Load("wijk1", "wijk1") # wijk1, wijk2, wijk3
    greedy = Greedy(load.houses, load.batteries, "priority") # output, distance, priority
    Helper.costs(Helper, greedy.batteries, greedy.houses)
