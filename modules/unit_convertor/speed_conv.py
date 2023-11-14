from modules.unit_convertor.unit_conv_base import *


# Function for all required Speed conversion
def speed_conv(*args):
    units = {
        "Foot/Second": 0.911344,
        "Miles/Hour": 0.621427,
        "Knots": 0.540003456,
        "Meter/Second": 0.2778,
        "Kilometers/Hour": 1,
        "Mach": 0.000816273,
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
