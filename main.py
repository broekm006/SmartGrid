import sys

sys.path.append('Code')
from load import Load
from frequency_visualizer import Frequency_visualizer
from grid_visualizer import Grid_visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber_update import Hill_climber
from hill_climber_BC import Hill_climber_BC
from k_means2 import K_means2
from random_connect import Random_connect
#from simulated_annealing import Simulated_annealing

sys.path.append('Code/classes')
from helper import Helper


if __name__ == "__main__":
    load = Load("wijk1", "wijk1")

    # Default Bounds
    # Helper.bounds(Helper, load.batteries, load.houses)

    # Greedy
    greedy = Greedy(load.houses, load.batteries, "priority") # "output", "distance", "priority"

    # random
    # random = Random_connect(load.houses, load.batteries)

    # Hill CLimber
    hill_climber = Hill_climber(greedy.houses, greedy.batteries, 1000, 1000)

    # Hill Climber Best Choice
    # hill_climber_BC = Hill_climber_BC(greedy.houses, greedy.batteries, 100)

    # Simulated Annealing
    #sim = Simulated_annealing(greedy.houses, greedy.batteries, 100)

    # K Means
    # k_means = K_means2(hill_climber_BC.houses, hill_climber_BC.batteries, "distance", "") # "random" or "" for innitial battery location


    # Bounds + Costs
    # Helper.bounds(Helper, greedy.batteries, greedy.houses)
    # Helper.costs(Helper, greedy.batteries, greedy.houses)
    # Helper.battery_info(Helper, k_means.batteries)
    # Helper.sort_houses(Helper, greedy.houses)

    # Grid visualisatie, specify houses, batteries and visual type
    #grid_visualisatie = Grid_visualizer(greedy.houses, greedy.batteries, "gridview")

<<<<<<< HEAD
    # HillClimber visualisatie
    # visualizer.csv_HillClimber(sim.multi_results, "MultiSA_PRIORITY_WIJK1") # HillClimber_BC1 / HillClimber_random1
=======
    # frequency visualisatie, meegeven resultaten, type visualisatie en titel
    frequency_table = Frequency_visualizer(hill_climber.multi_results, "result_frequency_table", "100 iterations HC") # HillClimber_BC1 / HillClimber_random1
>>>>>>> 118c31502f712657038646bd4b9fb4177203a84f
