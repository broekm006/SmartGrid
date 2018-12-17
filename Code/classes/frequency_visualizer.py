import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
# from bokeh.models.glyphs import Step
# from bokeh.models.annotations import Title
# from bokeh.io import curdoc, show


import sys
sys.path.append('../classes')

from house import House
from battery import Battery


class Frequency_visualizer():

    def __init__(self, results, visualtype, title):
        self.results_csv = self.write_csv(results, title)
        self.check_visual_type(visualtype)


    def write_csv(self, results, titel):
        '''Create a new .CSV file based on the results + name of the algorithm'''

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
        ''' Create frequency visualization based on the algorithm'''
        df = pd.read_csv(self.results_csv)

        sns.set(font_scale=0.5)

        plot = sns.distplot(df.costs, kde=False, bins=14)
        plot.set_title("Cost frequencies after Greedy priority sort and 1000 runs of HillClimber afterwards")
        plot.autoscale(enable=True, axis='both', tight=False)
        plot.set(xlabel='costs', ylabel='frequency')
        plot.grid(False)

        plt.show()


    def bar_sim():
        ''' Create a Bar graph for Simulated annealing'''
        readCsv = pd.read_csv("resultaten/Simulated_annealing.csv")

        sns.set_color_codes("dark")

        plot = sns.barplot(x="iteration", y="costs", data=readCsv, palette="RdBu")
        plot.set_title("Simulated_annealing barplot graph")
        plot.set(xlabel='Frequency * 1000', ylabel='Costs')
        plot.set_xticks(list(range(0,1001,100)))

        plt.show()


    def bar_total():
        '''Create a bar graph for the combined results  '''
        readCsv = pd.read_csv("resultaten/cheat.csv")

        sns.set_color_codes("dark")

        plot = sns.barplot(x="algorithm", y="costs", data=readCsv, order=["Lowerbound", "Output", "Distance" ,"Priority", "Output+HC", "Distance+HC", "Priority+HC", "Output+SA", "Distance+SA", "Priority+SA", "Upperbound"], palette="GnBu_d")
        plot.set_title("Algorithm Analyse")
        plot.set(xlabel='Algoritmes', ylabel='Kosten')

        plt.show()

    def sim_step_plot():
        source = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing.csv"))
        source0 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing0.csv"))
        source1 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing1.csv"))
        source2 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing2.csv"))
        source3 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing3.csv"))
        source4 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing4.csv"))
        source5 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing5.csv"))
        source6 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing6.csv"))
        source7 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing7.csv"))
        source8 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing8.csv"))
        source9 = ColumnDataSource(pd.read_csv("resultaten/Simulated_annealing9.csv"))
        title = Title()
        title.text = '10 times Greedy (priority) + Simulated Annealing'
        title.text_font_size = '7.5pt'

        plot = Plot(title=title, plot_width=300, plot_height=300, h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location=None)

        glyph1 = Step(x="iteration", y="costs", line_color="red", mode="before")
        plot.add_glyph(source, glyph1)

        glyph2 = Step(x="iteration", y="costs", line_color="green", mode="before")
        plot.add_glyph(source0, glyph2)

        glyph3 = Step(x="iteration", y="costs", line_color="blue", mode="before")
        plot.add_glyph(source1, glyph3)

        glyph4 = Step(x="iteration", y="costs", line_color="cyan", mode="before")
        plot.add_glyph(source2, glyph4)

        glyph5 = Step(x="iteration", y="costs", line_color="gray", mode="before")
        plot.add_glyph(source3, glyph5)

        glyph6 = Step(x="iteration", y="costs", line_color="black", mode="before")
        plot.add_glyph(source4, glyph6)

        glyph7 = Step(x="iteration", y="costs", line_color="fuchsia", mode="before")
        plot.add_glyph(source5, glyph7)

        glyph8 = Step(x="iteration", y="costs", line_color="yellow", mode="before")
        plot.add_glyph(source6, glyph8)

        glyph9 = Step(x="iteration", y="costs", line_color="lime", mode="before")
        plot.add_glyph(source7, glyph9)

        glyph10 = Step(x="iteration", y="costs", line_color="brown", mode="before")
        plot.add_glyph(source8, glyph10)

        glyph11 = Step(x="iteration", y="costs", line_color="pink", mode="before")
        plot.add_glyph(source9, glyph11)

        xaxis = LinearAxis()
        plot.add_layout(xaxis, 'below')
        plot.xaxis.axis_label = 'Iterations'

        yaxis = LinearAxis()
        plot.add_layout(yaxis, 'left')
        plot.yaxis.axis_label = 'Costs'

        plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
        plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

        show(plot)
