from flat import Bill, Flatmate
from reports import PdfReport

a = float(input("Dear user, please enter the bill amount: "))
b = input("Now, please enter the period: ")
the_bill = Bill(amount=a, period=b)
c = input("Roommate #1: please enter his/her name: ")
d = float(input(f"Roommate #1 ({c}): please enter the days he/she spent in the flat this period: "))
flatmate1 = Flatmate(name=c, days_in_flat=d)
e = input("Roommate #2: please enter his/her name: ")
f = float(input("Roommate #2 ("+e+"): please enter the days he/she spent in the flat this period: "))
flatmate2 = Flatmate(name=e, days_in_flat=f)

print(f"{flatmate1.name} pays: ", round(flatmate1.pays(the_bill, flatmate2), 1))
print(f"{flatmate2.name} pays: ", round(flatmate2.pays(the_bill, flatmate1), 1))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(bill=the_bill, flatmate1=flatmate1, flatmate2=flatmate2)
