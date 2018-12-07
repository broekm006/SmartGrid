import sys

sys.path.append('Code')
from load import Load
from visualizer import Visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2
from random_connect import Random_connect
from simulated_annealing import Simulated_annealing

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    # Default Bounds
    # Helper.bounds(Helper, load.batteries, load.houses)

    # Greedy
    greedy = Greedy(load.houses, load.batteries, "distance") # "output", "distance", "priority"

    # random
    # random = Random_connect(load.houses, load.batteries)

    # Hill CLimber
    hill_climber = Hill_climber(greedy.houses, greedy.batteries, 1000, 100)

    # Hill Climber Best Choice
    # hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries, 100)

    # Simulated Annealing
    # sim = Simulated_annealing(greedy.houses, greedy .batteries, 10)
    # sim.simulatie_V2()

    # K Means
    # k_means = K_means2(hill_climber_BC.houses, hill_climber_BC.batteries, "distance", "") # "random" or "" for innitial battery location


    # Bounds + Costs
    # Helper.bounds(Helper, greedy.batteries, greedy.houses)
    # Helper.costs(Helper, greedy.batteries, greedy.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    # Helper.sort_houses(Helper, greedy.houses)

    # Visualisatie
    visualizer = Visualizer(hill_climber.houses, hill_climber.batteries)

    # HillClimber visualisatie
    visualizer.csv_HillClimber(hill_climber.multi_results, "MultiHillClimberRandom") # HillClimber_BC1 / HillClimber_random1
