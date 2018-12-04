import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_test import Hill_climber_test
from k_means2 import K_means2

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk3", "wijk3")

    Helper.bounds(Helper, load.batteries, load.houses)
    # greedy = Greedy(load.houses, load.batteries, "output") # "output", "distance", "priority"

    k_means = K_means2(load.houses, load.batteries)
    # hill_climber = Hill_climber_test(k_means.houses, k_means.batteries, 500)
    # hill_climber.best_choice()
    # hill_climber.ice_climbers()

    # Helper.costs(Helper, k_means.batteries, k_means.houses)
    # Helper.sort_houses(Helper, k_means.houses)

    # Visualizer(hill_climber.houses, hill_climber.batteries)
    Visualizer(k_means2.houses, k_means2.batteries)
