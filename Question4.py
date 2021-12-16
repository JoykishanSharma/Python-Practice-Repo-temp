# Write a python program to convert temperature to and from Celsius to fahrenheit.

def fah_to_cel(temp):
    return ((temp - 32) * 5) / 9


def cel_to_fah(temp):
    return 9/5 * temp + 32


temperature = 22
temp_in_fah = cel_to_fah(temperature)
print("Temperature in Farenheit : ", temp_in_fah)

temperature = 198
temp_in_cel = fah_to_cel(temperature)
print("Temperature in celcius : ", round(temp_in_cel, 2))
