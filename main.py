from fpdf import FPDF


class Bill:
    """
    doc string: description of object
    Object containing data of Bill (amount, period)
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a Flatmate person containing its name, and days spent in the house
    """

    def __init__(self, name, days_in_flat):
        self.days_in_flat = days_in_flat
        self.name = name

    def pays(self, bill, other_flatmate):
        weight = self.days_in_flat/(self.days_in_flat + other_flatmate.days_in_flat)
        return bill.amount * weight


class PdfReport:
    """
    Create file with info about mates and amount to be paid by each
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        # See fpdf_test.py scratch for more information about PDF design
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.cell(w=150, h=40, txt="Amount:", border=1)
        pdf.cell(w=200, h=40, txt=str(bill.amount), border=1, ln=1)
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), ndigits=2)), border=0, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), ndigits=2)), border=0, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=100, period= "September 2022")
Jorge = Flatmate(name="Jorge", days_in_flat=21)
Veronika = Flatmate(name="Veronika", days_in_flat=19)

print(Jorge.pays(the_bill, Veronika))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate(bill=the_bill, flatmate1=Jorge, flatmate2=Veronika)

