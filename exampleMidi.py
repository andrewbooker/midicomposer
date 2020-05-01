#!/usr/bin/env python

import os
import sys
def checkImport(lib):
    parentDir = os.path.dirname(os.getcwd())
    sys.path.append(parentDir)
    if not os.path.exists(os.path.join(parentDir, lib)):
        print("%s library not found." % lib)
        print("please clone github.com/andrewbooker/%s.git into %s" % (lib, parentDir))
        exit()

checkImport("mediautils")
from mediautils.midiFileWriter import MidiFileWriter

import random
topNotes = [59, 60, 62, 64, 66, 67, 69, 71, 72, 74]
bassNotes = [35, 36, 38, 40]

def anyIn(notes):
    return notes[random.randint(0, len(notes) - 1)]

m = MidiFileWriter("./test.mid")
m.setTempo(120)
sixteenths = 2

for n in range(24):
    rep = random.randint(2, 7)
    m.addNote("bass", anyIn(bassNotes), 99, rep * sixteenths) 
    for r in range(rep):
        m.addNote("top", anyIn(topNotes), 99, 1 * sixteenths)
    

del m
print("done")
