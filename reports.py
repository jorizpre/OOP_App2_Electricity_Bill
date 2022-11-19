import webbrowser
from fpdf import FPDF


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

        # Inserting Image
        pdf.image("house.png", w=30, h=30)

        # Inserting rest of content
        pdf.set_font(family="Times", size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=150, h=40, txt="Amount:", border=1)
        pdf.cell(w=200, h=40, txt=str(bill.amount), border=1, ln=1)
        pdf.cell(w=150, h=40, txt="Period:", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate1.name, border=0)
        pdf.cell(w=200, h=40, txt=str(round(flatmate1.pays(bill, flatmate2), ndigits=2)), border=0, ln=1)
        pdf.cell(w=150, h=40, txt=flatmate2.name, border=0)
        pdf.cell(w=200, h=40, txt=str(round(flatmate2.pays(bill, flatmate1), ndigits=2)), border=0, ln=1)

        pdf.output(self.filename)

        # Opening the PDF file
        webbrowser.open(self.filename)
