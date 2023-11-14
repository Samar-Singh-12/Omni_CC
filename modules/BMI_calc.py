# Body Mass Index Function
def bmi_calc(weight, height):
    bmi = weight / height**2
    under = (18.5 * height**2) - weight
    over = weight - (24.9 * height**2)

    if bmi > 40:
        body_status, body_status_identifier = "Extemely Obese !", over
    elif bmi > 30:
        body_status, body_status_identifier = "Obese !", over
    elif bmi > 25:
        body_status, body_status_identifier = "Over Weight !", over
    elif bmi > 18.5:
        body_status, body_status_identifier = "Healthy !", "Maintain this Weight and you'll be good !"
    else:
        body_status, body_status_identifier = "Under Weight !", under
    print(f"Your BMI is {bmi:.2f} & you're {body_status}")

    if body_status_identifier == over:
        print(f"You need to loose {over:.2f} Kilos to be Healthy !")
    elif body_status_identifier == under:
        print(f"You need to gain {under:.2f} Kilos to be Healthy !")
    else:
        print(body_status_identifier)