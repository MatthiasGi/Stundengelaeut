from datetime import (date, timedelta)

from .deltafest import DeltaFest


class AdventsFest(DeltaFest):
    """
    Feste, die in Abhängigkeit vom ersten Advent stehen, werden mit dieser
    Klasse bezeichnet. Dabei wrid die Anzahl an Tagen angegeben, die das Fest
    sich vom ersten Advent unterscheidet.
    """

    def _reference(self, year: int) -> date:
        christmas = date(year, 12, 25)
        return christmas + timedelta(days=-christmas.isoweekday() - 7 * 3)


class HeiligeFamilieFest(DeltaFest):
    """
    Das Fest der Heiligen Familie ist ebenfalls beweglich. Es fällt auf den
    Sonntag in der Weihnachtsoktav. Gibt es den nicht (das bedeutet, dass kein
    Sonntag zwischen Weihnachten und Neujahr fällt, was nur möglich ist, wenn
    Weihnachten an einem Sonntag stattfindet), wird am 30.12. gefeiert.
    """

    def _reference(self, year: int) -> date:
        christmas = date(year, 12, 25)
        if christmas.isoweekday() == 7: return date(year, 12, 30)
        return christmas + timedelta(days=7 - christmas.isoweekday())


class OsterFest(DeltaFest):
    """
    Feste, die in Abhängigkeit von Ostern stehen, werden mit dieser Klasse
    bezeichnet. Dabei wird die Anzahl an Tagen angegeben, die das Fest sich von
    Ostersonntag unterscheidet.
    """

    def _reference(self, year: int) -> date:
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return date(year, month, day)


class TaufeDesHerrnFest(DeltaFest):
    """
    Feste, die in Bezug auf das Fest „Taufe des Herrn“ stehen, werden hier
    zusammengefasst. Taufe des Herrn fällt immer auf den Sonntag nach
    Erscheinung des Herrn (6. Januar).
    """

    def _reference(self, year: int) -> date:
        epiphany = date(year, 1, 6)
        delta = 7 - epiphany.isoweekday()
        if delta == 0: delta = 7
        return epiphany + timedelta(days=delta)
