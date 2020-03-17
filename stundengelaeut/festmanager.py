from stundengelaeut.feste.adventsfest import AdventsFest
from stundengelaeut.feste.adventszeit import Adventszeit
from stundengelaeut.feste.fastenzeit import Fastenzeit
from stundengelaeut.feste.heiligefamiliefest import HeiligeFamilieFest
from stundengelaeut.feste.osterfest import OsterFest
from stundengelaeut.feste.osterzeit import Osterzeit
from stundengelaeut.feste.rang import Rang
from stundengelaeut.feste.tagfest import TagFest
from stundengelaeut.feste.taufedesherrnfest import TaufeDesHerrnFest
from stundengelaeut.feste.weihnachtszeit import Weihnachtszeit

from stundengelaeut.melodies import (alma_redemptoris, ave_regina_caelorum,
                                     regina_caeli, salve_regina)

from datetime import date

class FestManager:
    """
    Statische Klasse, die die Behandlung von Festen zusammenfasst. Hier sind
    alle berücksichtigten Feste registriert und hier wird auch entschieden,
    welche marianische Antiphon zu spielen ist.
    """

    """Sammlung aller registrierten Feste."""
    feste = [
        TagFest(12, 25, "Hochfest der Geburt des Herrn", Rang.HOCHFEST),
        HeiligeFamilieFest(0, "Fest der Heiligen Familie", Rang.FEST),
        TagFest(12, 26, "Stephanus", Rang.FEST),
        TagFest(12, 26, "2. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(12, 27, "3. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(12, 28, "Unschuldige Kinder", Rang.FEST),
        TagFest(12, 28, "4. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(12, 29, "5. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(12, 30, "6. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(12, 31, "7. Tag der Weihnachtsoktav", Rang.OKTAVTAG),
        TagFest(1, 1, "Hochfest der Gottesmutter Maria", Rang.HOCHFEST),
        TagFest(1, 6, "Erscheinung des Herrn", Rang.HOCHFEST),
        TaufeDesHerrnFest(0, "Taufe des Herrn", Rang.FEST),

        OsterFest(-46, "Aschermittwoch", Rang.SONDERTAG),
        OsterFest(-7, "Palmsonntag", Rang.SONDERTAG),
        OsterFest(-3, "Gründonnerstag", Rang.SONDERTAG),
        OsterFest(-2, "Karfreitag", Rang.SONDERTAG),
        OsterFest(-1, "Karsamstag", Rang.SONDERTAG),
        OsterFest(0, "Ostersonntag", Rang.HOCHFEST),
        OsterFest(1, "Ostermontag", Rang.HOCHFEST),
        OsterFest(2, "Montag der Osteroktav", Rang.HOCHFEST),
        OsterFest(3, "Dienstag der Osteroktav", Rang.HOCHFEST),
        OsterFest(4, "Mittwoch der Osteroktav", Rang.HOCHFEST),
        OsterFest(5, "Donnerstag der Osteroktav", Rang.HOCHFEST),
        OsterFest(6, "Freitag der Osteroktav", Rang.HOCHFEST),
        OsterFest(7, "Sonntag der Barmherzigkeit", Rang.HOCHFEST),
        OsterFest(39, "Christi Himmelfahrt", Rang.HOCHFEST),
        OsterFest(49, "Pfingsten", Rang.HOCHFEST),
        OsterFest(50, "Maria, Mutter der Kirche", Rang.GEBOTENER_GEDENKTAG),
        OsterFest(56, "Dreifaltigkeitssonntag", Rang.HOCHFEST),
        OsterFest(60, "Hochfest des Leibes und Blutes Christi", Rang.HOCHFEST),

        AdventsFest(-7, "Christkönigssonntag", Rang.HOCHFEST),

        TagFest(2, 2, "Darstellung des Herrn", Rang.FEST),
        TagFest(8, 6, "Verklärung des Herrn", Rang.FEST),
        TagFest(9, 14, "Kreuzerhöhung", Rang.FEST),
        TagFest(11, 1, "Allerheiligen", Rang.HOCHFEST),
        TagFest(11, 2, "Allerseelen", Rang.SONDERTAG),

        TagFest(1, 24, "Franz von Sales", Rang.GEBOTENER_GEDENKTAG),
        TagFest(1, 28, "Thomas von Aquin", Rang.GEBOTENER_GEDENKTAG),
        TagFest(1, 31, "Johannes Bosco", Rang.GEBOTENER_GEDENKTAG),
        TagFest(2, 3, "Blasius", Rang.NICHTGEBOTENER_GEDENKTAG),
        TagFest(2, 22, "Kathedra Petri", Rang.FEST),
        TagFest(2, 24, "Matthias", Rang.FEST),
        TagFest(3, 9, "Dominikus Savio", Rang.NICHTGEBOTENER_GEDENKTAG),
        TagFest(3, 19, "Josef", Rang.HOCHFEST),
        TagFest(3, 25, "Verkündigung des Herrn", Rang.HOCHFEST),
        TagFest(4, 29, "Katharina von Siena", Rang.FEST),
        TagFest(5, 1, "Josef der Arbeiter", Rang.NICHTGEBOTENER_GEDENKTAG),
        TagFest(6, 5, "Bonifatius", Rang.NICHTGEBOTENER_GEDENKTAG),
        TagFest(6, 24, "Geburt Johannes' des Täufers", Rang.HOCHFEST),
        TagFest(6, 29, "Petrus und Paulus", Rang.HOCHFEST),
        TagFest(7, 2, "Mariä Heimsuchung", Rang.FEST),
        TagFest(7, 11, "Benedikt von Nursia", Rang.FEST),
        TagFest(7, 22, "Maria Magdalena", Rang.FEST),
        TagFest(7, 31, "Ignatius von Loyola", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 14, "Maximilian Kolbe", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 15, "Mariä Aufnahme in den Himmel", Rang.HOCHFEST),
        TagFest(8, 16, "Altfrid", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 20, "Bernhard von Clairvaux", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 22, "Maria Königin", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 28, "Augustinus von Hippo", Rang.GEBOTENER_GEDENKTAG),
        TagFest(8, 29, "Enthauptung Johannes' des Täufers", Rang.GEBOTENER_GEDENKTAG),
        TagFest(9, 29, "Erzengel Michael, Gabriel und Rafael", Rang.FEST),
        TagFest(10, 4, "Franz von Assisi", Rang.GEBOTENER_GEDENKTAG),
        TagFest(10, 11, "Maria, Mutter vom guten Rat", Rang.HOCHFEST),
        TagFest(11, 7, "Engelbert", Rang.FEST),
        TagFest(11, 11, "Martin von Tours", Rang.GEBOTENER_GEDENKTAG),
        TagFest(11, 30, "Andreas", Rang.FEST),
        TagFest(12, 4, "Adolph Kolping", Rang.GEBOTENER_GEDENKTAG),
        TagFest(12, 6, "Nikolaus", Rang.NICHTGEBOTENER_GEDENKTAG),
        TagFest(12, 8, "Hochfest der ohne Erbsünde empfangenen Jungfrau und Gottesmutter Maria", Rang.HOCHFEST),
        TagFest(12, 13, "Luzia", Rang.NICHTGEBOTENER_GEDENKTAG)
    ]

    """Sammlung der geprägten Zeiten."""
    zeiten = [
        (Adventszeit(), alma_redemptoris()),
        (Weihnachtszeit(), alma_redemptoris()),
        (Fastenzeit(), ave_regina_caelorum()),
        (Osterzeit(), regina_caeli())
    ]

    @staticmethod
    def antiphon(d = None):
        """
        Ermittelt, welche Antiphon zum gegebenen Datum zu spielen ist.

        Parameters
        ----------
        date : datetime.date (optional)
            Datum, für das die marianische Antiphon erfragt werden soll. Ohne
            Angabe wird das heutige Datum verwendet.

        Returns
        -------
        Die heute zu spielende marianische Antiphon aus stundengelaeut.melodies.
        """
        if d == None: d = date.today()
        for zeit in FestManager.zeiten:
            if zeit[0].isDate(d): return zeit[1]
        return salve_regina()

    @staticmethod
    def fest(d = None):
        """
        Ermittelt, welches Fest zum gegebenen Datum begangen wird. Dabei wird
        die Rangfolge berücksichtigt. Bei gleichem Rang überwiegen erstgenannte
        Feste in der Liste „feste“ oben.

        Parameters
        ----------
        date : datetime.date (optional)
            Datum, für das die Abfrage des Festes erfolgen soll. Ohne Angabe
            wird das heutige Datum verwendet.

        Returns
        -------
        Das zum gegebenen Datum begangene Fest.
        """
        if d == None: d = date.today()
        fest = None
        for f in FestManager.feste:
            if not f.isDate(d): continue
            if fest == None: fest = f; continue
            if f.rang > fest.rang: fest = f
        return fest

    @staticmethod
    def hasFest(d = None):
        """
        Ermittelt, ob zum gegebenen Datum ein Fest begangen wird. Effizienter,
        als zu überprüfen, ob die Methode „fest(date)“ etwas zurückgibt, da hier
        beim ersten Fund abgebrochen wird und keine Abwägung der Rangfolge
        erfolgt.

        Parameters
        ----------
        date : datetime.date (optional)
            Datum, für das die Abfrage eines Festes erfolgen soll. Ohne Angabe
            wird das heutige Datum verwendet.

        Returns
        -------
        Ob am gegebenem Datum ein Fest begangen wird.
        """
        if d == None: d = date.today()
        for f in FestManager.feste:
            if f.isDate(d): return True
        return False

    @staticmethod
    def zeit(d = None):
        """
        Ermittelt, welche geprägte Zeit am gegebenen Datum begangen wird.

        Parameters
        ----------
        date : datetime.date (optional)
            Datum, für das die Abfrage der geprägten Zeit erfolgen soll. Ohne
            Angabe wird das heutige Datum verwendet.

        Returns
        -------
        Die am gegebenem Datum begangene geprägte Zeit (oder None, falls keine
        begangen wird).
        """
        if d == None: d = date.today()
        for z in FestManager.zeiten:
            if z.isDate(d): return z

    @staticmethod
    def hasZeit(d = None):
        """
        Ermittelt, ob am gegebenem Datum eine geprägte Zeit begangen wird.

        Parameters
        ----------
        date : datetime.date (optional)
            Datum, für das die Abfrage einer geprägten Zeit erfolgen soll. Ohne
            Angabe wird das heutige Datum verwendet.

        Returns
        -------
        Ob eine geprägte Zeit zum gegebenem Datum begangen wird.
        """
        return FestManager.zeit(d) != None
