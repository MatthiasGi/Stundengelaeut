"""Sammlung von Melodien im richtigen Format für die anderen Teile

Die verwendeten Melodien (im Einzelnen sind dies die marianischen Antiphonen)
werden hier im kompatiblen Format für schnelle Aufrufe vorgehalten.
"""

from stundengelaeut.notes import *

# Voreingestellte Dauer einer Achtel-Note
def achtel():
    return 0.25

def regina_caeli(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [viertel, F3], # Regina caeli, laetare
        [viertel, G3],
        [viertel, F3],
        [viertel, G3],
        [viertel, A3],
        [viertel, A3SHARP],
        [viertel, A3],
        [halbe, G3],
        [viertel, A3SHARP], # Alleluia
        [viertel, A3],
        [viertel, G3],
        [halbe, F3],
        [viertel, F3], # quia, quem meruisti portare
        [viertel, C4],
        [viertel, C4],
        [viertel, D4],
        [viertel, C4],
        [viertel, A3SHARP],
        [viertel, A3],
        [viertel, F3],
        [viertel, G3],
        [halbe, A3],
        [viertel, A3SHARP], # Alleluia
        [viertel, A3],
        [viertel, G3],
        [halbe, F3],
        [viertel, C4], # resurrexit, sicut dixit
        [viertel, C4],
        [viertel, D4],
        [viertel, C4],
        [viertel, C4],
        [viertel, F3],
        [viertel, G3],
        [halbe, F3],
        [viertel, G3], # Alleluia
        [viertel, A3],
        [viertel, A3SHARP],
        [halbe, C4],
        [viertel, C4], # ora pro nobis Deum
        [viertel, F3],
        [viertel, G3],
        [viertel, A3SHARP],
        [viertel, A3],
        [viertel, G3],
        [halbe, F3],
        [viertel, E3], # Alleluia
        [viertel, G3],
        [halbe, G3],
        [ganze, F3]
    ]

def lourdes_lied(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [viertel, E3], # Die Glocken verkünden
        [viertel, A3],
        [viertel, A3],
        [viertel, C4SHARP],
        [viertel, A3],
        [viertel, A3],
        [viertel, C4SHARP], # mit fröhlichem Laut
        [viertel, B3],
        [viertel, B3],
        [achtel, C4SHARP],
        [achtel, B3],
        [halbe, A3],
        [viertel, E3], # Das Ave Maria
        [viertel, A3],
        [viertel, A3],
        [viertel, C4SHARP],
        [viertel, A3],
        [viertel, A3],
        [viertel, C4SHARP], # so lieblich und laut
        [viertel, B3],
        [viertel, B3],
        [achtel, C4SHARP],
        [achtel, B3],
        [halbe, A3],
        [viertel, A3], # Ave
        [halbe, D4],
        [viertel, D4], # Ave
        [halbe, C4SHARP],
        [viertel, C4SHARP], # Ave Maria
        [viertel, B3],
        [viertel, B3],
        [viertel, B3],
        [halbe, E4],
        [viertel, C4SHARP], # Ave
        [halbe, D4],
        [viertel, D4], # Ave
        [halbe, C4SHARP],
        [viertel, C4SHARP], # Ave Maria
        [viertel, B3],
        [viertel, B3],
        [achtel, C4SHARP],
        [achtel, B3],
        [ganze, A3]
    ]
