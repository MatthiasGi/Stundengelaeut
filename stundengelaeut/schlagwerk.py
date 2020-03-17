from stundengelaeut.notes import *
from stundengelaeut.today import Today

from datetime import datetime
from datetime import timedelta

class Schlagwerk:
    """
    Klasse, die das Schlagwerk der Uhr simuliert. Hier wird das eigentliche
    Stundengeläut ausgelöst.

    Attributes
    ----------
    carillon : stundengelaeut.carillon.Carillon
        Das Carillon-Objekt, auf dem die Schläge ausgeführt werden sollen.
    """
    def __init__(self, carillon):
        self.carillon = carillon

        self.trinitatis = A1SHARP
        self.maria      = C2SHARP
        self.josef      = D2SHARP
        self.apostel    = F2SHARP
        self.bernhard   = G2SHARP
        self.engel      = A2SHARP

    def tellQuarters(self, quarters):
        """
        Schlägt eine Anzahl an Viertelstunden an. Beachtet dabei, ob es heute
        ein begangenes Fest mit ausreichendem Rang gibt (siehe
        stundengelaeut.today.Today#celebration()).

        Parameters
        ----------
        quarters : int
            Anzahl an Viertelstunden, die es zu schlagen gilt.
        """
        for i in range(quarters):
            if Today.celebration():
                self.carillon.playMelody([
                    [0.5, self.engel],
                    [0.5, self.bernhard],
                    [1.5, self.apostel]
                ])
            else:
                self.carillon.playMelody([[2, self.engel]])

    def tellHours(self, hours):
        """
        Schlägt eine Anzahl an Stunden an.

        Parameters
        ----------
        hours : int
            Anzahl an Stunden, die es zu schlagen gilt.
        """
        for i in range(hours): self.carillon.playMelody([[2.5, self.trinitatis]])

    def tellTime(self, t = datetime.now(), complete = False):
        """
        Lässt die aktuelle Zeit anschlagen. Dabei erhält jede volle
        Viertelstunde einen Viertelstundenschlag, jede Stunde einen
        Stundenschlag. Die Anzahl der Schläge ist durch #roundQuarter(t)
        bestimmt.

        Parameters
        ----------
        t : datetime.datetime (optional)
            Zeit die anzuschlagen ist. Wenn keine Zeit übergeben wird, wird die
            aktuelle Zeit genutzt.
        complete : bool (optional)
            Ob der Stundenschlag in jedem Falle erfolgen soll. Ansonsten erfolgt
            er standardmäßig nur zur vollen Stunde.
        """
        quarters, hours = Schlagwerk.roundQuarter(t)
        self.tellQuarters(quarters)
        if quarters == 4 or complete: self.tellHours(hours)

    @staticmethod
    def roundQuarter(t = datetime.now()):
        """
        Methode, die die aktuelle Zeit auf die nächste Viertelstunde rundet und
        die Anzahl an Stunden und Viertelstunden für einen Stundenschlag daraus
        ermittelt.

        Parameters
        ----------
        t : datetime.datetime (optional)
            Objekt, das für die Rundung genutzt werden soll. Bei Nichtangabe
            wird der aktuelle Zeitpunkt gewählt.

        Returns
        -------
        quarters : int
            Anzahl der Viertelstundenschläge, die nach der Rundung entstehen.
        hours : int
            Anzahl der Stundenschläge, die nach der Rundung entstehen.
        """
        dt = t + timedelta(minutes = 7, seconds = 30)
        dt -= timedelta(minutes = dt.minute % 15)

        quarters = int(dt.minute / 15)
        if quarters == 0: quarters = 4
        hours = dt.hour % 12
        if hours == 0: hours = 12

        print(t, "->", dt.time, ";", quarters, ":", hours) # TODO: Debug
        return quarters, hours
