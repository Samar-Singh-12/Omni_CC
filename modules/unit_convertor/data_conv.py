from modules.unit_convertor.unit_conv_base import *


# Function for all required Data conversion
def data_conv(*args):
    units = {
        "Bits": 8589934592,
        "Bytes": 1073741824,
        "Kilo Bytes": 1048576,
        "Mega Bytes": 1024,
        "Giga Bytes": 1,
        "Tera Bytes": 0.0009765625,
        "Peta Bytes": 0.00000095367431640625,
    #     "Kilo Bits": 8388608,
    #     "Mega Bits": 8192,
    #     "Giga Bits": 8,
    #     "Tera Bits": 0.0078125,
    #     "Peta Bits": 0.00000762939453125,
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