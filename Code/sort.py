import sys
sys.path.append('Code/classes')


class Sort(object):


    def max_output(self, houses):
        '''Sort houses by max output'''
        return sorted(houses, key=lambda house: house.amp, reverse=True)

    def distance(self, houses, battery):
        ''' Sort houses based on distance to given battery'''
        for house in houses:
            house.distance_to_battery = abs(battery.y - house.y) + abs(battery.x - house.x)

        return sorted(houses, key=lambda house: house.distance_to_battery)

    def priority_value(self, houses, batteries):
        ''' Sort houses based on priority value'''
        # Get distance to each battery
        for house in houses:
            for battery in batteries:
                battery.distance = abs(battery.y - house.y) + abs(battery.x - house.x)

            # sort batteries based on distance to current house = priority list
            batteries = sorted(batteries, key=lambda battery: battery.distance)
            house.priority_list = batteries

            # get priority value
            first_distance = batteries[0].distance
            sec_distance = batteries[1].distance
            house.pv = sec_distance - first_distance

        return sorted(houses, key=lambda house: house.pv, reverse=True)
