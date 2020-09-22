import time

class Carillon:
    """
    Diese Klasse abstrahiert die MIDI-Schnittstelle dahingehend, dass ein Geläut
    simuliert werden kann. Die Noten (vgl. notes.py) werden hier ausgelöst und
    als Glocken virtuell angeschlagen, ferner können auch Melodien gespielt
    werden. Um den Umfang der Klasse gering zu halten, wird auf umfangreiche
    Tests verzichtet. Stattdessen wird darauf vertraut, dass der Programmierer
    zuvor die Eingabedaten entsprechend bereinigt.

    Attributes
    ----------
    midiout : object
        MIDI-Out-Objekt der rtmidi-Bibliothek. Dabei muss bereits ein Port
        geöffnet sein, es werden hier einfach Signale ausgegeben.
    channel : int (optional)
        MIDI-Kanal, auf dem die Signale später ausgegeben werden sollen.
    """
    def __init__(self, midiout, channel = 1):
        self.midiout = midiout
        self.channelAdder = channel - 1

    def noteOn(self, note, velocity = 127):
        """
        Sendet ein Note-An-Signal an das im Konstruktor übergebene
        MIDI-Out-Objekt.

        Parameters
        ----------
        note : int
            Note, die ausgelöst werden soll.
        velocity : int (optional)
            Velocity-Wert, der optional mit übergeben werden kann, um ihn in das
            MIDI-Signal einzubauen.
        """
        msg = [0x90 + self.channelAdder, note, velocity]
        self.midiout.send_message(msg)

    def noteOff(self, note, velocity = 0):
        """
        Sendet ein Note-Aus-Signal an das im Konstruktor übergebene
        MIDI-Out-Objekt.

        Parameters
        ----------
        note : int
            Note, die abgeschaltet werden soll.
        velocity : int (optional)
            Velocity-Wert, der optional mit übergeben werden kann, um ihn in das
            MIDI-Signal einzubauen.
        """
        msg = [0x80 + self.channelAdder, note, velocity]
        self.midiout.send_message(msg)

    def hitBell(self, note):
        """
        Löst einen einzelnen Ton aus und simuliert damit das Anschlagen einer
        Glocke.

        Parameters
        ----------
        note : int
            Note, die angeschlagen werden soll.
        """
        self.noteOn(note)
        self.noteOff(note)

    def playMelody(self, melody):
        """
        Spielt eine Melodie, die als Liste kodiert wird. Diese besteht aus
        Arrays, deren erstes Element die Dauer in Sekunden beinhaltet, die der
        Dauer eines Tones entspricht (genauer: die Zeit, die nach dem Anschlagen
        des Tones gewartet werden soll), und deren zweites Element der Tonhöhe
        entspricht.

        Parameters
        ----------
        melody : list of arrays
            Melodie als Liste kodiert, wie oben in der Beschreibung ausgeführt.
        """
        for m in melody:
            self.hitBell(m[1])
            time.sleep(m[0])

    def volume(self, volume):
        """
        Setzt die Lautstärke des Geläuts, indem ein Lautstärkepedal simuliert
        wird.

        Parameters
        ----------
        volume : int
            Gewünschte Lautstärke 0-127.
        """
        msg = [0xB0 + self.channelAdder, 1, volume]
        self.midiout.send_message(msg)
