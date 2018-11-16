import sys
sys.path.append('Code/algoritmes')

from load import Load

if __name__ == "__main__":
    load = Load("wijk2", "wijk2")
    load.connect_houses()
    load.costs()
