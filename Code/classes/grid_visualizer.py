import csv
import copy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#import numpy as np
# from celluloid import Camera
# import matplotlib
# matplotlib.use('Agg')


import sys
sys.path.append('../classes')

from house import House
from battery import Battery


class Grid_visualizer():

    def __init__(self, houses, batteries, visualtype, name):
        self.batteries = batteries
        self.visualdata = self.write_csv(houses, batteries)
        self.name = name
        self.printcheck()
        self.check_visual_type(visualtype)



    def check_visual_type(self, visualtype):

        # check for visual type
        if visualtype == "gridview":
            create_visualization(self)
        else:
            # possible animation
            pass


    def write_csv(self, houses, batteries):

        # create house list and...
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

                # write to csv
                csv_writer.writerow(house_list)

            # ...include batteries
            for battery in batteries:
                battery_list = []
                battery_list.append("battery")
                battery_list.append(battery.id)
                battery_list.append(battery.x)
                battery_list.append(battery.y)
                battery_list.append(battery.id)

                csv_writer.writerow(battery_list)

        # create battery list
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

    ''' Animation will possibly be used during presentation '''
    # def beweging():
    #     fig = plt.figure()
    #     camera = Camera(fig)
    #     for i in range(100):
    #         plt.plot([i] * 10)
    #         camera.snap()
    #     animation = camera.animate(interval=500, blit=True)
    #     animation.save(
    #         'simple.mp4',
    #         dpi=100,
    #         savefig_kwargs={
    #             'frameon': False,
    #             'pad_inches': 'tight'
    #         })

    def printcheck(self):
        for battery in self.batteries:
            connections = []
            connection_count = 0
            for house in battery.connected:
                connections.append(house.id)
                connection_count += 1


            print("ID: ", battery.id)
            print("Max capacity: ", battery.max_amp)
            print("Cost: ", battery.cost)
            print("Coordinates: (" + str(battery.x) + "," + str(battery.y) + ")")
            print("Current usage: ", battery.current_usage)
            print("Connected", connections)
            print("Connection count: ", connection_count)
            print()

def create_visualization(self):

    # create dataframe
    df = pd.read_csv(self.visualdata)

    # set surroundings
    sns.set_color_codes("dark")

    # create scatterplot from dataframe
    plot = sns.scatterplot(x="x", y="y", hue="connected_bat", data=df, ci=None, style="type", palette=sns.color_palette("Paired", n_colors=len(self.batteries)))

    # set plot title
    plot.set_title(self.name)

    # set axis labels
    plot.set(xlabel='X coordinates', ylabel='Y coordinates')

    # remove plot legend
    plot.legend_.remove()

    # show plot
    plt.show()
