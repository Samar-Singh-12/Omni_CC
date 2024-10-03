# Arithmetic Operations Functions:
def arithmetic(x, y, choice):
    try:
        sol = eval(f"{x}{choice}{y}")
        print(f"\n{x:.2f} {choice} {y:.2f} = {sol:.2f}")
    except ZeroDivisionError:
        print(f"{x} couldn't be divided by zero (0) !")
