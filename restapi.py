"""
Einfaches Zweitskript, das nebenher einen REST-Server zum Einstellen von
Lautstärke u.Ä. betreibt.
"""

# Voraussetzungen:
# sudo pip3 install adafruit-blinka
# sudo pip3 install adafruit-extended-bus
# sudo pip3 install adafruit-circuitpython-tpa2016
# sudo pip3 install flask

from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_tpa2016
from flask import Flask, abort, jsonify

# TPA-Objekt erstellen
i2c = I2C(0)
tpa = adafruit_tpa2016.TPA2016(i2c)

# Voreinstellungen vornehmen
tpa.attack_time = 1
tpa.compression_ratio = tpa.COMPRESSION_4_1
tpa.hold_time = 0
tpa.noise_gate_enable = True
tpa.noise_gate_threshold = tpa.NOISE_GATE_4
tpa.release_time = 1

# REST-Server erstellen
app = Flask("Stundengeläut")

@app.route('/volume/')
def getVolume():
    if tpa.amplifier_shutdown: return dict(volume=0)
    return jsonify(dict(volume=tpa.fixed_gain))
    # TODO: Hier skalieren auf 0-100 nötig

@app.route('/volume/<int:volume>')
def setVolume(volume):
    if volume < 0 or volume > 100: abort(400)
    if volume == 0:
        tpa.amplifier_shutdown = True
    else:
        tpa.amplifier_shutdown = False
        tpa.fixed_gain = int((58 / 99 * (volume - 1)) - 28)
    return getVolume()

# REST-Server starten
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
