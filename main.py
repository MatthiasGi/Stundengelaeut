from datetime import datetime
from datetime import time as dtime
import time

from lib import (Carillon, Striker, StrikeObserver, Today)


class MelodyPlayer(StrikeObserver):

    def __init__(self, carillon):
        self.carillon = carillon

    def pre_strike(self, striker: Striker, time: datetime) -> bool:
        if time.hour == 8 and time.minute == 0:
            self.active = True

        elif time.hour == 21 and time.minute == 30:
            name = Today.antiphon().replace(' ', '_')
            striker.strike(notify=False, complete=True)
            self.carillon.play(f'songs/{name}.mid')
            striker.active = False
            return False

        return True

    def post_strike(self, striker: Striker, time: datetime) -> None:
        if time.hour == 12 and time.minute == 00:
            self.carillon.play('songs/Lourdes_Lied.mid')


carillon = Carillon()
striker = Striker(carillon)
Today.infuse(striker)
player = MelodyPlayer(carillon)
striker.attach_observer(player)

tnow = datetime.now().time()
if tnow < dtime(7, 55) or tnow > dtime(21, 25):
    striker.active = False

while True:
    time.sleep(0.1)
