from stundengelaeut.notes import *
from stundengelaeut import date

class Schlagwerk:
    def __init__(self, carillon):
        self.carillon = carillon

        self.trinitatis = A1SHARP
        self.maria      = C2SHARP
        self.josef      = D2SHARP
        self.apostel    = F2SHARP
        self.bernhard   = G2SHARP
        self.engel      = A2SHARP

    def tellQuarters(self, quarters):
        for i in range(quarters):
            if date.isCelebration():
                self.carillon.playMelody([
                    [0.5, self.engel],
                    [0.5, self.bernhard],
                    [1.5, self.apostel]
                ])
            else:
                self.carillon.playMelody([[2, self.engel]])

    def tellHours(self, hours):
        for i in range(hours): self.carillon.playMelody([[3, self.trinitatis]])
