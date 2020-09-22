"""
Führt das Stundengeläut aus und hat auch eine Klingelfunktion an einem GPIO-
Input.
"""

from stundengelaeut_bak.stundengelaeut import Stundengelaeut
from stundengelaeut_bak.melodies import macht_hoch_die_tuer

import board
import digitalio

import rtmidi
import time

midiout = rtmidi.MidiOut()
midiout.open_port(len(midiout.get_ports()) - 1)
s = Stundengelaeut(midiout)


def play_doorbell(button):
    idx = [0, 9, 18, 28, 38, 47, 56, 62, 69]
    melody = macht_hoch_die_tuer()
    parts = [melody[idx[i]:idx[i+1]] for i in range(len(idx) - 1)]

    while button.value:
        for p in parts:
            s.carillon.playMelody(p)
            if not button.value: return


doorbell = digitalio.DigitalInOut(board.D17)
doorbell.direction = digitalio.Direction.INPUT

while True:
    s.update()
    play_doorbell(doorbell)
    time.sleep(0.1)
