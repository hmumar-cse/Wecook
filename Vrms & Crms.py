import numpy as np

# Example raw ADC readings from ESP32
voltage_adc = np.array([2100, 2120, 2110, 2130, 2105])
current_adc = np.array([320, 350, 340, 360, 330])

# ESP32 ADC parameters
ADC_MAX = 4095
V_REF = 3.3

# Step 1: Convert ADC to actual voltage & current
voltage = (voltage_adc / ADC_MAX) * V_REF * 100   # scaled voltage
current = (current_adc / ADC_MAX) * V_REF * 10    # scaled current

# Step 2: Calculate RMS values
Vrms = np.sqrt(np.mean(voltage ** 2))
Irms = np.sqrt(np.mean(current ** 2))

# Step 3: Calculate power
power = Vrms * Irms

print("Vrms:", Vrms)
print("Irms:", Irms)
print("Power:", power)
