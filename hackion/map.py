import numpy as np

class CityMap(dict):

    def __init__(self, nx, ny):
        self.nx = nx
        self.ny = ny

    def city_block_distance(self, start, end):
        x1, y1, = start
        x2, y2 = end
        return abs(x1 - x2) + abs(y1 - y2)
    
    def random_destination(self):
        return [np.random.randint(0, self.nx), np.random.randint(0, self.ny)]

if __name__ == "__main__":
    my_map = CityMap(10, 10)
    # car class
    car_position = [0, 0]
    car_destination = my_map.random_destination()
    print(car_destination)
    print(my_map.city_block_distance(car_position, car_destination))