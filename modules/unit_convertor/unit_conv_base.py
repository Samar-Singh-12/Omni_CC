from pyinputplus import inputMenu

# Function for taking inputs for Unit converters
def take_inp(units, *args):
    unit_in = inputMenu(
        list(units.keys()),
        prompt="\nChoose Input Option from below ↓: \n",
        numbered=True,
    )
    value = input(f"Enter the Value in {unit_in}: ")

    if args:
        unit_out = args[0]
    else:
        unit_out = inputMenu(
            list(units.keys()),
            prompt="\nChoose Output Option from below ↓: \n",
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