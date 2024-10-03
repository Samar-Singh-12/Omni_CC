# Importing Necessary Packages
from math import log
from sys import exit
from statistics import mean, mode, median
from modules.py_matrix import *
from modules.date_calc import *
from modules.arithmetic import *
from modules.BMI_calc import *
from modules.unit_converter import *
from modules.better_input import *

if __name__ == "__main__":
    # Defining Calculator Category
    def Calculator():
        # Taking choice input
        category_inp = inputMenu(
            [
                "+/-/÷/× Calculator",
                "Power & Root Calculator",
                "Factorial Calculator",
                "log Calculator",
                "Simultaneous Summation, Subtraction or Multiplication",
                "Matrix +/-/× Calculator",
                "Statistics Calculator (Mean/Mode/Median)",
                "Percentage Calculator",
                "BMI Calculator",
                "Interest Calculator",
                "Date Calculator",
                "Go Back",
            ],
            prompt="\nConduct any Operation from ↑ Choose: ",
        )
        # Looping of chosen Operation
        internal_loop = True
        while internal_loop:
            # Basic Arithmetic Operations :-
            if category_inp == "+/-/÷/× Calculator":
                print(
                    "-----x-----x-----x----- +/-/÷/× Calculator©-----x-----x-----x-----\n"
                )
                num_1 = inputNum("Enter number 1 : ")
                choice = inputMenu(
                    ["+", "-", "*", "/"], prompt="Choose any Operation from ↑: "
                )
                num_2 = inputNum("Enter number 2 : ")
                sol = arithmetic(num_1, num_2, choice)

            # Calculator for Power and Root
            elif category_inp == "Power & Root Calculator":
                print(
                    "-----x-----x-----x-----Power & Root Calculator©-----x-----x-----x-----\n"
                )
                choice = inputMenu(
                    ["Power", "Root"], prompt="Choose any one from ↑: "
                )
                if choice == "Power":
                    print("xⁿ or nth power of x")
                    value = inputNum("Enter Base (x): ")
                    variable = inputNum("Enter Exponent (n): ")
                    sol = pow(value, variable)
                elif choice == "Root":
                    print("ⁿ√x or nth root of x")
                    value = inputNum("Enter Radicand (x): ")
                    variable = inputNum("Enter Index (n): ")
                    sol = pow(value, (1 / variable))
                print(f"\n{variable} {choice} {value} is: {sol:.2f}")

            # Calculator for Factorial
            elif category_inp == "Factorial Calculator":
                print(
                    "-----x-----x-----x-----Factorial Calculator©-----x-----x-----x-----\n"
                )
                value = inputInt("x! or x Factorial\nInput the value x: ")
                sol = 1
                for i in range(2, value + 1):
                    sol *= i
                print(f"{value} factorial = {sol}")

            # Log Calculator with custom base values
            elif category_inp == "log Calculator":
                print("-----x-----x-----x-----Log Calculator©-----x-----x-----x-----\n")
                choice = inputMenu(
                    ["Natural log (ln)", "Base 10 (log)"],
                    prompt="log should be ? ↑: ",
                )
                value = inputNum("\nEnter the value: ")
                dict_values = {"Natural log (ln)": 2.7182818, "Base 10 (log)": 10}
                sol = log(value, dict_values[choice])
                print(f"Log Value: {sol:.4f}")

            # Calculator for continous Summation, Subtraction or Multiplication
            elif (
                category_inp == "Simultaneous Summation, Subtraction or Multiplication"
            ):
                print(
                    "-----x-----x-----x-----Continous Arithmetic Operations©-----x-----x-----x-----\n"
                )
                values = input("Enter Numbers seperated by commas: ")
                list_in = [int(i) for i in values.split(",")]
                choice = inputMenu(
                    ["+", "-", "*"], prompt="Choose any Operation from ↑: "
                )
                if choice == "+":
                    sol = sum(list_in)
                    print(f"\nSummation of the list is : {sol}")
                elif choice == "-":
                    for i in range(1, len(list_in)):
                        list_in[0] -= list_in[i]
                        i += 1
                    print(f"\nSubtraction of the list is : {list_in[0]}")
                elif choice == "*":
                    sol = 1
                    for i in list_in:
                        sol *= i
                    print(f"\nMultiplication of the list is : {sol}")

            # Calculator for Matrix +/-/×
            elif category_inp == "Matrix +/-/× Calculator":
                print(
                    "-----x-----x-----x-----Matrix Calculator©-----x-----x-----x-----\n"
                )
                ma = matrix_takein("A")
                mb = matrix_takein("B")
                choice = inputMenu(
                    ["Addition", "Subtraction", "Multiplication"],
                    prompt="\nConduct any Operation from ↑ Choose: ",
                )
                if choice == "Addition":
                    matrix_combo(ma, mb, "+")
                else:
                    dict = {"Subtraction": "-", "Multiplication": "×"}
                    orientation = inputInt(
                        prompt=f"\nYou want to operate like? \n1. A {dict.get(choice)} B \n2. B {dict.get(choice)} A\n",
                        min=1,
                        max=2,
                    )
                    if orientation == 1:
                        pass
                    else:
                        ma, mb = mb, ma
                    if choice == "Multiplication":
                        matrix_mul(ma, mb)
                    else:
                        matrix_combo(ma, mb, "-")

            # Calculator for Mean, Mode & Median for a given data
            elif category_inp == "Statistics Calculator (Mean/Mode/Median)":
                print(
                    "-----x-----x-----x-----Mean, Mode, Median Calculator©-----x-----x-----x-----\n"
                )
                values = input("Enter Numerical Data seperated by commas: ")
                list_in = [float(i) for i in values.split(",")]
                choice = inputMenu(
                    ["mean", "mode", "median", "all"],
                    prompt="Choose any Operation from ↑: ",
                )
                mean_sol = f"\nMean of the data: {mean(list_in):.2f}"
                mode_sol = f"\nMode of the data: {mode(list_in):.2f}"
                median_sol = f"\nMedian of the data: {median(list_in):.2f}"
                if choice == "mean":
                    print(mean_sol)
                elif choice == "mode":
                    print(mode_sol)
                elif choice == "median":
                    print(median_sol)
                elif choice == "all":
                    print(mean_sol, mode_sol, median_sol)

            # Many Percentage Based Calculations
            elif category_inp == "Percentage Calculator":
                print(
                    "-----x-----x-----x-----Percentage Calculator©-----x-----x-----x-----\n"
                )
                print(
                    f"1. Find initial value by final value and percentage (What is ___% of ___) \n2. Find percentage of one value to another value (___ is what % of ___) \n3. Find final value by initial value and percentage  (___ is ___% of ?) \n4. Increase or Decrease Value by x percentage (___ ↑/↓ ___% = ?)\n"
                )
                choice = inputInt(prompt="Choose: ", min=1, max=4)
                if choice == 1:
                    percent = inputNum("\nEnter the Percentage: ")
                    value = inputNum("Enter the Value: ")
                    sol = (percent * value) / 100
                    print(f"\n{percent}% of {value} will be {sol:.2f}")
                elif choice == 2:
                    value_1 = inputNum("\nEnter 1st Value: ")
                    value_2 = inputNum("Enter 2nd Value: ")
                    sol = (value_1 * 100) / value_2
                    print(f"\n{value_1} is {sol:.2f}% of {value_2}")
                elif choice == 3:
                    value = inputNum("\nEnter initial Value: ")
                    percent = inputNum("Enter the Percentage: ")
                    sol = value * (100 / percent)
                    print(f"\n{value} is {percent}% of {sol:.2f}")
                elif choice == 4:
                    value = inputNum("\nEnter the Value: ")
                    int_choice = inputMenu(
                        ["Increase", "Decrease"],
                        prompt="Choose any one from ↑: ",
                    )
                    percent = inputNum("Enter the Percentage: ")
                    if int_choice.lower() == "increase":
                        sol = value * (1 + (percent / 100))
                        print(f"\n{percent}% Increase in {value} gives {sol:.2f}")
                    elif int_choice.lower() == "decrease":
                        sol = value * (1 - (percent / 100))
                        print(f"\n{percent}% Decrease in {value} gives {sol:.2f}")

            # BMI Calculator
            elif category_inp == "BMI Calculator":
                print(
                    "-----x-----x-----x-----Body Mass Index Calc©-----x-----x-----x-----\n"
                )
                choice = inputMenu(
                    ["Kilograms", "Pounds"],
                    prompt="Choose Input Option from ↑: ",
                )
                weight_in = inputNum(f"\nEnter your weight in {choice}:  ")

                kilos = weight_in if choice == "Kilograms" else weight_in * 2.204623

                packed = height_conv("Meters")
                meters = packed[0]
                bmi_calc(kilos, meters)

            # Simple Interest and Compound Interest Calculator
            elif category_inp == "Interest Calculator":
                print(
                    "-----x-----x-----x-----Simple & Compound interests©-----x-----x-----x-----\n"
                )
                choice = inputMenu(
                    ["Simple Interest", "Compound Interest", "Both"],
                    prompt="Choose any one from ↑: ",
                )
                principle = inputNum("\nEnter Principal Balance: ")
                rate = inputNum("Enter Annual Interest Rate: ")
                time = inputNum("Enter Time (years): ")
                si = (principle * rate * time) / 100
                si_amount = principle + si
                ci_amount = principle * ((1 + rate / 100) ** time)
                ci = ci_amount - principle
                if choice == "Simple Interest":
                    print(f"\nAmount: {si_amount:.2f} & its Simple Interest: {si:.2f}")
                elif choice == "Compound Interest":
                    print(
                        f"\nAmount: {ci_amount:.2f} & its Compound Interest: {ci:.2f}"
                    )
                elif choice == "Both":
                    print(f"\nAmount: {si_amount:.2f} & its Simple Interest: {si:.2f}")
                    print(
                        f"\nAmount: {ci_amount:.2f} & its Compound Interest: {ci:.2f}"
                    )

            # Calculator for Date related Calculations
            elif category_inp == "Date Calculator":
                print(
                    "-----x-----x-----x-----Date Calculator©-----x-----x-----x-----\n"
                )
                choice = inputMenu(
                    ["Difference Between Dates", "Addition of data to a Date"],
                    prompt="Choose any one Option from ↑: ",
                )
                if choice == "Difference Between Dates":
                    start_date = input(
                        "\nEnter the date from which the time has to be claculated [dd/mm/yyyy]: "
                    )
                    finish_date = input(
                        "Enter the date upto which the time has to be claculated [dd/mm/yyyy]: "
                    )
                    date_diff(start_date, finish_date)
                elif choice == "Addition of data to a Date":
                    date_in = input("\nEnter the date [dd/mm/yyyy]: ")
                    days_arth = inputInt(f"Enter the no. of days to be added: ")
                    month_arth = inputInt(f"Enter the no. of months to be added: ")
                    year_arth = inputInt(f"Enter the no. of years to be added: ")
                    date_arth(date_in, year_arth, month_arth, days_arth)

            elif category_inp == "Go Back":
                Executor()
                return

            # Loop continue or not
            internal_loop = inputYesNo(
                f"\nDo you want to conduct {category_inp} again ? [Yes/No]:  "
            )
            if internal_loop:
                continue
            else:
                break

    # Defining Unit Converter Category
    def Unit_Conv():
        # Taking choice input
        category_inp = inputMenu(
            [
                "Currency Converter",
                "Digital Storage Converter",
                "Height Convertor",
                "Length Convertor",
                "Speed Converter",
                "Mass Convertor",
                "Area Convertor",
                "Volume Converter",
                "Pressure Converter",
                "Temperature Convertor",
                "Go Back",
            ],
            prompt="\nConduct any Operation from ↑ Choose: ",
        )
        # Looping of chosen Operation
        internal_loop = True
        counter = 0
        while internal_loop:
            # Calculator for Currency Conversion
            if category_inp == "Currency Converter":
                print(
                    "-----x-----x-----x-----Currency Exchange Rates©-----x-----x-----x-----\n"
                )
                print("NOTE: This requires a stable INTERNET CONNECTION !!!")
                if counter == 0:
                    update_rates()
                packed = currency_conv()
                print_ot(packed)

            # Calculator for Storage Unit Conversion
            elif category_inp == "Digital Storage Converter":
                print(
                    "-----x-----x-----x-----Digital Storage Conversion©-----x-----x-----x-----\n"
                )
                packed = digital_storage_conv()
                print_ot(packed)

            # Calculator for Height Conversion
            elif category_inp == "Height Convertor":
                print(
                    "-----x-----x-----x-----Height Conversion©-----x-----x-----x-----\n"
                )
                packed = height_conv()
                ot = packed[0]
                value = packed[1]
                unit_in = packed[2]
                unit_out = packed[3]
                if unit_out != "Foots'Inches":
                    print_ot(packed)
                else:
                    print(
                        f"{value} {unit_in} will be {ot//12:.0f}'{ot%12:.1f} {unit_out}"
                    )

            # Calculator for Length Conversion
            elif category_inp == "Length Convertor":
                print(
                    "-----x-----x-----x-----Length Conversion©-----x-----x-----x-----\n"
                )
                packed = length_conv()
                print_ot(packed)

            # Calculator for Speed Conversion
            elif category_inp == "Speed Converter":
                print(
                    "-----x-----x-----x-----Speed Conversion©-----x-----x-----x-----\n"
                )
                packed = speed_conv()
                print_ot(packed)

            # Calculator for Mass Conversion
            elif category_inp == "Mass Convertor":
                print(
                    "-----x-----x-----x-----Mass Conversion©-----x-----x-----x-----\n"
                )
                packed = mass_conv()
                print_ot(packed)

            # Calculator for Area Conversion
            elif category_inp == "Area Convertor":
                print(
                    "-----x-----x-----x-----Area Conversion©-----x-----x-----x-----\n"
                )
                packed = area_conv()
                print_ot(packed)

            # Calculator for Volume Conversion
            elif category_inp == "Volume Converter":
                print(
                    "-----x-----x-----x-----Volume Conversion©-----x-----x-----x-----\n"
                )
                packed = volume_conv()
                print_ot(packed)

            # Calculator for Pressure Conversion
            elif category_inp == "Pressure Converter":
                print(
                    "-----x-----x-----x-----Pressure Conversion©-----x-----x-----x-----\n"
                )
                packed = pressure_conv()
                print_ot(packed)

            # Calculator for Temperature Conversion
            elif category_inp == "Temperature Convertor":
                print(
                    "-----x-----x-----x-----Temperature Conversion©-----x-----x-----x-----\n"
                )
                packed = take_inp(
                    {"Celcius": "Superior", "Farenheit": "Stupid", "Kelvin": "Physics"}
                )
                value = float(packed[0])
                unit_in = packed[1]
                unit_out = packed[2]
                print(
                    f"\nThe Converted Value will be {temp_conv(value,unit_in,unit_out):.2f} {unit_out}"
                )

            elif category_inp == "Go Back":
                Executor()
                return

            counter += 1

            # Continue Internal Loop or not
            internal_loop = inputYesNo(
                f"\nDo you want to conduct {category_inp} again ? [Yes/No]:  "
            )
            if internal_loop:
                continue
            else:
                break

    # Defining the main code Execution Function
    def Executor():
        # Taking input
        main_inp = inputMenu(
            ["Calculators", "Unit Converters", "Exit Code"],
            prompt="\nAccess Calculators or Unit Convertors ? Choose from ↑: ",
        )
        # Looping of chosen Category
        category_loop = True
        while category_loop:
            if main_inp == "Calculators":
                Calculator()
            elif main_inp == "Unit Converters":
                Unit_Conv()
            else:
                print(
                    "\n----x-----x-----x-----Closing Mahenga Calculator©-----x-----x-----x----\n"
                )
                exit()

            # Continue Category Loop or not
            category_loop = inputYesNo(
                f"\nDo you want to conduct an operation in the {main_inp} Category? [Yes/No]: "
            )
            if category_loop:
                continue
            else:
                return

    # Main code starts from here:
    print(
        "\n----x-----x-----x-----x-----Mahenga Calculator©-----x-----x-----x-----x----"
    )

    # Looping of Code
    choice_loop = True
    while choice_loop:
        Executor()

        # Continue Main Loop or not
        choice_loop = inputYesNo(
            "\nDo you want to access another Category ? [Yes/No]: "
        )
        if choice_loop:
            continue
        else:
            print(
                "\n----x-----x-----x-----Closing Mahenga Calculator©-----x-----x-----x----\n"
            )
            break
