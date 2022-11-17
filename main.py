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

    def pay(self, bill):
        return bill.amount/2


class PdfReport:
    """Object that contains the info to generate a pdf report"""
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(120, 'March 2021')
jonh = Flatmate('Jonh', 20)
mary = Flatmate('Mary', 27)
print(jonh.pay(the_bill))