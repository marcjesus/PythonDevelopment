import numpy as np
import matplotlib.pyplot as plt

class EVMotor:
    def __init__(self, name, power_kW, max_torque_Nm, max_speed_rpm, voltage_V, back_emf_constant):
        self.name = name
        self.power_kW = power_kW
        self.max_torque_Nm = max_torque_Nm
        self.max_speed_rpm = max_speed_rpm
        self.voltage_V = voltage_V
        self.back_emf_constant = back_emf_constant
    
    def torque_curve(self, speeds_rpm):
        return np.maximum(0, self.max_torque_Nm * (1 - speeds_rpm / self.max_speed_rpm))
    
    def power_curve(self, speeds_rpm):
        speeds_rad_per_sec = speeds_rpm * 2 * np.pi / 60
        torque = self.torque_curve(speeds_rpm)
        power = torque * speeds_rad_per_sec / 1000  # Power in kW
        return np.minimum(self.power_kW, power)
    
    def back_emf_curve(self, speeds_rpm):
        speeds_rad_per_sec = speeds_rpm * 2 * np.pi / 60
        back_emf = self.back_emf_constant * speeds_rad_per_sec
        return back_emf
    
    def plot_characteristics(self):
        speeds_rpm = np.linspace(0, self.max_speed_rpm, 500)
        torque = self.torque_curve(speeds_rpm)
        power = self.power_curve(speeds_rpm)
        back_emf = self.back_emf_curve(speeds_rpm)
        
        plt.figure(figsize=(12, 8))
        
        plt.subplot(3, 1, 1)
        plt.plot(speeds_rpm, torque, label='Torque (Nm)', color='b')
        plt.title(f'{self.name} Motor Torque Curve')
        plt.xlabel('Speed (RPM)')
        plt.ylabel('Torque (Nm)')
        plt.grid(True)
        
        plt.subplot(3, 1, 2)
        plt.plot(speeds_rpm, power, label='Power (kW)', color='r')
        plt.title(f'{self.name} Motor Power Curve')
        plt.xlabel('Speed (RPM)')
        plt.ylabel('Power (kW)')
        plt.grid(True)
        
        plt.subplot(3, 1, 3)
        plt.plot(speeds_rpm, back_emf, label='Back EMF (V)', color='g')
        plt.title(f'{self.name} Motor Back EMF Curve')
        plt.xlabel('Speed (RPM)')
        plt.ylabel('Back EMF (V)')
        plt.grid(True)
        
        plt.tight_layout()
        plt.show()

# Create an instance for an example motor
# Assuming back EMF constant (ke) = 0.1 V*s/rad
tesla_model_s = EVMotor("Tesla Model S", power_kW=310, max_torque_Nm=931, max_speed_rpm=16000, voltage_V=400, back_emf_constant=0.1)
nissan_leaf = EVMotor("Nissan Leaf", power_kW=110, max_torque_Nm=320, max_speed_rpm=10390, voltage_V=400, back_emf_constant=0.1)
chevrolet_bolt = EVMotor("Chevrolet Bolt", power_kW=150, max_torque_Nm=360, max_speed_rpm=8750, voltage_V=400, back_emf_constant=0.1)

# Plot characteristics for each motor
motors = [tesla_model_s, nissan_leaf, chevrolet_bolt]

for motor in motors:
    motor.plot_characteristics()
