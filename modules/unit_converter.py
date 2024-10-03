from modules.better_input import inputMenu
from modules.exchange_rates import *    

# Function for taking inputs for Unit converters
def take_inp(units, unit_out=None):
    unit_in = inputMenu(
        list(units.keys()),
        prompt="\nChoose Input Option from ↑: "
    )
    value = input(f"Enter the Value in {unit_in}: ")

    if unit_out:
        pass
    else:
        unit_out = inputMenu(
            list(units.keys()),
            prompt="\nChoose Output Option from ↑: ",
            numbered=True,
        )
    return value, unit_in, unit_out


# Printing the information for Unit convertors
def print_ot(packed):
    ot = packed[0]
    value = packed[1]
    unit_in = packed[2]
    unit_out = packed[3]
    print(f"\n{value} {unit_in} will be {ot:.4f} {unit_out}")


# Function for all required Area conversion
def area_conv(unit_out=None):
    units = {
        "Sq. Foot": 43560,
        "Sq. Yard": 4840,
        "Sq. Meter": 4046.856,
        "Acres": 1,
        "Hectares": 0.404686,
    }
    if unit_out:
        packed = take_inp(units, unit_out)
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out

# Function for all required Currency conversion

def currency_conv(unit_out=None):
    units = create_dict()
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))
    return ot, value, unit_in, unit_out 

# Function for all required Data conversion
def digital_storage_conv(unit_out=None):
    units = {
        "Bits": 8589934592,
        "Bytes": 1073741824,
        "Kilo Bytes": 1048576,
        "Mega Bytes": 1024,
        "Giga Bytes": 1,
        "Tera Bytes": 0.0009765625,
        "Peta Bytes": 0.00000095367431640625,
        "Kilo Bits": 8388608,
        "Mega Bits": 8192,
        "Giga Bits": 8,
        "Tera Bits": 0.0078125,
        "Peta Bits": 0.00000762939453125,
    }
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out


# Function for all required Length conversion
def length_conv(unit_out=None):
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
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out


# Function for all required Height conversion
def height_conv(unit_out=None):
    units = {
        "Centimeters": 100000,
        "Inches": 39370.08,
        "Foots": 3280.84,
        "Meters": 1000,
        "Foots'Inches": 0,
    }
    if unit_out:
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


# Funtion for all required Weight conversion
def mass_conv(unit_out=None):
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
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out


# Function for all required Pressure conversion
def pressure_conv(unit_out=None):
    units = {
        "Pascals": 1000,
        "mm of Hg": 7.5018,
        "Kilo Pascals": 1,
        "Pounds/Inch² (psi)": 0.145,
        "Bars": 0.01,
        "Atmospheric Pressure": 0.009869,
    }
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out


# Function for all required Speed conversion
def speed_conv(unit_out=None):
    units = {
        "Foot/Second": 0.911344,
        "Miles/Hour": 0.621427,
        "Knots": 0.540003456,
        "Meter/Second": 0.2778,
        "Kilometers/Hour": 1,
        "Mach": 0.000816273,
    }
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out


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


# Function for all required Volume conversion
def volume_conv(unit_out=None):
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
    if unit_out:
        packed = take_inp(units, unit_out)
    else:
        packed = take_inp(units)
    value = float(packed[0])
    unit_in = packed[1]
    unit_out = packed[2]
    ot = value * (units.get(unit_out) / units.get(unit_in))

    return ot, value, unit_in, unit_out
