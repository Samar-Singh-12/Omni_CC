from modules.unit_convertor.unit_conv_base import *


# Funtion for all required Weight conversion
def mass_conv(*args):
    units = {
        "Miligrams": 1000000,
        "Carats": 5000,
        "Grams": 1000,
        "Ounces": 35.27396,
        "Pounds": 2.204623,
        "Kilograms": 1,
        "Stone": 0.157473,
        "Tonnes": 0.001,
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
