# Stundengelaeut
Einfaches Skript, das ein Stundengeläut per MIDI simuliert.

## Voraussetzungen
Um das Stundengeläut tatsächlich nutzen zu können, ist ein MIDI-Empfänger nötig.
Für ein rein virtuelles Carillon bieten sich dafür z.B. drei Komponenten an:

1. Grand Orgue (https://sourceforge.net/projects/ourorgan/)
2. Carillon (im Repository befindet sich eine modifizierte Version von
   http://duphly.free.fr/en/carillon.html, die um fehlende Halbtöne durch
   Verstimmen bestehender Glocken ergänzt werden)
3. Virtueller MIDI-Port (Mac:
  https://help.ableton.com/hc/de/articles/209774225-Verwendung-virtueller-MIDI-Busse,
  Windows: http://www.tobias-erichsen.de/software/loopmidi.html)

## Automatischer Start (Windows)
Sofern ein automatischer Start in Windows gewünscht ist, bietet sich an, eine Batch-Datei im Autostart-Ordner abzulegen (`%appdata%\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`). Annahme ist hier, dass das Skript auf D: liegt:
```bat
D:
cd D:\Skripte\Stundengelaeut
git pull
call conda activate py
python main.py
pause
```
