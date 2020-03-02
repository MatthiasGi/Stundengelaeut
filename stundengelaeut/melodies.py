"""Sammlung von Melodien im richtigen Format für die anderen Teile

Die verwendeten Melodien (im Einzelnen sind dies die marianischen Antiphonen)
werden hier im kompatiblen Format für schnelle Aufrufe vorgehalten.
"""

from stundengelaeut import notes

# Voreingestellte Dauer einer Achtel-Note
def achtel():
    return 0.25

def regina_caeli(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [viertel, notes.F3], # Regina caeli, laetare
        [viertel, notes.G3],
        [viertel, notes.F3],
        [viertel, notes.G3],
        [viertel, notes.A3],
        [viertel, notes.A3SHARP],
        [viertel, notes.A3],
        [halbe, notes.G3],
        [viertel, notes.A3SHARP], # Alleluia
        [viertel, notes.A3],
        [viertel, notes.G3],
        [halbe, notes.F3],
        [viertel, notes.F3], # quia, quem meruisti portare
        [viertel, notes.C4],
        [viertel, notes.C4],
        [viertel, notes.D4],
        [viertel, notes.C4],
        [viertel, notes.A3SHARP],
        [viertel, notes.A3],
        [viertel, notes.F3],
        [viertel, notes.G3],
        [halbe, notes.A3],
        [viertel, notes.A3SHARP], # Alleluia
        [viertel, notes.A3],
        [viertel, notes.G3],
        [halbe, notes.F3],
        [viertel, notes.C4], # resurrexit, sicut dixit
        [viertel, notes.C4],
        [viertel, notes.D4],
        [viertel, notes.C4],
        [viertel, notes.C4],
        [viertel, notes.F3],
        [viertel, notes.G3],
        [halbe, notes.F3],
        [viertel, notes.G3], # Alleluia
        [viertel, notes.A3],
        [viertel, notes.A3SHARP],
        [halbe, notes.C4],
        [viertel, notes.C4], # ora pro nobis Deum
        [viertel, notes.F3],
        [viertel, notes.G3],
        [viertel, notes.A3SHARP],
        [viertel, notes.A3],
        [viertel, notes.G3],
        [halbe, notes.F3],
        [viertel, notes.E3], # Alleluia
        [viertel, notes.G3],
        [halbe, notes.G3],
        [ganze, notes.F3]
    ]
