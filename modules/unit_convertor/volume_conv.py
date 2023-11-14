from modules.unit_convertor.unit_conv_base import *


# Function for all required Volume conversion
def volume_conv(*args):
    units = {
        "Teaspoon (UK)": 168.9364,
        "Inch³": 61.02347,
        "Tablespoon (UK)": 56.3121,
        "Fluid Ounces (UK)": 35.195,
        "Litres": 1,
        "Gallons (UK)": 0.211969,
        "Foot³": 0.035315,
        "Yard³": 0.00130795,
        "Meter³": 0.001,
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
