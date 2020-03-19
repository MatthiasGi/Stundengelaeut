from stundengelaeut.feste.fest import Fest
from datetime import timedelta

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
    name : str
        Name des Festes.
    rang : .rang.Rang
        Rang des Festes
    """
    def __init__(self, days, name, rang):
        self._delta = timedelta(days = days)
        self._name = name
        self._rang = rang

    def rang(self):
        """@inheritDoc"""
        return self._rang

    def name(self):
        """@inheritDoc"""
        return self._name

    def referenceDate(self, year):
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

        Raises
        ------
        NotImplementedError
            Da die Methode abstrakt ist, wirft sie diesen Fehler. Kindklassen
            haben die Implementierung vorzunehmen.
        """
        raise NotImplementedError

    def isDate(self, d):
        """@inheritDoc"""
        return self.referenceDate(d.year) + self._delta == d
