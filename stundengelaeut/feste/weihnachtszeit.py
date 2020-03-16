from taufedesherrnfest import TaufeDesHerrnFest
from datetime import date

class Weihnachtszeit(TaufeDesHerrnFest):
    """
    Die Weihnachtszeit beginnt mit dem Hochfest der Geburt (25.12., inklusive)
    und endet mit dem Fest Taufe des Herrn (s. .taufedesherrn.TaufeDesHerrnFest,
    inklusive). Aufgrund des Jahreswechsels ist hier auf Datumsüberschneidungen
    zu achten.
    """
    def __init__(self):
        pass

    def isDate(self, d):
        """@inheritDoc"""
        if d.month == 12:
            return date(d.year, 12, 25) <= d
        else:
            return self.referenceDate(d.year) >= d

    def rang(self):
        """@inheritDoc"""
        return Rang.GEPRAEGTE_ZEIT

    def name(self):
        """@inheritDoc"""
        return "Weihnchtszeit"
