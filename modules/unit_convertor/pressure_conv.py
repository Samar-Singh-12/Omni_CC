from modules.unit_convertor.unit_conv_base import *


# Function for all required Pressure conversion
def pressure_conv(*args):
    units = {
        "Pascals": 1000,
        "mm of Hg": 7.5018,
        "Kilo Pascals": 1,
        "Pounds/Inch² (psi)": 0.145,
        "Bars": 0.01,
        "Atmospheric Pressure": 0.009869,
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
