from stundengelaeut.feste.osterfest import OsterFest
from stundengelaeut.feste.rang import Rang
from datetime import timedelta

class Osterzeit(OsterFest):
    """
    Die Osterzeit umfasst die Zeit nach Ostersonntag (inklusive) bis
    Pfingstsonntag (ebenfalls inklusive).
    """
    def __init__(self):
        pass

    def isDate(self, d):
        """@inheritDoc"""
        ostern = self.referenceDate(d.year)
        pfingsten = ostern + timedelta(days = 50)
        return d >= ostern and d < pfingsten
        # d < pfingsten, um Pfingstmontag auszusparen.

    def rang(self):
        """@inheritDoc"""
        return Rang.GEPRAEGTE_ZEIT

    def name(self):
        """@inheritDoc"""
        return "Osterzeit"
