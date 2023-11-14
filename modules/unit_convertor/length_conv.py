from modules.unit_convertor.unit_conv_base import *


# Function for all required Length conversion
def length_conv(*args):
    units = {
        "Centimeters": 100000,
        "Inches": 39370.08,
        "Foots": 3280.84,
        "Yards": 1093.613,
        "Meters": 1000,
        "Kilometers": 1,
        "Miles": 0.621371,
        "Nautical Miles": 0.539957,
    }
    if args:  
        unit_out = args[0]
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out
