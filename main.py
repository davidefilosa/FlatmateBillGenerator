from flat import Bill, Flatmate
from report import PdfReport

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
