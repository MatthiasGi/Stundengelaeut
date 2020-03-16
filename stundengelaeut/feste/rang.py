from enum import Enum, unique

@unique
class Rang(Enum):
    """
    Diese Auflistung klassifiziert den Rang von Festen eindeutig und erlaubt
    eine Unterscheidung dazwischen.
    """
    HOCHFEST = 10
    SONNTAG = 20
    FEST = 30
    GEBOTENER_GEDENKTAG = 40
    NICHTGEBOTENER_GEDENKTAG = 50
    GEPRAEGTE_ZEIT = 60
