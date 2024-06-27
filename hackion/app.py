import hackion
import numpy as np

my_map = hackion.CityMap(10, 10)
car_position = [0, 0]
car_destination = [3, 3]  # my_map.random_destination()
print(car_destination)

distance_km = my_map.city_block_distance(car_position, car_destination)
distance_m = distance_km * 100


# to do: get speed limit from map
speed_limit = 30

# car class
vehicle = hackion.Vehicle()
vehicle.set_speed(speed_limit)
t, power = vehicle.power_to(distance_m)
power_array = np.column_stack((t, power))

total_energy = np.trapz(power, t / 3600)
print(f"Total energy: {total_energy:.2f} Wh")
print(f"Peak power: {np.max(power):.2f} W")

# battery class
battery = hackion.Battery()
final_soc = battery.determine_final_soc(power_array)

print(final_soc)
