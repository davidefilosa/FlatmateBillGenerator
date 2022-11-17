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
        return round(bill.amount * weight,2)


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


the_bill = Bill(amount=500, period='November 2022')
john = Flatmate(name='John', days_in_house=20)
mary = Flatmate(name='Mary', days_in_house=27)
print(john.pay(bill=the_bill, flatmate2=mary))
print(mary.pay(bill=the_bill, flatmate2=john))
report = PdfReport('november_bill')
report.generate(flatmate1=john, flatmate2=mary, bill=the_bill)
