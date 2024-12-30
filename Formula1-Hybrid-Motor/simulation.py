import numpy as np
import matplotlib.pyplot as plt
from motor_model import HybridMotor
from energy_recovery import EnergyRecovery
from aero_and_tires import Aerodynamics, Tires

class F1Simulation:
    def __init__(self, motor, recovery_system, aero_system, tire_system):
        self.motor = motor
        self.recovery_system = recovery_system
        self.aero_system = aero_system
        self.tire_system = tire_system
        self.time = np.linspace(0, 180, 180)  # Simülasyon süresi
        self.speed = np.zeros_like(self.time)  # Aracın hızı
        self.torque = np.zeros_like(self.time)  # Aracın torku
        self.power = np.zeros_like(self.time)  # Toplam güç
        self.energy = np.zeros_like(self.time)  # Batarya enerji durumu
        self.drag_force = np.zeros_like(self.time)  # Hava sürükleme kuvveti
        self.downforce = np.zeros_like(self.time)  # Downforce

    def run_simulation(self):
        for i, t in enumerate(self.time):
            rpm = np.interp(self.speed[i], [0, 300], [1000, 12000])  # Hızdan RPM hesapla
            self.torque[i] = self.motor.total_torque(rpm)
            self.power[i] = self.motor.total_power(rpm)
            deceleration = np.random.uniform(0.2, 0.5)  # Rastgele frenleme oranı
            energy_recovered = self.recovery_system.regen_energy(self.speed[i], deceleration)
            self.energy[i] = self.recovery_system.charge_battery(energy_recovered)
            self.drag_force[i] = self.aero_system.drag_force(self.speed[i])
            self.downforce[i] = self.aero_system.downforce(self.speed[i])

    def plot_results(self):
        plt.figure(figsize=(12, 12))

        plt.subplot(4, 1, 1)
        plt.plot(self.time, self.speed, label='Speed (km/h)')
        plt.legend()
        plt.title('Speed Over Time')

        plt.subplot(4, 1, 2)
        plt.plot(self.time, self.torque, label='Torque (Nm)')
        plt.legend()
        plt.title('Torque Over Time')

        plt.subplot(4, 1, 3)
        plt.plot(self.time, self.power, label='Power (kW)')
        plt.legend()
        plt.title('Power Over Time')

        plt.subplot(4, 1, 4)
        plt.plot(self.time, self.energy, label='Battery Energy (kWh)')
        plt.legend()
        plt.title('Battery Energy Over Time')

        plt.tight_layout()
        plt.show()

# Parametreler
rpm_range_ice = (np.linspace(1000, 12000, 8), np.linspace(50, 450, 8))  # İçten yanmalı motor aralığı
rpm_range_electric = (np.linspace(1000, 12000, 8), np.linspace(100, 300, 8))  # Elektrikli motor aralığı

# Hibrid Motor, Enerji Sistemi, Aerodinamik ve Lastik Sistemleri
hybrid_motor = HybridMotor(max_torque_ice=500, max_torque_electric=250, max_power_ice=700, max_power_electric=350, rpm_range_ice=rpm_range_ice, rpm_range_electric=rpm_range_electric)
energy_system = EnergyRecovery(efficiency=0.85, battery_capacity=100, regen_factor=0.8, discharge_rate=0.1)
aero_system = Aerodynamics(drag_coefficient=0.5, downforce_coefficient=2.0, vehicle_weight=700)
tire_system = Tires(max_grip=1000, tire_diameter=0.7)

# Simülasyonu çalıştır
sim = F1Simulation(hybrid_motor, energy_system, aero_system, tire_system)
sim.run_simulation()
sim.plot_results()
