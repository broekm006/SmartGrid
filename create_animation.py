import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt

# for file_number in range(146):
#     print(file_number)

step = 1

colors = ["#dd805b", "#3c4fd7", "#9c8e8f", "#40e4f0", "#1ce8cf", "#fdf2f4", "#3ca96f", "#50dab8", "#1ae0a5", "#c088f5", "#9e28cd", "#aa1b56", "#ed5f71", "#20e24b", "#46638c", "#af01ac", "#925ca4", "#7d08ee", "#1c05ef", "#7b1867", "#34ba57", "#590f77", "#3c2e1f", "#e56b0f", "#1715f2", "#1a1647", "#fdc32e", "#4fce0f", "#390bf0", "#4dbeb3", "#850cd0", "#05a7a9", "#114077", "#9953a0", "#b837f9", "#9824f4", "#b35208", "#898705", "#9996ca", "#a435aa", "#3960f4", "#908e53", "#49c0e3", "#8c98d9", "#fa070c", "#60233f", "#fbaeb9", "#7d2894", "#f056e1", "#00c8c5", "#2d4cf0", "#ae2d93", "#bd0808", "#ec1be7", "#9a9c5c", "#ea1e49", "#1b916e", "#77c9b7", "#629559", "#f97f83", "#8a271c", "#d1fb4c", "#d7b6db", "#78f8b4", "#409daa", "#c4a1e3", "#784cea", "#259abe", "#f921ee", "#b3bed3", "#458573", "#820ad7", "#c37750", "#5a1f24", "#a17ae9", "#027a17", "#1d34f4", "#b01d93", "#4a8b42", "#9a197b", "#b35ad4", "#182f76", "#150f64", "#71078b", "#aa6b90", "#be087b", "#a64651", "#9c1a49", "#1e0386", "#218b94", "#71bf2f", "#d0b007", "#f3bf06", "#27b40d", "#6eea73", "#e21ec7", "#8b7dc3", "#d3f4ba", "#656d18", "#b3016e", "#df5c7f", "#fae120", "#96b246", "#f15369", "#12b95c", "#aed2d0", "#524d37", "#f4e3b6", "#7a218e", "#42be9a", "#ab5e89", "#4b5c20", "#b60918", "#4e6b06", "#ae5735", "#2ea4c3", "#ddeca0", "#f04249", "#ff1c29", "#e4f389", "#3d866b", "#e96a05", "#c7e3eb", "#8be112", "#efe9bb", "#317dca", "#72fb2e", "#6d6c1e", "#83755a", "#55d766", "#f92294", "#dd1631", "#1f9ccc", "#9c2485", "#5338ee", "#839049", "#cc5a40", "#0f7730", "#2bd82a", "#9f6aa6", "#05fa9e", "#cc69fa", "#35a6b0", "#04d513", "#cf09d0", "#1ecf02", "#e213a8", "#00a26a", "#877bd0", "#262d0c", "#8d568b"]

colordict = {}
for i in range(150):
    colordict[i] = colors[i]

print(colordict)
print()

color_list = []

# create dataframe
df = pd.read_csv("houses" + str(step) + ".csv")

for index, row in df.iterrows():
    if row["type"] == "house":
        color_list.append(colordict[row["connected_bat"]])

print("length of the colorlist:", len(color_list))
print(color_list)
print()
batterylist = []
for index, row in df.iterrows():
    if row["type"] == "battery":
        batterylist.append(row["id"])
print(batterylist)

# set surroundings
sns.set_color_codes("dark")

# create scatterplot from dataframe
plot = sns.scatterplot(x="x", y="y", hue="connected_bat", data=df, ci=None, style="type", palette=colordict)

# set plot title
plot.set_title("Hierarchical Agglomerative Clustering: step " + str(step))

# set axis labels
plot.set(xlabel='X coordinates', ylabel='Y coordinates')

# remove plot legend
plot.legend_.remove()

filename='step' + str(step) + '.png'
plt.savefig(filename)
#plt.gca()
