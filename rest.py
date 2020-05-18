import busio
import board
import adafruit_tpa2016

from flask import Flask

app = Flask(__name__)

i2c = busio.I2C(board.SCL, board.SDA)
tpa = adafruit_tpa2016.TPA2016(i2c)

@app.route('/state')
def get_state():
    return '{ state: %d }' % (0 if tpa.amplifier_shutdown else 1)

@app.route('/state/<int:state>')
def set_state(state):
    tpa.amplifier_shutdown = (state == 0)
    return get_state()
