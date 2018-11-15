import sys

sys.path.append('Code/algoritmes')
from load import Load

sys.path.append('Code/classes')
from helper import Helper

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
    load.connect_houses()

    # Moet Helper toevoegen voor Helper(self, ..., ...)
    Helper.costs(Helper, load.battery, load.house)
