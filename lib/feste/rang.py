from enum import Enum, unique
from functools import total_ordering


@unique
@total_ordering
class Rang(Enum):
    """
    Diese Auflistung klassifiziert den Rang von Festen eindeutig und erlaubt
    eine Unterscheidung dazwischen.

    Constants
    ---------
    HOCHFEST : int
    SONDERTAG : int
    SONNTAG : int
    FEST : int
    GEBOTENER_GEDENKTAG : int
    OKTAVTAG : int
    NICHTGEBOTENER_GEDENKTAG : int
    GEPRAEGTE_ZEIT : int
    """

    HOCHFEST = 70
    SONDERTAG = 63
    SONNTAG = 60
    FEST = 50
    GEBOTENER_GEDENKTAG = 40
    OKTAVTAG = 30
    NICHTGEBOTENER_GEDENKTAG = 20
    GEPRAEGTE_ZEIT = 10

    def __lt__(self, other: 'Rang'):
        """
        Erlaubt es, die Ränge gegeneinander abzuwägen. So kann entschieden
        werden, welches Fest überwiegt.

        Parameters
        ----------
        other : obj
            Objekt, mit dem verglichen werden soll.

        Returns
        -------
        Sofern das andere Objekt ebenfalls ein Rang-Objekt ist, wird der Inhalt
        verglichen. Ansonsten wird NotImplemented als Fehlerobjekt
        zurückgegeben.
        """
        if self.__class__ is not other.__class__: return NotImplemented
        return self.value < other.value
