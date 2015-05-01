import random
from noise import pnoise1
from pysynth_e import *

base = random.randint(0, 255)

bands = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
sharps = ['{}#'.format(b) for b in bands]
notes = zip(bands, sharps)
note_range = len(bands)
bpm = random.randint(120,220)

def wave():
    return  [int(pnoise1((i/100.0) * base, 4) * 100) for i in range(0, 128)]

def convert_wave(wave):
    return [bands[(point % note_range)] for point in wave]


def generate_abc():
    notes = convert_wave(wave())
    length = random.randint(2, 4)
    return tuple([(note, length) for note in notes])


song = generate_abc()
make_wav(song, fn='test{}.wav'.format(base), bpm=bpm)

