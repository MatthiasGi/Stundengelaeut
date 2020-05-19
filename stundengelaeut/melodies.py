"""Sammlung von Melodien im richtigen Format für die anderen Teile

Die verwendeten Melodien (im Einzelnen sind dies die marianischen Antiphonen)
werden hier im kompatiblen Format für schnelle Aufrufe vorgehalten.
"""

from stundengelaeut.notes import *

def _achtel():
    """
    Gibt die voreingestellte Dauer einer Achtelnote zurück. So ist eine
    persistente Änderung ausgeschlossen.

    Returns
    -------
    Standardwert für die Dauer einer Achtelnote.
    """
    return 0.25

def _note_values(achtel):
    """
    Generiert übrige Notenwerte aus der Dauer einer Achtelnote.

    Parameters
    ----------
    achtel : int
        Dauer einer Achtelnote

    Returns
    -------
    Drei Zahlen, in folgender Reihenfolge die Dauer einer ganzen, halben und
    viertel Note.
    """
    viertel = 2 * achtel
    halbe = 2 * viertel
    ganze = 2 * halbe
    return ganze, halbe, viertel


"""
Gibt die Melodie des „Macht hoch die Tür“ in einem carillon-freundlichen Format
zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Macht hoch die Tür, die Tor macht weit,
es komnmt der Herr der Herrlichkeit,
ein König aller Königreich,
ein Heiland aller Welt zugleich,
der Heil und Leben mit sich bringt,
derhalben jauchzt, mit Freuden singt.
Gelobet sei mein Gott,
mein Schöpfer reich an Rat.
"""
def macht_hoch_die_tuer(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

    return [
        [viertel, G3], # Macht hoch die Tür die Tor macht weit
        [halbe, A3SHARP],
        [viertel, G3SHARP],
        [halbe, G3],
        [viertel, F3],
        [viertel, D3SHARP],
        [viertel, F3],
        [viertel, G3],
        [halbe, F3],
        [viertel, A3SHARP], # es kommt der Herr der Herrlichkeit
        [halbe, G3SHARP],
        [viertel, G3SHARP],
        [halbe, G3],
        [viertel, G3],
        [viertel, F3],
        [viertel, D3SHARP],
        [viertel, F3],
        [halbe, D3SHARP],
        [viertel, G3], # ein König aller Königreich
        [halbe, F3],
        [viertel, F3],
        [viertel, G3],
        [viertel, A3],
        [viertel, A3SHARP],
        [viertel, A3SHARP],
        [viertel, C4],
        [viertel, A3],
        [halbe, A3SHARP],
        [viertel, F3], # ein Heiland aller Welt zugleich
        [halbe, G3],
        [viertel, F3],
        [viertel, G3],
        [viertel, A3],
        [viertel, A3SHARP],
        [viertel, A3SHARP],
        [viertel, C4],
        [viertel, A3],
        [halbe, A3SHARP],
        [viertel, A3SHARP], # der Heil und Leben mit sich bringt
        [halbe, C4],
        [viertel, A3SHARP],
        [halbe, C4],
        [viertel, A3SHARP],
        [viertel, C4],
        [viertel, A3SHARP],
        [viertel, G3SHARP],
        [halbe, G3],
        [viertel, A3SHARP], # derhalben jauchzt mit Freuden singt
        [halbe, C4],
        [viertel, A3SHARP],
        [halbe, C4],
        [viertel, A3SHARP],
        [viertel, C4],
        [viertel, A3SHARP],
        [viertel, G3SHARP],
        [halbe, G3],
        [viertel, A3SHARP], # gelobet sei mein Gott
        [halbe, D3SHARP],
        [viertel, D3SHARP],
        [halbe, G3SHARP],
        [viertel, G3],
        [2.5 * halbe, F3],
        [viertel, A3SHARP], # mein Schöpfer reich an Rat
        [halbe, G3SHARP],
        [viertel, G3],
        [viertel, F3],
        [viertel, D3SHARP],
        [viertel, F3],
        [2.5 * halbe, D3SHARP]
    ]

"""
Gibt die Melodie des Regina caeli in einem carillon-freundlichen Format zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Regina caeli, laetare, alleulia.
Quia quem meruisti portare, alleluia,
Ressurexit, sicut dixit, alleluia.
Ora pro nobis Deum, alleluia.
"""
def regina_caeli(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

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

"""
Gibt die Melodie des Ave Regina Caelorum in einem carillon-freundlichen Format
zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Ave Regina caelorum,
ave Domina Angelorum:
Salve radix, salve porta,
ex qua mundo lux est orta:
Gaude Virgo gloriosa,
super omnes speciosa:
Vale o valde decora,
et pro nobis Christum exora.
"""
def ave_regina_caelorum(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

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

"""
Gibt die Melodie des Alma Redemptoris Mater in einem carillon-freundlichen
Format zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Alma Redemptoris Mater,
quae pervia caeli
porta manes
et stella maris,
succurre cadenti,
surgere qui curat, populo:
tu quae genuisti,
natura mirante,
tuum sanctum Genitorem,
Virgo prius ac posterius,
Gabrielis ab ore
sumens illud Ave,
peccatorum miserere.
"""
def alma_redemptoris(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

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

"""
Gibt die Melodie des Salve Regina in einem carillon-freundlichen Format zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Salve, Regina,
mater misericordiae;
Vita, dulcedo et spes nostra, salve.
Ad te clamamus, exsules filii Evae.
Ad te suspiramus,
gementes et flentes in hac lacrimarum valle.
Eia ergo, Advocata nostra,
illos tuos misericordes oculos
ad nos converte.
Et Jesum, benedictum fructum ventris tui,
nobis post hoc exsilium ostende.
O clemens, o pia, o dulcis virgo Maria.
"""
def salve_regina(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

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

"""
Gibt die Melodie des Lourdes-Lieds in einem carillon-freundlichen Format zurück.

Parameters
----------
achtel : int (optional)
    Dauer einer Achtelnote

Returns
-------
Die Glocken verkünden mit fröhlichem Laut
Das Ave Maria so lieblich und laut.
Ave, Ave, Ave Maria,
Ave, Ave, Ave Maria.
"""
def lourdes_lied(achtel = _achtel()):
    ganze, halbe, viertel = _note_values(achtel)

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
