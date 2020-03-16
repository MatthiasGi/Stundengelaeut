from .osterfest import OsterFest
from .rang import Rang
from datetime import timedelta

class Fastenzeit(OsterFest):
    """
    Die österliche Fastenzeit beginnt mit Aschermittwoch (inklusive) und endet
    mit dem Ostersonntag (exklusive). Dabei sind die Sonntage ausgenommen. Sie
    werden in dieser Klasse jedoch mit berücksichtigt.
    """
    def __init__(self):
        pass

    def isDate(self, d):
        """@inheritDoc"""
        ostern = self.referenceDate(d.year)
        aschermittwoch = ostern + timedelta(days = -46)
        return aschermittwoch <= d and ostern > d

    def rang(self):
        """@inheritDoc"""
        return Rang.GEPRAEGTE_ZEIT

    def name(self):
        """@inheritDoc"""
        return "Fastenzeit"
