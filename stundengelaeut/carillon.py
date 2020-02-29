class Carillon:

    midiout = None
    channelAdder = None

    def __init__(self, midiout, channel = 1):
        self.midiout = midiout
        self.channelAdder = channel - 1

    def noteOn(self, note, velocity = 127):
        msg = [0x90 + self.channelAdder, note, velocity]
        self.midiout.send_message(msg)

    def noteOff(self, note, velocity = 0):
        msg = [0x80 + self.channelAdder, note, velocity]
        self.midiout.send_message(msg)
