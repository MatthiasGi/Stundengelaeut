from abc import (ABC, abstractmethod)
from datetime import (datetime, timedelta)
import schedule
from threading import Thread
import time

from .carillon import Carillon


class Striker:
    """
    Klasse, die den automatischen Schlagmechanismus der Uhr simuliert. Hier
    wird das eigentliche Stundengeläut ausgelöst.

    Attributes
    ----------
    active : bool
        Ob das Schlagwerk gerade schlagend ist.
    carillon : Carillon
        Das Carillon-Objekt, auf dem die Schläge ausgeführt werden sollen.
    festive : bool
        Ob eine feierliche Form des Schlages genutzt werden soll.
    quarters : bool
        Ob Viertelstundenschläge ausgeführt werden sollen.
    _observers : list
        Liste mit StrikeObserver-Klassen, die über automatische Schläge
        informiert werden sollen.

    Constants
    ---------
    TRINITATIS : int
        Ton der Trinitatis-Glocke (A1#)
    MARIA : int
        Ton der Maria-Glocke (C2#)
    JOSEF : int
        Ton der Josefs-Glocke (D2#)
    APOSTEL : int
        Ton der Apostel-Glocke (F2#)
    BERNHARD : int
        Ton der Bernhard-Glocke (G2#)
    ENGEL : int
        Ton der Engel-Glocke (A2#)

    Methods
    -------
    attach_observer(observer)
        Fügt einen StrikeObserver hinzu, der über Schläge informiert wird.
    remove_observer(observer)
        Entfernt einen StrikeObserver.
    strike_quarters(n)
        Schlägt eine Anzahl an Viertelstunden.
    strike_hours(n)
        Schlägt eine Anzal an Stunden.
    strike(time, notify, complete)
        Schlägt eine konkrete Zeit an.
    play(*params, **kwargs)
        Spielt eine Melodie mit Aussetzendem Stundengeläut.
    _thread()
        Interne Thread-Methode, die das automatische Schlagen sicherstellt.
    """

    TRINITATIS = 0x22  # A1SHARP
    MARIA = 0x25       # C2SHARP
    JOSEF = 0x27       # D2SHARP
    APOSTEL = 0x2A     # F2SHARP
    BERNHARD = 0x2C    # G2SHARP
    ENGEL = 0x2E       # A2SHARP

    def __init__(self, carillon: Carillon):
        """
        Erstellt das Schlagwerk und weist ihm ein Carillon zu.

        Parameters
        ----------
        carillon : Carillon
            Carillon, auf dem geschlagen werden soll.
        """
        self.carillon = carillon
        self.active = True
        self.festive = False
        self.quarters = True
        self._observers = []

        for t in range(0, 60, 15):
            schedule.every().hour.at(':%02d' % t).do(self.strike)

        t = Thread(target=self._thread, daemon=True)
        t.start()

    def attach_observer(self, observer: 'StrikeObserver') -> None:
        """
        Fügt einen StrikeObserver hinzu, der über automatisierte Schläge
        informiert werden soll.

        Parameters
        ----------
        observer : StrikeObserver
            Der hinzuzufügende Beobachter.
        """
        self._observers.append(observer)

    def remove_observer(self, observer: 'StrikeObserver') -> None:
        """
        Entfernt einen Beobachter, er wird im Anschluss nicht mehr über Schläge
        informiert.

        Parameters
        ----------
        observer : StrikeObserver
            Der zu entfernende Beobachter.
        """
        self._observers.remove(observer)

    def strike_quarters(self, n: int) -> None:
        """
        Schlägt eine Anzahl an Viertelstunden (sofern diese nicht global
        deaktiviert sind).

        Parameters
        ----------
        n : int
            Anzahl der Viertelstunden, die angeschlagen werden sollen.
        """
        if not self.quarters: return
        for i in range(n):
            if not self.active: return
            if self.festive:
                self.carillon.hit(Striker.ENGEL)
                time.sleep(0.5)
                self.carillon.hit(Striker.BERNHARD)
                time.sleep(0.5)
                self.carillon.hit(Striker.APOSTEL)
                time.sleep(1.5)
            else:
                self.carillon.hit(Striker.ENGEL)
                time.sleep(2)

    def strike_hours(self, n: int) -> None:
        """
        Schlägt eine Anzahl an Stunden.

        Parameters
        ----------
        n : int
            Anzahl der Stunden, die angeschlagen werden sollen.
        """
        for i in range(n):
            if not active: return
            self.carillon.hit(Striker.TRINITATIS)
            time.sleep(2.5)

    def strike(
        self, time: datetime = None, notify: bool = True,
        complete: bool = False
    ) -> None:
        """
        Schlägt eine Zeit an.

        Parameters
        ----------
        time : datetime (optional)
            Die anzuschlagende Zeit. Wenn keine Zeit übergeben wird, wird die
            aktuelle Zeit angenommen.
        notify : bool (optional)
            Ob die StrikeObserver über den Schlag informiert werden sollen
            (standardmäßig der Fall). Dieses Argument kann z.B. benutzt werden,
            wenn der Strike abgewandelt werden soll, um neuerliche
            Informationen zu verhindern.
        complete : bool (optional)
            Ob in jedem Falle die Stunden mit angegeben werden sollen. Dies ist
            standardmäßig der Fall, wenn vier Viertelstundenschläge voran
            gehen.
        """
        if time is None: time = datetime.now()

        # Zeit auf nächste Viertelstunde runden
        dt = time + timedelta(minutes=7, seconds=30)
        dt -= timedelta(minutes=dt.minute % 15, seconds=dt.second,
                        microseconds=dt.microsecond)

        # Anzahl Stunden- und Viertelstundenschläge extrahieren
        quarters = int(dt.minute / 15)
        if quarters == 0: quarters = 4
        hours = dt.hour % 12
        if hours == 0: hours = 12

        # Falls erforderlich, Beobachter informieren und Schlag ausführen
        for o in self._observers:
            if notify and not o.pre_strike(self, dt): return
        self.strike_quarters(quarters)
        if quarters % 4 == 0 or complete: self.strike_hours(hours)
        if notify:
            for o in self._observers: o.post_strike(self, dt)

    def play(self, *params, **kwargs) -> None:
        """
        Spielt eine Melodie auf dem Carillon und stellt sicher, dass diese
        nicht von Stundenschlägen unterbrochen wird. Parameter werden
        unverändert an Carillon#play weitergereicht.
        """
        cache = self.active
        self.active = False
        self.carillon.play(*params, **kwargs)
        schedule.run_pending()
        self.active = cache

    def _thread(self):
        """
        Interne Methode, die als Thread ausgeführt wird und das automatische
        Schlagen sicherstellt.
        """
        while True:
            schedule.run_pending()
            time.sleep(1)


class StrikeObserver(ABC):
    """
    Abstrakte Klasse, die Methoden definiert, mit der einzelne Klassen über
    bevorstehende oder stattgefundene Schläge des Schlagwerks informiert.

    Methods
    -------
    pre_strike(striker, time) : bool
        Methode, die vor dem Schlagen ausgeführt wird.
    post_strike(striker, time)
        Methode, die nach dem Schlagen ausgeführt wird.
    """

    @abstractmethod
    def pre_strike(self, striker: Striker, time: datetime) -> bool:
        """
        Wird aufgerufen, bevor ein automatischer Schlag ausgeführt werden. Über
        den Rückgabewert kann gesteuert werden, ob das Schlagen tatsächlich
        stattfindet.

        Parameters
        ----------
        striker : .striker.Striker
            Schlagwerk, das die Methode auslöst.
        time : datetime
            Zeit, die angeschlagen werden soll.

        Returns
        -------
        Ein Boolean-Wert, der angibt, ob die weitere Ausführung stattfinden
        soll.
        """
        pass

    @abstractmethod
    def post_strike(self, striker: Striker, time: datetime) -> None:
        """
        Sobald der Schlag ausgeführt wurde, wird hier diese Methode aufgerufen.

        Parameters
        ----------
        striker : .striker.Striker
            Schlagwerk, das die Methode auslöst.
        time : datetime
            Zeit, die angeschlagen wurde.
        """
        pass
