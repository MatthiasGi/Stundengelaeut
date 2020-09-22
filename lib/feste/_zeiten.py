from datetime import (date, timedelta)

from ._feste import (AdventsFest, OsterFest, TaufeDesHerrnFest)
from .rang import Rang


class Adventszeit(AdventsFest):
    """
    Die Adventszeit beginnt am ersten Advent (inklusive) und endet mit dem
    Weihnachtsfest am 25.12. (exklusive).
    """

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return 'Adventszeit'

    @property
    def rang(self) -> Rang:
        return Rang.GEPRAEGTE_ZEIT

    def _happens(self, d: date) -> bool:
        advent = self._reference(d.year)
        christmas = date(d.year, 12, 25)
        return advent <= d and christmas > d


class Fastenzeit(OsterFest):
    """
    Die österliche Fastenzeit beginnt mit Aschermittwoch (inklusive) und endet
    mit dem Ostersonntag (exklusive). Dabei sind die Sonntage ausgenommen. Sie
    werden in dieser Klasse jedoch mit berücksichtigt.
    """

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return 'Fastenzeit'

    @property
    def rang(self) -> Rang:
        return Rang.GEPRAEGTE_ZEIT

    def _happens(self, d: date) -> bool:
        easter = self._reference(d.year)
        ashwednesday = easter + timedelta(days=-46)
        return ashwednesday <= d and easter > d


class Osterzeit(OsterFest):
    """
    Die Osterzeit umfasst die Zeit nach Ostersonntag (inklusive) bis
    Pfingstsonntag (ebenfalls inklusive).
    """

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return 'Osterzeit'

    @property
    def rang(self) -> Rang:
        return Rang.GEPRAEGTE_ZEIT

    def _happens(self, d: date) -> bool:
        easter = self._reference(d.year)
        pentecoste = easter + timedelta(days=49)
        return d >= easter and d <= pentecoste


class Weihnachtszeit(TaufeDesHerrnFest):
    """
    Die Weihnachtszeit beginnt mit dem Hochfest der Geburt (25.12., inklusive)
    und endet mit dem Fest Taufe des Herrn (s. TaufeDesHerrnFest, inklusive).
    Aufgrund des Jahreswechsels ist hier auf Datumsüberschneidungen zu achten.
    """

    def __init__(self):
        pass

    @property
    def name(self) -> str:
        return 'Weihnachtszeit'

    @property
    def rang(self) -> Rang:
        return Rang.GEPRAEGTE_ZEIT

    def _happens(self, d: date) -> bool:
        if d.month == 12:
            return date(d.year, 12, 25) <= d
        else:
            return self._reference(d.year) >= d
