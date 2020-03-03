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

def ave_regina_caelorum(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [viertel, F3], # Ave Regina caelorum
        [viertel, E3],
        [viertel, D3],
        [viertel, C3],
        [viertel, D3],
        [viertel, F3],
        [viertel, G3],
        [halbe, F3],
        [viertel, A3], # ave Domina angelorum
        [viertel, C4],
        [viertel, A3SHARP],
        [viertel, G3],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [viertel, A3],
        [halbe, G3],
        [viertel, F3], # salve radix, salve porta
        [viertel, E3],
        [viertel, D3],
        [viertel, C3],
        [viertel, D3],
        [viertel, F3],
        [viertel, G3],
        [halbe, F3],
        [viertel, A3], # ex qua mundo lux est orta
        [viertel, G3],
        [viertel, A3SHARP],
        [viertel, A3],
        [viertel, G3],
        [viertel, D3],
        [viertel, G3],
        [halbe, F3],
        [viertel, F3], # Gaude Virgo gloriosa
        [viertel, G3],
        [viertel, A3],
        [viertel, A3],
        [viertel, G3],
        [viertel, A3],
        [viertel, A3SHARP],
        [halbe, A3],
        [viertel, C4], # super omnes speciosa
        [viertel, A3SHARP],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [viertel, D3],
        [viertel, G3],
        [halbe, F3],
        [viertel, A3SHARP], # vale, o valde decora
        [viertel, A3],
        [viertel, G3],
        [viertel, A3SHARP],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [viertel, G3],
        [viertel, A3],
        [halbe, A3],
        [viertel, C4], # et pro nobis Christum exora
        [viertel, A3SHARP],
        [viertel, A3SHARP],
        [viertel, C4],
        [viertel, D4],
        [viertel, A3],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [halbe, G3],
        [ganze, F3]
    ]

def alma_redemptoris(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [achtel, C3], # Alma redemptoris mater
        [achtel, E3],
        [achtel, F3],
        [achtel, G3],
        [viertel, A3],
        [viertel, G3],
        [viertel, G3],
        [viertel, G3],
        [viertel, A3],
        [viertel, B3],
        [viertel, C4],
        [halbe, G3],
        [viertel, E3], # quad pervia caeli porta manes
        [viertel, E3],
        [viertel, E3],
        [viertel, F3],
        [viertel, E3],
        [viertel, D3],
        [viertel, E3],
        [viertel, F3],
        [viertel, A3],
        [halbe, G3],
        [viertel, A3], # et stella maris
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [halbe, G3],
        [viertel, E3], # succurre cadenti
        [viertel, F3],
        [viertel, E3],
        [viertel, D3],
        [viertel, E3],
        [halbe, G3],
        [viertel, E3], # surgery qui curat, populo
        [viertel, F3],
        [viertel, G3],
        [viertel, A3],
        [viertel, C4],
        [viertel, B3],
        [viertel, D3],
        [viertel, C3],
        [halbe, C3],
        [viertel, C4], # Tu quae genuisti
        [viertel, B3],
        [viertel, C4],
        [viertel, C4],
        [viertel, D4],
        [halbe, G3],
        [viertel, C4], # natura mirante
        [viertel, B3],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [halbe, E3],
        [viertel, E3], # tuum sanctum Genitorem
        [viertel, E3],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [viertel, E3],
        [viertel, D3],
        [viertel, E3],
        [viertel, F3],
        [halbe, E3],
        [viertel, C4], # Virgo prius ac posterius
        [viertel, B3],
        [viertel, A3],
        [viertel, G3],
        [viertel, A3],
        [viertel, G3],
        [viertel, E3],
        [viertel, F3],
        [halbe, G3],
        [viertel, A3], # Gabrielis ab ore
        [viertel, A3],
        [viertel, C4],
        [viertel, A3],
        [viertel, G3],
        [viertel, F3],
        [halbe, E3],
        [viertel, F3], # sumens ilud Ave
        [viertel, E3],
        [viertel, G3],
        [viertel, G3],
        [viertel, A3],
        [halbe, G3],
        [viertel, C4], # peccatorum miserere
        [viertel, B3],
        [viertel, C4],
        [achtel, A3],
        [viertel, G3],
        [viertel, A3],
        [viertel, F3],
        [viertel, E3],
        [viertel, D3],
        [ganze, C3]
    ]

def salve_regina(achtel = achtel()):
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe

    return [
        [viertel, C3], # Salve regina
        [viertel, E3],
        [viertel, G3],
        [viertel, A3],
        [halbe, G3],
        [viertel, A3], # mater misericordiae
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [viertel, G3],
        [viertel, A3],
        [viertel, G3],
        [halbe, G3],
        [viertel, C4], # Vita dulcedo
        [viertel, G3],
        [viertel, A3],
        [halbe, F3],
        [halbe, D3],
        [viertel, E3], # et spes nostra salve
        [viertel, F3],
        [viertel, G3],
        [viertel, E3],
        [achtel, E3],
        [achtel, D3],
        [halbe, C3],
        [viertel, G3], # Ad te clamamus
        [viertel, A3],
        [viertel, B3],
        [viertel, C4],
        [halbe, G3],
        [viertel, A3], # Exsules filii Evae
        [viertel, B3],
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [viertel, G3],
        [viertel, A3],
        [halbe, G3],
        [viertel, C4], # Ad te suspiramus
        [viertel, G3],
        [viertel, A3],
        [viertel, F3],
        [viertel, D3],
        [halbe, E3],
        [viertel, E3], # gementes et flentes
        [viertel, G3],
        [viertel, A3],
        [viertel, C4],
        [viertel, A3],
        [halbe, G3],
        [viertel, A3], # in hac lacrimarum valle
        [viertel, G3],
        [viertel, F3],
        [viertel, E3],
        [viertel, D3],
        [viertel, E3],
        [viertel, D3],
        [halbe, C3],
        [viertel, G3], # Eia ergo
        [viertel, A3],
        [viertel, B3],
        [halbe, C4],
        [viertel, G3], # advocata nostra
        [viertel, A3],
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [halbe, G3],
        [viertel, C4], # illos tuos misericordes oculos
        [viertel, G3],
        [viertel, A3],
        [viertel, F3],
        [viertel, D3],
        [viertel, E3],
        [viertel, F3],
        [viertel, G3],
        [viertel, F3],
        [viertel, A3],
        [viertel, G3],
        [halbe, G3],
        [viertel, F3], # ad nos converte
        [viertel, E3],
        [viertel, D3],
        [achtel, E3],
        [achtel, D3],
        [halbe, C3],
        [viertel, G3], # Et Jesum
        [achtel, A3],
        [achtel, B3],
        [halbe, C4],
        [viertel, B3], # benedictum fructum ventris tui
        [viertel, G3],
        [viertel, A3],
        [viertel, G3],
        [viertel, G3],
        [viertel, A3],
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [halbe, G3],
        [viertel + achtel, C3], # nobis
        [viertel + achtel, G3],
        [viertel, A3], # post hoc exsilium ostende
        [viertel, C4],
        [viertel, B3],
        [viertel, A3],
        [viertel, G3],
        [viertel, E3],
        [viertel, F3],
        [achtel, E3],
        [achtel, D3],
        [halbe, C3],
        [viertel, E3], # o clemens
        [achtel, F3],
        [achtel, G3],
        [halbe, E3],
        [halbe, C3],
        [viertel, G3], # o pia
        [achtel, A3],
        [achtel, B3],
        [achtel, C4],
        [achtel, B3],
        [achtel, A3],
        [achtel, G3],
        [halbe, G3],
        [halbe, C4], # o dulcis
        [achtel, G3],
        [achtel, A3],
        [viertel, F3],
        [viertel, D3],
        [achtel, E3],
        [achtel, F3],
        [halbe, G3],
        [viertel, C3], # virgo maria
        [viertel, F3],
        [viertel, E3],
        [achtel, D3],
        [achtel, C3],
        [ganze, C3]
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
