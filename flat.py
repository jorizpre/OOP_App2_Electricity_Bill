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
        weight = self.days_in_flat / (self.days_in_flat + other_flatmate.days_in_flat)
        return bill.amount * weight


