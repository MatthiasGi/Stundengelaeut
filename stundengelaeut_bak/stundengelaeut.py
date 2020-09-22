from stundengelaeut.carillon import Carillon
from stundengelaeut.schlagwerk import Schlagwerk
from stundengelaeut.melodies import lourdes_lied
from stundengelaeut.today import Today

from datetime import (datetime, time)
import schedule

class Stundengelaeut:
    """
    Diese Klasse fasst die Einrichtung des eigentlichen Geläuts übersichtlich
    zusammen.

    Attributes
    ----------
    midiout : rtmidi.MidiOut
        MidiOut-Objekt mit geöffnetem Port, der genutzt werden soll.
    channel : int (optional)
        Midi-Kanal, auf dem die Töne ausgegeben werden sollen. Standardmäßig
        wird Kanal 1 genutzt.
    stumm : bool (optional)
        Ob das Stundengeläut im stummen Modus starten soll. Standardmäßig tut es
        das abhängig von der Zeit.
    """
    def __init__(self, midiout, channel = 1, stumm = False):
        self.carillon = Carillon(midiout, channel)
        self.stumm = stumm
        if not stumm: self._check_stumm()
        self.schlagwerk = Schlagwerk(self.carillon)

        schedule.every().day.at("08:00").do(self.morgen)
        schedule.every().day.at("21:00").do(self.abend)

        schedule.every().hour.at(":15").do(self.schlaege)
        schedule.every().hour.at(":30").do(self.schlaege)
        schedule.every().hour.at(":45").do(self.schlaege)
        schedule.every().hour.at(":00").do(self.schlaege)

        schedule.every().day.at("12:00").do(self.mittag)

    def _check_stumm(self):
        """
        Interne Funktion, die prüft, ob das Geläut zur aktuellen Zeit stumm
        bleiben soll. Dabei wird die Uhrzeit und der Tag (Kartag?) mit bedacht.
        """
        if Today.mute(): self.stumm = True; return
        if datetime.now().time() < time(8, 0): self.stumm = True; return
        if datetime.now().time() > time(21, 0): self.stumm = True; return
        self.stumm = False

    def schlaege(self):
        """
        Führt die eigentlichen Schläge aus – sofern das Geläut nicht stumm
        gestellt ist.
        """
        if self.stumm: return
        self.schlagwerk.tellTime()

    def mittag(self):
        """
        Wird zur Mittagszeit aufgerufen und spielt die Lourdes-Hymne (sofern das
        Carillon nicht stumm gestellt ist).
        """
        if self.stumm: return
        self.carillon.playMelody(lourdes_lied())

    def abend(self):
        """
        Wird am Abend ausgeführt: Gibt einmal die komplette Zeit aus, spielt
        eine marianische Antiphon und stellt das Geläut dann stumm.
        """
        if self.stumm: return
        self.schlagwerk.tellTime(complete = True)
        self.carillon.playMelody(Today.antiphon())
        self.stumm = True

    def morgen(self):
        """
        Wird am morgen ausgeführt und aktiviert das Geläut wieder (stummer Modus
        wird deaktiviert), sofern anderes nicht dagegen spricht.
        """
        self._check_stumm()

    def update(self):
        """
        Ist regelmäßig aufzurufen, um die Abarbeitung der automatischen Geläut-
        Vorgänge vorzunehmen.
        """
        schedule.run_pending()

    def mute(self):
        """
        Setzt das Stundengeläut über einen zusätzlichen, externen Trigger aus.
        """
        self.stumm = True

    def unmute(self, automatic = True):
        """
        Schaltet das Stundengeläut anhand eines zusätzlichen, externen Trigger
        sofort wieder ein.

        Parameters
        ----------
        automatic : bool
            Ob für die Wiedereinschaltung die Rahmenbedingungen überprüft
            werden sollen. Ist dieser Wert True wird das Geläut z.B. dennoch
            Nachts oder während des Triduum Paschalis nicht angeschaltet.
        """
        self.stumm = False
        if automatic: self._check_stumm()
