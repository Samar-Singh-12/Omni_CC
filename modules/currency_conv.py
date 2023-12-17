import requests
import openpyxl

# API endpoint and your app ID (get yours from Open Exchange Rates)
API_URL = "https://v6.exchangerate-api.com/v6/4fd120e4fbf752644f2d3019/latest/USD"

# Spreadsheet file
SPREADSHEET_FILE = "exchange_rates.xlsx"


def update_rates():
    """
    Fetches exchange rates from API and updates spreadsheet.
    """

    # Send API request
    response = requests.get(API_URL)
    response.raise_for_status()

    # Get rates from JSON response
    data = response.json()
    rates = data.get("conversion_rates", {})

    # Create a new workbook or load an existing one
    try:
        wb = openpyxl.load_workbook(SPREADSHEET_FILE)
        sheet = wb.active
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        sheet = wb.active

    # Clear the sheet
    for row in sheet.iter_rows():
        for cell in row:
            cell.value = None

    # Write rates to the sheet
    for i, (currency, rate) in enumerate(rates.items(), start=2):
        sheet.cell(row=i, column=1, value=currency)
        sheet.cell(row=i, column=2, value=rate)

    # Save changes to spreadsheet
    wb.save(SPREADSHEET_FILE)


# Update rates initially
update_rates()