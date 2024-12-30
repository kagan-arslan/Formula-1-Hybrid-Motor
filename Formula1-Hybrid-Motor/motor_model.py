import numpy as np

class HybridMotor:
    def __init__(self, max_torque_ice, max_torque_electric, max_power_ice, max_power_electric, rpm_range_ice, rpm_range_electric):
        self.max_torque_ice = max_torque_ice  # ICE için maksimum tork (Nm)
        self.max_torque_electric = max_torque_electric  # Elektrikli motor için maksimum tork (Nm)
        self.max_power_ice = max_power_ice  # ICE için maksimum güç (kW)
        self.max_power_electric = max_power_electric  # Elektrikli motor için maksimum güç (kW)
        self.rpm_range_ice = rpm_range_ice  # ICE RPM aralığı
        self.rpm_range_electric = rpm_range_electric  # Elektrikli motor RPM aralığı

    def get_ice_torque(self, rpm):
        # İçten yanmalı motorun torkunu RPM'ye göre hesaplayalım
        torque = np.interp(rpm, self.rpm_range_ice[0], self.rpm_range_ice[1])
        return torque

    def get_electric_torque(self, rpm):
        # Elektrikli motorun torkunu RPM'ye göre hesaplayalım
        torque = np.interp(rpm, self.rpm_range_electric[0], self.rpm_range_electric[1])
        return torque

    def get_ice_power(self, rpm):
        # ICE motorunun gücünü hesaplayalım
        torque = self.get_ice_torque(rpm)
        power = (torque * rpm) / 5252  # Güç = tork x devir / 5252
        return power

    def get_electric_power(self, rpm):
        # Elektrikli motorun gücünü hesaplayalım
        torque = self.get_electric_torque(rpm)
        power = (torque * rpm) / 5252  # Güç = tork x devir / 5252
        return power

    def total_power(self, rpm):
        # Toplam güç (ice ve elektrikli motor) hesaplanır
        ice_power = self.get_ice_power(rpm)
        electric_power = self.get_electric_power(rpm)
        total_power = ice_power + electric_power
        return total_power

    def total_torque(self, rpm):
        # Toplam tork hesaplanır
        ice_torque = self.get_ice_torque(rpm)
        electric_torque = self.get_electric_torque(rpm)
        total_torque = ice_torque + electric_torque
        return total_torque