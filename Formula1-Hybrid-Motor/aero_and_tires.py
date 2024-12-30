import numpy as np

class Aerodynamics:
    def _init_(self, drag_coefficient, downforce_coefficient, vehicle_weight):
        self.drag_coefficient = drag_coefficient  # Hava sürükleme katsayısı
        self.downforce_coefficient = downforce_coefficient  # Downforce katsayısı
        self.vehicle_weight = vehicle_weight  # Araç ağırlığı (kg)

    def drag_force(self, speed):
        # Hava sürükleme kuvveti hesaplaması
        air_density = 1.225  # kg/m^3 (deniz seviyesinde hava yoğunluğu)
        frontal_area = 2  # m^2 (örnek araç yüzeyi)
        drag_force = 0.5 * air_density * speed**2 * self.drag_coefficient * frontal_area
        return drag_force

    def downforce(self, speed):
        # Aerodinamik downforce hesaplaması
        downforce = self.downforce_coefficient * (speed ** 2)
        return downforce

class Tires:
    def _init_(self, max_grip, tire_diameter):
        self.max_grip = max_grip  # Maksimum lastik tutuşu (N)
        self.tire_diameter = tire_diameter  # Lastik çapı (m)

    def tire_grip(self, downforce):
        # Lastik tutuşu downforce'a göre hesaplanır
        grip = self.max_grip * (downforce / 1000)  # 1000 ile normalize edilmiştir
        return grip