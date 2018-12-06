import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    Helper.bounds(Helper, load.batteries, load.houses)
    greedy = Greedy(load.houses, load.batteries, "priority") # "output", "distance", "priority"

    hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries)
    hill_climber_BC.best_choice()
    # k_means = K_means2(load.houses, load.batteries, "priority", "random") # "random" or "" for innitial battery location

    # hill_climber = Hill_climber_test(k_means.houses, k_means.batteries, 500)
    # hill_climber.ice_climbers()

    Helper.costs(Helper, hill_climber_BC.batteries, hill_climber_BC.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    Helper.bounds(Helper, hill_climber_BC.batteries, hill_climber_BC.houses)
    # Helper.sort_houses(Helper, greedy.houses)

    Visualizer(hill_climber_BC.houses, hill_climber_BC.batteries)
