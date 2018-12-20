import csv
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
from solution import Solution

sys.path.append('Code/algoritmes')
from test_merge import Cluster_merge


class Grid_visualizer():

    def __init__(self, houses, batteries, visualtype, name, solutions, best_solution):
        # self.batteries = batteries
        self.name = name

        # print(len(solutions))
        # self.batteries = best_solution.batteries
        # self.solution_number = 0
        # self.visualdata = self.write_csv(best_solution.houses, best_solution.batteries)
        # self.check_visual_type(visualtype)

        for index, solution in enumerate(solutions):
            self.batteries = solution.batteries
            self.solution_number = index
            self.visualdata = self.write_csv(solution.houses, solution.batteries)
            print(self.visualdata)
            self.check_visual_type(visualtype)

        # self.printcheck()



    def check_visual_type(self, visualtype):

        # check for visual type
        if visualtype == "gridview":
            create_visualization(self)
        else:
            # possible animation
            pass


    def write_csv(self, houses, batteries):

        # create house list and...
        with open("houses" + str(self.solution_number) + ".csv", "w") as csv_file:
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

        return "houses" + str(self.solution_number) + ".csv"

    ''' Animation will possibly be used during presentation '''
    def beweging():

        fig = plt.figure()
        camera = Camera(fig)
        for i in range(100):
            plt.plot([i] * 10)
            camera.snap()
        animation = camera.animate()
        # animation = camera.animate(interval=500, blit=True)
        # animation.save(
        #     'simple.mp4',
        #     dpi=100,
        #     savefig_kwargs={
        #         'frameon': False,
        #         'pad_inches': 'tight'
        #     })

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
    print(df)

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

    filename='step'+str(self.solution_number)+'.png'
    plt.savefig(filename)
    plt.gca()


    # show plot
    #plt.show()
