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

nextT = 0
nextB = 0
def anyIn(notes):
    #return notes[random.randint(0, len(notes) - 1)]
    global nextB
    global nextT
    if notes == bassNotes:
        nextB += 1
        if nextB == len(notes):
            nextB = 0
        return notes[nextB]

    if notes == topNotes:
        nextT += 1
        if nextT == len(notes):
            nextT = 0
        return notes[nextT]

m = MidiFileWriter("./test.mid")
intervalLength = 1000 # if tempo, =16ths otherwise =milliseconds

tempo = 57
ppqn = 60000/tempo

m.setTempo(tempo, ppqn)

for n in range(24):
    rep = 4#random.randint(3, 7)
    m.addNote("bass", anyIn(bassNotes), 99, rep * intervalLength) 
    for r in range(rep):
        m.addNote("top", anyIn(topNotes), 99, 1 * intervalLength)
    

del m
print("done")
