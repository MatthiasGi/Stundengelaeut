import mido
import time


class Carillon:
    """
    Diese Klasse abstrahiert die MIDI-Schnittstelle dahingehend, dass sie ein
    spielbares Instrument zur Verfügung stellt.

    Attributes
    ----------
    port : object
        Das mido-Port-Objekt, an das die Nachrichten gesendet werden sollen.
    volume : int
        Eingestellte Lautstärke von 0-127. Startet bei 127.

    Methods
    -------
    hit(note)
        Schlägt eine übergebene Note an.
    play(self, path, basebpm=120, transpose=0)
        Spielt eine MIDI-Datei.
    """

    def __init__(self, port=None):
        """
        Erstellt das virtuelle Instrument zur Abstraktion von MIDI-Nachrichten.

        Parameters
        ----------
        port : object (optional)
            Mido-Portobjekt, auf das die Nachrichten ausgegeben werden sollen.
            Bei Nichtangabe, wird der Standardport genutzt.
        """
        if port is None: port = mido.open_output()
        self.port = port
        self.volume = 127

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value: int):
        if value < 0 or value > 127:
            raise ValueError('Lautstärke muss zwischen 0 und 127 liegen!')
        self._volume = value
        self.port.send(mido.Message('control_change', control=1, value=value))

    def hit(self, note) -> None:
        """
        Löst einen einzelnen Ton aus.

        Parameters
        ----------
        note : int
            Note, die angeschlagen werden soll.
        """
        self.port.send(mido.Message('note_on', note=note))
        self.port.send(mido.Message('note_off', note=note))

    def play(self, path, basebpm=120, transpose=0) -> None:
        """
        Spielt eine MIDI-Datei auf dem Carillon ab. Dabei wird die erste Spur
        verwendet.

        Parameters
        ----------
        path : str
            Pfad zur abzuspielenden MIDI-Datei.
        basebpm : int (optional)
            BPMs, die 120 entsprechen. Damit lässt sich das Stück beschleunigen
            oder verlangsamen.
        transpose : int (optional)
            Anzahl der Halbtöne, um die das Stück transponiert werden soll.
        """
        mid = mido.MidiFile(path)
        tempo = mido.bpm2tempo(basebpm)
        for msg in mid.tracks[0]:
            if msg.type == 'set_tempo':
                tempo = 120 / basebpm * msg.tempo
            if msg.type not in ('note_on', 'note_off'): continue
            time.sleep(mido.tick2second(msg.time, mid.ticks_per_beat, tempo))

            if msg.velocity == 0: continue
            self.hit(msg.note + transpose)
