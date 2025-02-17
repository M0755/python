fahrenheit_temps = [32, 50, 77, 104, 212]


celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]

print("Temperatures in Fahrenheit:", fahrenheit_temps)
print("Equivalent temperatures in Celsius:", celsius_temps)
