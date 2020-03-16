from datetime import date
from datetime import timedelta
from stundengelaeut.feast import Feast

class Date:

    lastupdate = date.today() + timedelta(days = -1)

    antiphon = None

    celebration = False

    @staticmethod
    def check():
        today = date.today()
        if Date.lastupdate >= today: return
        Date.lastupdate = today

        antiphon = melodies.salve_regina()
        celebration = (today.isoweekday() == 7)

        # Weihnachtsfestkreis
        christmas = date(today.year, 12, 25)
        advent = christmas + timedelta(days = -christmas.isoweekday() - 7*3)
