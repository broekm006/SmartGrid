class Sort(object):


    def max_output(self, houses):
        # Sort houses by max output
        return sorted(houses, key=lambda house: house.amp, reverse=True)
    '''
    def distance(self, houses):

    def priority(self, houses):
    '''
