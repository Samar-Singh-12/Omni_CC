from modules.unit_convertor.unit_conv_base import *


# Function for all required Height conversion
def height_conv(*args):
    units = {
        "Centimeters": 100000,
        "Inches": 39370.08,
        "Foots": 3280.84,
        "Meters": 1000,
        "Foots'Inches": 0,
    }
    if args:  
        unit_out = args[0]
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = packed[0]
    unit_in = packed[1]
    unit_out = packed[2]
    if unit_in != "Foots'Inches":
        value = float(value)
    else:
        fandi = [float(i) for i in value.split("'")]
        value, unit_in = fandi[0] * 12 + fandi[1], "Inches"  # value is in inches

    if unit_out != "Foots'Inches":
        ot = value * (units.get(unit_out) / units.get(unit_in))
    else:
        ot = value * (units.get("Inches") / units.get(unit_in))

    return ot, value, unit_in, unit_out
