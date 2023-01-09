def celsius_to_f(inputTemp):
    return (inputTemp * 9/5) + 32

def calculate_windchill(inputTemp,inputWindSpeed):
    return 35.74 + 0.6215*inputTemp - 35.75*(inputWindSpeed**0.16) + 0.4275*inputTemp*(inputWindSpeed**0.16)

input_temp = float(input("What is the temperature? "))
input_system = input("Fahrenheit or Celsius (F/C)? ")
wind_speed = 5
wind_chill = -1

# (8 °C × 9/5) + 32 = 46.4 °F
if input_system.upper() == "C":
    input_temp = celsius_to_f

while wind_speed <= 60:
    print(f"At temperature {input_temp}F, and wind speed {wind_speed} mph, the windchill is: {calculate_windchill(input_temp,wind_speed):.2f}F")
    wind_speed += 5