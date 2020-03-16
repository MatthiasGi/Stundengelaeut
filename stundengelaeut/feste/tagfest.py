from .fest import Fest

class TagFest(Fest):
    """
    Feste, die an einem bestimmten Datum stattfinden, werden mit dieser Klasse
    bezeichnet.

    Attributes
    ----------
    monat : int
        Monat, in dem das Fest stattfindet (1-12).
    tag : int
        Tag, an dem das Fest stattfindet (1-31, 1-30, 1-29 – je nach Monat).
    name : str
        Name des Festes.
    rang : .rang.Rang
        Rang des Festes

    Raises
    ------
    SystemExit
        Wenn ein ungültiger Monat oder Tag übergeben wurde, bricht das Programm
        hier ab.
    """
    def __init__(self, monat, tag, name, rang):
        if monat < 1 or monat > 12:
            raise SystemExit("Ungültiger Monat übergeben!")
        if tag < 1 or tag > 31:
            raise SystemExit("Ungültiger Tag übergeben! (1)")
        if monat in [4, 6, 9, 11] and tag > 30:
            raise SystemExit("Ungültiger Tag übergeben! (2)")
        else if monat == 2 and tag > 29:
            raise SystemExit("Ungültiger Tag übergeben! (3)")
        self.monat = monat
        self.tag = tag
        self.name = name
        self.rang = rang

    def isDate(self, d):
        """@inheritDoc"""
        return d.month == self.month and d.day == self.day

    def rang(self):
        """@inheritDoc"""
        return self.rang

    def name(self):
        """@inheritDoc"""
        return self.name
