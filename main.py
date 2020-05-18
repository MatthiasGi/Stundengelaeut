from stundengelaeut.stundengelaeut import Stundengelaeut
import rtmidi
import time

midiout = rtmidi.MidiOut()
midiout.open_port(len(midiout.get_ports()) - 1)
s = Stundengelaeut(midiout)

while True:
    s.update()
    time.sleep(2)
