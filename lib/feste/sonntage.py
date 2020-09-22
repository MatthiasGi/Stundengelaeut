from datetime import date

from .fest import Fest
from .rang import Rang


class Sonntage(Fest):
    """Zusammenfassung aller Sonntage."""

    @property
    def name(self) -> str:
        return 'Sonntag'

    @property
    def rang(self) -> Rang:
        return Rang.SONNTAG

    def _happens(self, d: date):
        return d.isoweekday() == 7
