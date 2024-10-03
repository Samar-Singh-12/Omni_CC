# Input Number Function:
def inputNum(prompt):
    while True:
        try:
            inp = float(input(prompt))
            return inp
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please input a valid Number\n")
            continue


# Input Integer Function:
def inputInt(prompt):
    while True:
        try:
            inp = int(input(prompt))
            return inp
        except ValueError as e:
            print(f"\nInvalid input: {e}. Please input a valid Integer\n")
            continue


# Input Yes/No Function:
def inputYesNo(prompt):
    while True:
        inp = input(prompt).strip().lower()
        if inp in ["y", "yes"]:
            return True
        elif inp in ["n", "no"]:
            return False
        else:
            print("\nPlease input [yes/y] or [no/n]\n")


# Input Menu Function:
def enum_lst(lst):
    for n, i in enumerate(lst):
        print(f"{n+1}. {i}")


def print_lst(lst):
    for i in lst:
        print(f"- {i}")


def inputMenu(lst, prompt="Input from above: ", numbered=True):
    while True:
        if numbered:
            enum_lst(lst)
            inp = input(prompt).strip()
            if inp.isdigit():
                index = int(inp)
                if 1 <= index < len(lst) + 1:
                    return lst[index - 1]
        else:
            print_lst(lst)
            inp = input(prompt).strip()

        if inp in lst:
            return inp

        print("\nPlease Input a valid value!\n")
