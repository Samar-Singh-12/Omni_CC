from modules.unit_convertor.unit_conv_base import *


# Function for all required Temperature conversion
def temp_conv(value, unit_in, unit_out):
    if unit_in == "Celcius":
        if unit_out == "Farenheit":
            temp = (value * 9 / 5) + 32
        elif unit_out == "Kelvin":
            temp = value + 273.15
        else:
            temp = value
    elif unit_in == "Farenheit":
        if unit_out == "Celcius":
            temp = (value - 32) * 5 / 9
        elif unit_out == "Kelvin":
            temp = ((value - 32) * 5 / 9) + 273.15
        else:
            temp = value
    elif unit_in == "Kelvin":
        if unit_out == "Celcius":
            temp = value - 273.15
        elif unit_out == "Farenheit":
            temp = ((value - 273.15) * (9 / 5)) + 32
        else:
            temp = value
    
    return temp
