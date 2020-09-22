from datetime import date

class Fest:
    """
    Die abstrakte Klasse Fest liefert einen Rahmen für Informationen zu einem
    spezifischen Fest. Sie ist dabei so angelegt, dass die Grundinformationen
    durch Unterklassen, die sich an den eigentlichen Kirchenfesten orientieren,
    verbindlich abgefragt werden können.
    """

    def isDate(self, d):
        """
        Ermittelt, ob das Fest an einem bestimmten übergebenem Datum
        stattfindet. Diese Methode ist durch die Unterklasse entsprechend zu
        implementieren.

        Parameters
        ----------
        d : datetime.date
            Datum, für das überprüft werden soll, ob es sich um ein
            entsprechendes Fest handelt.

        Returns
        -------
        Hat einen Bool-Wert zurückzugeben, der für das genannte Datum bestimmt,
        ob ein Fest vorliegt.

        Raises
        ------
        NotImplementedError
            Da die Methode abstrakt ist, wirft sie diesen Fehler. Kindklassen
            haben die Implementierung vorzunehmen.
        """
        raise NotImplementedError

    def isToday(self):
        """
        Ermittelt, ob das Fest am heutigen Tage stattfindet. Shorthand, der in
        der abstrakten Oberklasse bereits implementiert ist.

        Returns
        -------
        Einen Bool-Wert, der angibt, ob das Fest heute stattfindet.
        """
        self.isDate(date.today())

    def rang(self):
        """
        Soll den Rang des durch die Instanz repräsentierten Festes zurückgeben.

        Returns
        -------
        Den Rang des repräsentierten Festes als stundengelaeut.fest.rang.Rang.

        Raises
        ------
        NotImplementedError
            Da die Methode abstrakt ist, wirft sie diesen Fehler. Kindklassen
            haben die Implementierung vorzunehmen.
        """
        raise NotImplementedError

    def name(self):
        """
        Soll den Namen des durch die Instanz repräsentierten Festes zurückgeben.

        Returns
        -------
        Name des repräsentierten Festes als einfacher String.

        Raises
        ------
        NotImplementedError
            Da die Methode abstrakt ist, wirft sie diesen Fehler. Kindklassen
            haben die Implementierung vorzunehmen.
        """
        raise NotImplementedError
