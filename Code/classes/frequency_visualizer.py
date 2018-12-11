import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append('../classes')

from house import House
from battery import Battery


class Frequency_visualizer():

    def __init__(self, results, visualtype, title):
        self.results_csv = self.write_csv(results, title)
        self.check_visual_type(visualtype)

    def write_csv(self, results, titel):
        '''Multi iterations'''

        with open("resultaten/" + titel + ".csv", mode = 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["iteration", "costs"])

            for index, result in enumerate(results):
                csv_writer.writerow([index, result])

        return ("resultaten/" + titel + ".csv")

    def check_visual_type(self, visualtype):
        '''Check for visual type and call right method'''

        if visualtype == "result_frequency_table":
            self.create_frequency_visual()
        else:
            pass

    def create_frequency_visual(self):
        df = pd.read_csv(self.results_csv)

        sns.set()

        sns.set(font_scale=0.5)
        plot = sns.distplot(df.costs, kde=False, bins=14)

        plot.set_title("Cost frequencies after Greedy priority sort and 1000 runs of HillClimber afterwards")
        # plot.set_xticks(list(range(50000, 70000, 1000)))
        # plot.set_yticks(list(range(0, 20, 2)))
        plot.autoscale(enable=True, axis='both', tight=False)

        plot.set(xlabel='costs', ylabel='frequency')
        plot.grid(False)

        plt.show()

    def make_my_day():
        readCsv = pd.read_csv("resultaten/Simulated_annealing.csv")
        sns.set_color_codes("dark")

        plot = sns.barplot(x="number", y="costs", data=readCsv, palette="RdBu")
        plot.set_title("Simulated_annealing barplot graph")
        plot.set(xlabel='X as', ylabel='Y as')
        #plot.set_xticks(np.arange(1,500, step=10))

        plt.show()

    def make_my_day2():
        readCsv = pd.read_csv("resultaten/cheat.csv")
        sns.set_color_codes("dark")

        plot = sns.barplot(x="algorithm", y="costs", data=readCsv, order=["Lowerbound", "Output", "Distance" ,"Priority", "Output+HC", "Distance+HC", "Priority+HC", "Output+SA", "Distance+SA", "Priority+SA", "Upperbound"], palette="GnBu_d")
        plot.set_title("Algorithm Analyse")
        plot.set(xlabel='Algoritmes', ylabel='Kosten')
        #plot.set_xticks(np.arange(1,500, step=10))

        plt.show()
