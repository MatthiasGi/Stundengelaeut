from abc import (ABC, abstractmethod)
from datetime import date

from .rang import Rang


class Fest(ABC):
    """
    Die abstrakte Klasse Fest liefert einen Rahmen für Informationen zu einem
    spezifischen Fest. Sie ist dabei so angelegt, dass die Grundinformationen
    durch Unterklassen, die sich an den eigentlichen Kirchenfesten orientieren,
    verbindlich abgefragt werden können.

    Attributes
    ----------
    name : str
        Name des repräsentierten Festes.
    rang : Rang
        Rang des repräsentierten Festes.

    Methods
    -------
    happens(d) : bool
        Gibt an, ob das Fest am übergebenen Tag stattfindet.
    _happens(d) : bool
        Interne Methode, die zur Ermittlung des Datums durch Subklassen
        implementiert werden muss.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Soll den Namen des durch die Instanz repräsentierten Festes
        zurückgeben.
        """
        pass

    @property
    @abstractmethod
    def rang(self) -> Rang:
        """
        Soll den Rang des durch die Instanz repräsentierten Festes zurückgeben.
        """
        pass

    def happens(self, d: date = None) -> bool:
        """
        Methode, die angibt, ob am übergebenen Datum das bestimmte Fest
        stattfindet.

        Parameters
        ----------
        d : date (optional)
            Datum, das überprüft werden soll. Wird keins übergeben, wird der
            heutige Tag verwendet.

        Returns
        -------
        Ob das Fest am gegebenen Tag stattfindet.
        """
        if d is None: d = date.today()
        return self._happens(d)

    @abstractmethod
    def _happens(self, d: date) -> bool:
        """
        Abstrakte, interne Methode, die angeben soll, ob am übergebenen Datum
        das genannte Fest stattfindet.

        Parameters
        ----------
        d : date
            Datum, das überprüft werden soll.

        Returns
        -------
        Hat einen Bool-Wert zurückzugeben, der angibt, ob das Fest am gegebenen
        Tag stattfindet.
        """
        pass
