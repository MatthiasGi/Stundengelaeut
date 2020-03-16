from enum import Enum, unique

@unique
class Rang(Enum):
    """
    Diese Auflistung klassifiziert den Rang von Festen eindeutig und erlaubt
    eine Unterscheidung dazwischen.
    """
    HOCHFEST = 10
    SONDERTAG = 19
    SONNTAG = 20
    FEST = 30
    GEBOTENER_GEDENKTAG = 40
    OKTAVTAG = 50
    NICHTGEBOTENER_GEDENKTAG = 60
    GEPRAEGTE_ZEIT = 70
