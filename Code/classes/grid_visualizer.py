import csv, sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sys.path.append('../classes')

from house import House
from battery import Battery


class Grid_visualizer():

    def __init__(self, houses, batteries, visualtype):
        self.batteries = batteries
        self.visualdata = self.write_csv(houses, batteries)
        self.check_visual_type(visualtype)



    def check_visual_type(self, visualtype):
        '''Check for visual type and call right method'''
        if visualtype == "gridview":
            create_visualization(self)
        else:
            pass


    def write_csv(self, houses, batteries):
        '''Create a new .CSV file based on the results + name of the algorithm'''
        with open("houses.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["type", "id", "x", "y", "connected_bat"])
            for house in houses:
                house_list = []
                house_list.append("house")
                house_list.append(house.id)
                house_list.append(house.x)
                house_list.append(house.y)
                if house.connected != False:
                    house_list.append(house.connected.id)
                else:
                    house_list.append("not connected")

                csv_writer.writerow(house_list)

            for battery in batteries:
                battery_list = []
                battery_list.append("battery")
                battery_list.append(battery.id)
                battery_list.append(battery.x)
                battery_list.append(battery.y)
                battery_list.append(battery.id)

                csv_writer.writerow(battery_list)


        with open("batteries.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csv_writer.writerow(["battery_id", "battery_x", "battery_y"])
            for battery in batteries:
                battery_list = []
                battery_list.append(battery.id)
                battery_list.append(battery.x)
                battery_list.append(battery.y)

                csv_writer.writerow(battery_list)

        return "houses.csv"


def create_visualization(self):
    '''Use previously created .CSV file to create a visual representation of the grid + how everything is connected '''
    df = pd.read_csv(self.visualdata)

    sns.set_color_codes("dark")
<<<<<<< HEAD
    #sns.palplot(sns.color_palette())
    plot = sns.scatterplot(x="x", y="y", hue="connected_bat", data=df, ci=None, style="type", palette=sns.color_palette("Paired", n_colors = len(self.batteries)))
=======
    plot = sns.scatterplot(x="x", y="y", hue="connected_bat", data=df, ci=None, style="type", palette=["C0", "C1", "C2", "C3", "C4"])
>>>>>>> 93b363af56e4b91f77635d7c8947de2681429cd3

    plot.set_title("Wijk 1: K-Means with Simulated Annealing")
    plot.legend_.remove()
    plot.set(xlabel='X coordinates', ylabel='Y coordinates')

    plt.show()
