from datetime import (date, datetime, timedelta)

from .feste import (Fest, Manager, Rang)
from .striker import (Striker, StrikeObserver)


class Today:
    """
    Statische Klasse, die den heutigen Tag wiederspiegelt und Informationen
    dazu cached.

    Static attributes
    -----------------
    _antiphon : str
        Name der aktuellen Antiphon.
    _fest : Fest
        Aktuell begangenes Fest.
    _lastupdate : date
        Letztes Aktualisierungsdatum.
    _muted : bool
        Ob das Stundengeläut schweigen soll.

    Static methods
    --------------
    antiphon() : str
        Name der aktuellen Antiphon.
    fest() : Fest
        Begangenes Fest.
    festive() : bool
        Ob der heutige Tag als Fest begangen wird.
    infuse(striker)
        Hält ein Schlagwerk über den Tageszustand informiert.
    muted() : bool
        Ob das Stundengeläut am heutigen Tage schweigen soll.
    _check()
        Interne Methode zur ggf. nötigen Aktualisierung der Daten.
    """

    """Aktuell abzuspielende Antiphon."""
    _antiphon = None

    """Heute begangenes Fest."""
    _fest = None

    """Letzter Aktualisierungszeitpunkt."""
    _lastupdate = date.today() + timedelta(days=-1)

    """Ob das Stundengeläut heute schweigen soll."""
    _muted = False

    @staticmethod
    def antiphon() -> str:
        """Gibt die aktuelle marianische Antiphon zurück."""
        Today._check()
        return Today._antiphon

    @staticmethod
    def fest() -> Fest:
        """Gibt das heute begangene Fest zurück."""
        Today._check()
        return Today._fest

    @staticmethod
    def festive() -> bool:
        """
        Gibt zurück, ob heute ein Feiertag mit ausreichend Rang begangen wird,
        damit von dem normalen Läutschema abgewichen werden kann.

        Returns
        -------
        Ob der heutige Tag festlich begangen wird.
        """
        if Today.fest() is None: return False
        return Today.fest().rang >= Rang.NICHTGEBOTENER_GEDENKTAG

    @staticmethod
    def infuse(striker: Striker) -> None:
        """
        Fügt einem Schlagwerk einen Beobachter hinzu, der die tagesaktuelle
        Lage dort weitergibt.

        Parameters
        ----------
        striker : Striker
            Schlagwerk, das upgedatet werden soll.
        """
        striker.attach_observer(_TodayObserver())

    @staticmethod
    def muted() -> bool:
        """Gibt zurück, ob das Stundengeläut heute schweigen soll."""
        Today._check()
        return Today._muted

    @staticmethod
    def _check() -> None:
        """
        Überprüft, ob heute bereits ein Update stattgefunden hat. Andernfalls
        werden die statischen Attribute aus dem Manager übernommen.
        """
        if Today._lastupdate >= date.today(): return
        Today._lastupdate = date.today()
        Today._antiphon = Manager.antiphon()
        Today._fest = Manager.fest()
        Today._muted = Manager.muted()


class _TodayObserver(StrikeObserver):
    """
    Interne Klasse, die ein Schlagwerk über den Tageszustand informieren kann.
    """

    def pre_strike(self, striker: 'Striker', time: datetime) -> bool:
        striker.festive = Today.festive()
        return not Today.muted()

    def post_strike(self, striker: 'Striker', time: datetime) -> None:
        pass
