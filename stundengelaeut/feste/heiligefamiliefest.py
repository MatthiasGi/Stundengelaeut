from stundengelaeut.feste.deltafest import DeltaFest
from datetime import date
from datetime import timedelta

class HeiligeFamilieFest(DeltaFest):
    """
    Das Fest der Heiligen Familie ist ebenfalls beweglich. Es fällt auf den
    Sonntag in der Weihnachtsoktav. Gibt es den nicht (das bedeutet, dass kein
    Sonntag zwischen Weihnachten und Neujahr fällt, was nur möglich ist, wenn
    Weihnachten an einem Sonntag stattfindet), wird am 30.12. gefeiert.
    """

    def referenceDate(self, year):
        """@inheritDoc"""
        weihnachten = date(d.year, 12, 25)
        if weihnachten.isoweekday() == 7: return date(d.year, 12, 30)
        return weihnachten + timedelta(days = 7 - weihnachten.isoweekday())
