from datetime import date
from datetime import timedelta

from stundengelaeut.festmanager import FestManager
from stundengelaeut.feste.rang import Rang

class Today:
    """
    Statische Klasse, die Informationen zum heutigen Tage zusammenträgt und
    gegebenenfalls aktualisiert.
    """

    """
    Letzter Tag, an dem die Aktualisierung durchgeführt wurde. Wird
    zwischengespeichert, damit nur einmal pro Tag geupdatet wird.
    """
    _lastupdate = date.today() + timedelta(days = -1)

    """Aktuelle Antiphon, die wiedergegeben werden soll."""
    _antiphon = None

    """Fest, das am heutigen Tage begangen wird."""
    _feast = None

    """Ob das Stundengeläut heute schweigen soll."""
    _mute = False

    @staticmethod
    def check():
        """
        Überprüft, ob heute bereits ein Update stattgefunden hat. Falls nicht,
        werden aktuellere Daten aus dem FestManager übernommen.
        """
        if Today._lastupdate >= date.today(): return
        Today._lastupdate = date.today()
        Today._antiphon = FestManager.antiphon()
        Today._feast = FestManager.fest()
        Today._mute = FestManager.mute()

    @staticmethod
    def antiphon():
        """
        Gibt die aktuell zu spielende marianische Antiphon zurück.

        Returns
        -------
        Die aktuell zu spielende Antiphon.
        """
        Today.check()
        return Today._antiphon

    @staticmethod
    def feast():
        """
        Gibt das heute begangene Fest zurück.

        Returns
        -------
        Das heute begangene Fest (oder eben None, wenn keines stattfindet).
        """
        Today.check()
        return Today._feast

    @staticmethod
    def celebration():
        """
        Gibt zurück, ob heute ein Feiertag mit ausreichendem Rang begangen wird,
        damit von dem normalen Läutschema abgewichen werden kann.

        Returns
        -------
        Ob heute ein „begangenes“ Fest stattfindet.
        """
        Today.check()
        if Today._feast == None: return False
        return Today._feast.rang() >= Rang.NICHTGEBOTENER_GEDENKTAG

    @staticmethod
    def mute():
        Today.check()
        return Today._mute
