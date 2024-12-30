import numpy as np

class EnergyRecovery:
    def __init__(self, efficiency, battery_capacity, regen_factor, discharge_rate):
        self.efficiency = efficiency  # Enerji geri kazanım verimliliği
        self.battery_capacity = battery_capacity  # Batarya kapasitesi (kWh)
        self.regen_factor = regen_factor  # Geri kazanım faktörü
        self.discharge_rate = discharge_rate  # Batarya boşaltma oranı (kW/saat)

    def regen_energy(self, speed, deceleration):
        # Enerji geri kazanımı frenleme sırasında hesaplanır
        energy = 0.5 * self.regen_factor * (speed ** 2) * deceleration
        energy_recovered = energy * self.efficiency
        return energy_recovered

    def charge_battery(self, energy):
        # Bataryaya enerji şarj edilir ve kapasite sınırı dikkate alınır
        battery_energy = min(self.battery_capacity, energy)
        return battery_energy

    def discharge_battery(self, power):
        # Bataryanın enerjisi belirli bir güçle boşaltılır
        energy_used = power * self.discharge_rate
        self.battery_capacity -= energy_used
        if self.battery_capacity < 0:
            self.battery_capacity = 0
        return self.battery_capacity