from adventsfest import AdventsFest
from adventszeit import Adventszeit
from fastenzeit import Fastenzeit
from heiligefamiliefest import HeiligeFamilieFest
from osterfest import OsterFest
from osterzeit import Osterzeit
from rang import Rang
from tagfest import TagFest
from taufedesherrnfest import TaufeDesHerrnFest
from weihnachtszeit import Weihnachtszeit

class FestManager:
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
