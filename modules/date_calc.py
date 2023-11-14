from dateutil.relativedelta import relativedelta
from dateutil.parser import parse

# This converts string to Date Time object
def date_conv(date):
    date_new = date.replace(",", "/")
    date_ot = parse(date_new, dayfirst=True)
    return date_ot


# This takes the Date Time Object and gives almost everything else we need
def date_diff(a, b):
    diff = relativedelta(date_conv(b), date_conv(a))
    days = diff.days
    months = diff.months
    years = diff.years
    diff_diff = date_conv(b) - date_conv(a)
    total_days = diff_diff.days

    print(f"\nTotal no. of Days between the given dates = {total_days} Days")
    print(
        f"Total no. of Months & Days between the given dates = {(years*12)+months} Months & {days} Days \n"
    )
    print(
        f"\nTime data between the given dates = {years} Years, {months} Months & {days} Days !"
    )


# This does Summation or Subtraction from Dates
def date_arth(a, y, m, d):
    a = date_conv(a)
    final = a + relativedelta(years=+y, months=+m, days=+d)
    print(f"The final date = {final.day}/{final.month}/{final.year}")