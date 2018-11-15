import sys
sys.path.append('Code/algoritmes')

from load import Load

if __name__ == "__main__":
    load = Load("wijk1", "wijk1")
    load.connect_houses()
    load.costs()
