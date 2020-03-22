from stundengelaeut.feste.fest import Fest
from stundengelaeut.feste.rang import Rang

class Sonntage(Fest):
    """
    Zusammenfassung aller Sonntag
    """

    def rang(self):
        """@inheritDoc"""
        return Rang.SONNTAG

    def name(self):
        """@inheritDoc"""
        return "Sonntag"

    def isDate(self, d):
        """@inheritDoc"""
        return d.isoweekday() == 7
