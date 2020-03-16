from stundengelaeut.stundengelaeut import Stundengelaeut
import rtmidi
import time

midiout = rtmidi.MidiOut()
midiout.open_port(0)
s = Stundengelaeut(midiout)

while True:
    s.update()
    time.sleep(0.2)
