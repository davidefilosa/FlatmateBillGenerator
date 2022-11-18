import webbrowser
from fpdf import FPDF
import os
from filestack import Client




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
        pdf.output(f'invoices/{self.filename}.pdf')
        os.chdir('invoices')
        webbrowser.open(f'{self.filename}.pdf')


class FileSharer:
    def __init__(self, filepath, api_key='AhzQO8uKTZOpkvyprZ8p3z'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
