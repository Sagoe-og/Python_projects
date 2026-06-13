import math


def convertor(celcius_temp):
    """COnverts temperature from celcius to farenheit"""
    #formula = (celcius* 9/5) +32

    farenheit_temp = (celcius_temp * (9/5) +32)
    return farenheit_temp







def wind_chill_calculator(temperature, wind_speed):
    """Calculates the wind chill index based on the temperature in Farenheit and wind speed in miles per hour"""
  

    if temperature > 50 or wind_speed < 3:
        return temperature
    else :
        wind_chill = (35.74 + (0.6215 * temperature))- (35.75 * (wind_speed ** 0.16))  + (0.4275 * temperature * (wind_speed ** 0.16))
        return wind_chill
    


if __name__ == "__main__":
    print("___Wind Chill calculator (Farenheit only)___")

    while True:
          #get temperature input from user
        try:
            temp = input("Enter the temperature in Farenheit(°F) : ")
            temperature = float(temp)
            break
        except ValueError:
            print("Invalid input.Please enter a numerical wind speed")





      #get wind speed input from user
    while True:
        try:
            temp_windspeed = input("Enter the wind speed in miles per hour (MPH) : ")
            wind_speed  = float(temp_windspeed)
            break
        except ValueError:
            print("Invalid input. Please enter a numerical wind speed")


#formula for calculating the wind speed
    calculated_wind_Chill = wind_chill_calculator(temperature, wind_speed)


    #displaying the final results


    print(f"For temperature{temperature} °F  and wind speed {wind_speed} MPH:")
    print(f"The calculated wind chill is : {calculated_wind_Chill:.2f}°F")


    

