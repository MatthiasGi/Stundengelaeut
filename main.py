from stundengelaeut.stundengelaeut import Stundengelaeut
import rtmidi
import time
import os.path

midiout = rtmidi.MidiOut()
midiout.open_port(len(midiout.get_ports()) - 1)
s = Stundengelaeut(midiout)

while True:
    s.update()
    if os.path.exists('mute.ctrl'):
        s.mute()
    else:
        s.unmute()
    time.sleep(2)
