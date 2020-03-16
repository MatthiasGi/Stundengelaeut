from stundengelaeut.carillon import Carillon
from stundengelaeut.schlagwerk import Schlagwerk
from stundengelaeut.melodies import lourdes_lied
from stundengelaeut.today import Today
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
        das nicht.
    """
    def __init__(self, midiout, channel = 1, stumm = False):
        self.carillon = Carillon(midiout, channel)
        self.stumm = stumm
        self.schlagwerk = Schlagwerk(self.carillon)

        schedule.every().day.at("08:00").do(self.morgen)
        schedule.every().day.at("21:00").do(self.abend)

        schedule.every().hour.at(":15").do(self.schlaege)
        schedule.every().hour.at(":30").do(self.schlaege)
        schedule.every().hour.at(":45").do(self.schlaege)
        schedule.every().hour.at(":00").do(self.schlaege)

        schedule.every().day.at("12:00").do(self.mittag)

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
        wird deaktiviert).
        """
        self.stumm = False

    def update(self):
        """
        Ist regelmäßig aufzurufen, um die Abarbeitung der automatischen Geläut-
        Vorgänge vorzunehmen.
        """
        schedule.run_pending()
