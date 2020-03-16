from stundengelaeut.feste.adventsfest import AdventsFest
from stundengelaeut.feste.rang import Rang
from datetime import date

class Adventszeit(AdventsFest):
    """
    Die Adventszeit beginnt am ersten Advent (inklusive) und endet mit dem
    Weihnachtsfest am 25.12. (exklusive).
    """
    def __init__(self):
        pass

    def isDate(self, d):
        """@inheritDoc"""
        advent = self.referenceDate(d.year)
        weihnachten = date(d.year, 12, 25)
        return advent <= d and weihnachten > d

    def rang(self):
        """@inheritDoc"""
        return Rang.GEPRAEGTE_ZEIT

    def name(self):
        """@inheritDoc"""
        return "Fastenzeit"
