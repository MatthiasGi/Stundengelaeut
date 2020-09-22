from datetime import (date, timedelta)
from abc import abstractmethod

from .fest import Fest
from .rang import Rang


class DeltaFest(Fest):
    """
    Feste, die in Abhängigkeit zu einem anderen Fest stehen, werden in dieser
    abstrakten Klasse zusammengefasst, um Wiederholungen zu vermeiden. Dabei
    wird die Anzahl an Tagen angegeben, in denen dieses Fest von einem anderen
    abweicht.

    Attributes
    ----------
    days : int
        Unterschied in Anzahl von Tagen in Bezug auf ein anderes Fest.

    Methods
    -------
    _reference : date
        Interne Methode für Subklassen: Refernzdatum in einem spezifizierten
        Jahr.
    """

    def __init__(self, days: int, name: str, rang: Rang):
        self._delta = timedelta(days=days)
        self._name = name
        self._rang = rang

    @property
    def rang(self) -> Rang:
        return self._rang

    @property
    def name(self) -> str:
        return self._name

    def _happens(self, d: date) -> bool:
        return self._reference(d.year) + self._delta == d

    @abstractmethod
    def _reference(self, year: int) -> date:
        """
        Referenzfest, an dem die Tagesdifferenz für ein bestimmtes Jahr
        auszurichten ist (wäre das Referenzfest unabhängig von der Jahreszahl,
        wäre .tagfest.TagFest bereits eine ausreichende Implementation).

        Parameters
        ----------
        year : int
            Jahreszahl, für die das Referenzdatum ermittelt werden soll.

        Returns
        -------
        Hat das Refernzdatum als datetime.date-Objekt für das selektierte Jahr
        auszugeben.
        """
        pass
