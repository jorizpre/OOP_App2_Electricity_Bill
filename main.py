class Bill:
    """
    "doc string: description of object"
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

    def pays(self, bill):
        # return (self.days_in_flat/bill.period)*bill.amount
        pass


class PdfReport:
    """
    Create file with info about mates and amount to be paid by each
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill, flatmate1, flatmate2):
        pass
