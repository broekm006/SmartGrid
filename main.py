import sys

sys.path.append('Code')
from load import Load

sys.path.append('Code/classes')
from helper import Helper
from sort import Sort

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
    load.connect_houses()

    # Moet Sort & Helper toevoegen voor Helper(self, ..., ...)
    Sort.max_output(Sort, load.house)
    Helper.costs(Helper, load.battery, load.house)
