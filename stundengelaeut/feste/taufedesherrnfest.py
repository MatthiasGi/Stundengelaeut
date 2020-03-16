from deltafest import DeltaFest
from datetime import date
from datetime import timedelta

class TaufeDesHerrnFest(DeltaFest):
    """
    Feste, die in Bezug auf das Fest „Taufe des Herrn“ stehen, werden hier
    zusammengefasst. Taufe des Herrn fällt immer auf den Sonntag nach
    Erscheinung des Herrn (6. Januar).
    """

    def referenceDate(self, year):
        """@inheritDoc"""
        erscheinung = date(year, 1, 6)
        delta = 7 - erscheinung.isoweekday()
        if delta == 0: delta = 7
        return erscheinung + timedelta(days = delta)
