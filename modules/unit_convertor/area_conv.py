from modules.unit_convertor.unit_conv_base import *


# Function for all required Area conversion
def area_conv(*args):
    units = {
        "Sq. Foot": 43560,
        "Sq. Yard": 4840,
        "Sq. Meter": 4046.856,
        "Acres": 1,
        "Hectares": 0.404686,
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