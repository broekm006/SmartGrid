import sys
import argparse

sys.path.append('Code')
from load import Load
from frequency_visualizer import Frequency_visualizer
from grid_visualizer import Grid_visualizer

sys.path.append('Code/algoritmes')
from greedy import Greedy
from hill_climber import Hill_climber
from k_means2 import K_means2
from random_connect import Random_connect
from test_merge import Cluster_merge
from simulated_annealing import Simulated_annealing

sys.path.append('Code/classes')
from helper import Helper
from solution import Solution

def what_to_run(self, wijk, algo, sec_algo, NoT, vis):
    ''' Kijkt welke variant van greedy'''
    wijk = "wijk" + wijk
    load = Load(wijk, wijk)

    print()
    print("INNITIAL UPPER & LOWERBOUND (before k-means and/or HAC)")
    print()
    print(wijk)
    Solution.bounds(Solution, load.batteries, load.houses)


    if algo == "random":
        random = Random_connect(load.houses, load.batteries)
    elif algo == "greedy_output":
        greedy = Greedy(load.houses, load.batteries, "output")
    elif algo == "greedy_distance":
        greedy = Greedy(load.houses, load.batteries, "distance")
    elif algo == "greedy_priority":
        greedy = Greedy(load.houses, load.batteries, "priority")
    elif algo == "k_means_output":
        k_means = K_means2(load.houses, load.batteries, "output", "")
        k_means.results()
    elif algo == "k_means_distance":
        k_means = K_means2(load.houses, load.batteries, "distance", "")
        k_means.results()
    elif algo == "k_means_priority":
        k_means = K_means2(load.houses, load.batteries, "priority", "")
        k_means.results()
    elif algo == "HAC":
        splitter = Cluster_merge(load.houses)


    else:
        print("Error running algorithm")

    if sec_algo == "hill_climber" and algo == "greedy_output" or sec_algo == "hill_climber" and algo == "greedy_distance" or sec_algo == "hill_climber"  and algo == "greedy_priority":
        hill_climber = Hill_climber(greedy.houses, greedy.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber.houses, hill_climber.batteries, "gridview", "Greedy + Hill Climber")
    elif sec_algo == "hill_climber" and algo == "k_means_output" or sec_algo == "hill_climber" and algo == "k_means_distance" or sec_algo == "hill_climber" and algo == "k_means_priority":
        hill_climber = Hill_climber(k_means.houses, k_means.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(hill_climber.houses, hill_climber.batteries, "gridview", "K-Means + Hill Climber")
    elif sec_algo == "simulated_annealing" and algo == "greedy_output" or sec_algo == "simulated_annealing" and algo == "greedy_distance" or sec_algo == "simulated_annealing" and algo == "greedy_priority":
        sim = Simulated_annealing(greedy.houses, greedy.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(sim.houses, sim.batteries, "gridview", "Greedy + Simulated Annealing")
    elif sec_algo == "simulated_annealing" and algo == "k_means_output" or sec_algo == "simulated_annealing" and algo == "k_means_distance" or sec_algo == "simulated_annealing" and algo == "k_means_priority":
        sim = Simulated_annealing(k_means.houses, k_means.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(sim.houses, sim.batteries, "gridview", "K-Means + Simulated Annealing")
    elif sec_algo == "simulated_annealing" and algo == "HAC":
        sim = Simulated_annealing(splitter.houses, splitter.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(splitter.houses, splitter.batteries, "gridview", "Hierarchical Agglomerative Clustering")
    elif sec_algo == "hill_climber" and algo == "HAC":
        sim = Hill_climber(splitter.houses, splitter.batteries, NoT, 1)
        if vis == 'True':
            grid_visualisatie = Grid_visualizer(splitter.houses, splitter.batteries, "gridview", "Hierarchical Agglomerative Clustering")
    elif sec_algo == "escape":
        pass

    else:
        print("Error running secondary algorithm")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py', usage='%(prog)s [-h] [-a [greedy_output, greedy_distance, greedy_priority, k_means_output, k_means_distance, k_means_priority, HAC]] [-b [hill_climber, simulated_annealing, brute_force]] [-i [iterations]] [-v [Y]]')
    parser.add_argument('-w', '--wijk', type=str, choices=['1', '2', '3'], required=True, help='Choose the grid you would like to run the algorithm(s) on.')
    parser.add_argument('-a', '--algorithm', type=str, choices=['greedy_output', 'greedy_distance', 'greedy_priority','k_means_output', 'k_means_distance', 'k_means_priority', 'HAC'], required=True, help='Choose the primary algorithm you would like to run.')
    parser.add_argument('-b', '--secondary_algorithm', choices=['hill_climber','simulated_annealing'], type=str, required=False, default="simulated_annealing", help='Choose the secondary algorithm you would like to run. If not specified, Simulated Annealing is ran.')
    parser.add_argument('-i','--iterations', type=int, help='Enter the number of times you wish to run the selected algorithmself.', required=False, default=1)
    parser.add_argument('-v','--visualizer', choices=['True','False'], type=str, help='Enter True if you want to see a visual representation of the algorithm and a print of the battery info.', required=False, default='False')

    args = parser.parse_args()
    what_to_run(what_to_run, args.wijk, args.algorithm, args.secondary_algorithm, args.iterations, args.visualizer)

# algo == type of algorithm
# sec_algo == type of iterative algorithm to combine with initial algorithm
# NoT == Number of Times to run the algorithm(s)
# vis == Whether we run a visual or not
