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
        return bill * weight


class PdfReport:
    """Object that contains the info to generate a pdf report"""
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(amount=500, period='March 2021')
john = Flatmate(name='John', days_in_house=20)
mary = Flatmate(name='Mary', days_in_house=27)
print(john.pay(bill=the_bill.amount, flatmate2=mary))
print(mary.pay(bill=the_bill.amount, flatmate2=john))
