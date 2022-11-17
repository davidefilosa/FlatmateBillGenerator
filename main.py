import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill (amount and bill).
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about a flatmate (name, days spent in the house).
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pay(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        return round(bill.amount * weight, 2)


class PdfReport:
    """Object that contains the info to generate a pdf report"""
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image(name='files/house.png', w=60)
        pdf.ln(25)
        pdf.set_font("Arial", size=24, style='B')
        pdf.cell(500, 20, txt='Flatmates Bill', ln=1, align='C')
        pdf.set_font("Arial", size=16, style='B')
        pdf.ln(25)
        pdf.cell(150, 10, txt='Period', ln=0, align='L')
        pdf.cell(150, 10, txt=bill.period, ln=1, align='L')
        pdf.ln(15)
        pdf.set_font("Arial", size=16, style='')
        pdf.cell(150, 10, txt=flatmate1.name, ln=0, align='L')
        pdf.cell(150, 10, txt=f'{flatmate1.pay(bill, flatmate2)}$', ln=1, align='L')
        pdf.ln(10)
        pdf.cell(150, 10, txt=flatmate2.name, ln=0, align='L')
        pdf.cell(150, 10, txt=f'{flatmate2.pay(bill, flatmate1)}$', ln=1, align='L')
        pdf.output(f'{self.filename}.pdf')
        webbrowser.open(f'{self.filename}.pdf')


while True:
    try:
        amount = float(input('Please add the bill amount: '))
    except ValueError:
        print('The bill amount should be a number. Please enter it again: ')
        continue

    period = input('Please enter the bill period. E.g. December 2022: ')
    flatmate1_name = input('What his the name of the first flatmate? ')
    try:
        flatmate1_days_in_house = int(input(f'How many days {flatmate1_name} spent in the house? '))
    except ValueError:
        print('The days should be a number. Please enter it again: ')
        continue

    flatmate2_name = input('What his the name of the second flatmate? ')
    try:
        flatmate2_days_in_house = int(input(f'How many days {flatmate2_name} spent in the house? '))
    except ValueError:
        print('The days should be a number. Please enter it again: ')
        continue

    the_bill = Bill(amount, period)
    flatmate1 = Flatmate(name=flatmate1_name, days_in_house=flatmate1_days_in_house)
    flatmate2 = Flatmate(name=flatmate2_name, days_in_house=flatmate2_days_in_house)
    print(flatmate1.pay(bill=the_bill, flatmate2=flatmate2))
    print(flatmate2.pay(bill=the_bill, flatmate2=flatmate1))
    report = PdfReport(f'{the_bill.period.replace(" ", "_")}')
    report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
    y = input('Do you want to generate another report? Y/N: ')
    if y.upper() == 'Y':
        continue
    else:
        break
