from deltafest import DeltaFest
from datetime import date
from datetime import timedelta

class AdventsFest(DeltaFest):
    """
    Feste, die in Abhängigkeit vom ersten Advent stehen, werden mit dieser
    Klasse bezeichnet. Dabei wrid die Anzahl an Tagen angegeben, die das Fest
    sich vom ersten Advent unterscheidet.
    """

    def referenceDate(self, year):
        """@inheritDoc"""
        christmas = date(year, 12, 25)
        return christmas + timedelta(days = -christmas.isoweekday() - 7*3)
