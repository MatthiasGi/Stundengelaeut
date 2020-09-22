from datetime import date

from .fest import Fest
from .rang import Rang


class TagFest(Fest):
    """
    Feste, die an einem bestimmten Datum stattfinden, werden mit dieser Klasse
    bezeichnet.

    Attributes
    ----------
    _monat : int
        Internes Feld für Monat des Festes.
    _name : str
        Internes Feld für Namen.
    _rang : Rang
        Internes Feld für Rang.
    _tag : int
        Internes Feld für Tag des Feldes.
    """

    def __init__(self, monat: int, tag: int, name: str, rang: Rang):
        """
        Erstellt das Fest und speichert die Parameter zwischen.

        Parameters
        ----------
        monat : int
            Monat des Datums.
        tag : int
            Tag des Datums.
        name : str
            Name des Fests.
        rang : Rang
            Rang des Fests.

        Raises
        ------
        ValueError
            Falls die Tag-Monat-Kombination nicht valide ist.
        """
        if monat < 1 or monat > 12:
            raise ValueError("Ungültiger Monat übergeben!")
        if tag < 1 or tag > 31:
            raise ValueError("Ungültiger Tag übergeben! (1)")
        if monat in [4, 6, 9, 11] and tag > 30:
            raise ValueError("Ungültiger Tag übergeben! (2)")
        if monat == 2 and tag > 29:
            raise ValueError("Ungültiger Tag übergeben! (3)")
        self._monat = monat
        self._tag = tag
        self._name = name
        self._rang = rang

    @property
    def name(self):
        return self._name

    @property
    def rang(self):
        return self._rang

    def _happens(self, d: date) -> bool:
        return self._monat == d.month and self._tag == d.day
