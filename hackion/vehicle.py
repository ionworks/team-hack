import numpy as np
import matplotlib.pyplot as plt


class Vehicle:
    mass: float = 1500
    efficiency: float = 0.9
    v_max: float = 0
    drag_coefficient: float = 0.3
    frontal_area: float = 2.2  # m^2 (frontal area of the car)
    rolling_resistance_coefficient: float = 0.015

    def current_position(self):
        raise NotImplementedError

    def drive_to(self, destination):
        raise NotImplementedError

    def set_speed(self, speed):
        self.v_max = speed

    def power_to(self, distance):
        acceleration = 1  # m/s^2
        deceleration = 1  # m/s^2

        self.set_speed(10)

        t, speed = self.get_speed_profile_to(distance, acceleration, deceleration)

        return self.get_power_profile(t, speed, self.mass, self.drag_coefficient, self.frontal_area, self.rolling_resistance_coefficient)

    def get_speed_profile_to(self, total_distance, acceleration, deceleration):
        # Time to reach maximum speed
        t_acceleration = self.v_max / acceleration

        # Distance covered during acceleration
        d_acceleration = 0.5 * acceleration * t_acceleration ** 2

        # Time to decelerate from maximum speed to rest
        t_deceleration = self.v_max / deceleration

        # Distance covered during deceleration
        d_deceleration = 0.5 * deceleration * t_deceleration ** 2

        current_speed = self.v_max
        # Check if the total distance is enough to reach maximum speed and decelerate
        if d_acceleration + d_deceleration > total_distance:
            # Adjust maximum speed if distance is not enough
            current_speed = np.sqrt(total_distance * acceleration * deceleration / (acceleration + deceleration))
            t_acceleration = current_speed / acceleration
            t_deceleration = current_speed / deceleration
            d_acceleration = 0.5 * acceleration * t_acceleration ** 2
            d_deceleration = 0.5 * deceleration * t_deceleration ** 2
            d_constant = 0
            t_constant = 0
        else:
            # Distance covered at constant speed
            d_constant = total_distance - d_acceleration - d_deceleration

            # Time spent at constant speed
            t_constant = d_constant / current_speed

        # Total time
        total_time = t_acceleration + t_constant + t_deceleration

        # Create time array
        t = np.linspace(0, total_time, 500)

        # Initialize speed array
        speed = np.zeros_like(t)

        # Fill speed array
        for i, time in enumerate(t):
            if time < t_acceleration:
                speed[i] = acceleration * time
            elif time < t_acceleration + t_constant:
                speed[i] = current_speed
            else:
                speed[i] = current_speed - deceleration * (time - t_acceleration - t_constant)

        return t, speed

    @staticmethod
    def get_power_profile(t, speed, mass, drag_coefficient, frontal_area, rolling_resistance_coefficient, air_density=1.225,
                      gravity=9.81):
        # Calculate the acceleration
        acceleration = np.gradient(speed, t)

        # Calculate resistive forces
        drag_force = 0.5 * drag_coefficient * air_density * frontal_area * speed ** 2
        rolling_resistance = rolling_resistance_coefficient * mass * gravity

        # Calculate total force
        total_force = mass * acceleration + drag_force + rolling_resistance

        # Calculate power
        power = total_force * speed

        # Plot the power profile
        plt.plot(t, power)
        plt.xlabel('Time (s)')
        plt.ylabel('Power (W)')
        plt.title('Power Profile')
        plt.grid(True)
        plt.show()

        return t, power
