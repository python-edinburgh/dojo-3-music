import glob
import random
import string
import sys

from pydub import AudioSegment
from pydub.effects import speedup
from pydub.playback import play

def generate_rand_string(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))

def get_songs():
    songs = glob.glob('*.mp3')
    return songs


def random_songs(number_of_songs):
    songs = get_songs()
    out = []
    for _ in range(number_of_songs):
        out.append(random.choice(songs))
    for i in out:
        print i
    return out


def random_segments(song):
    length = len(song)
    segment_length = (5 + (15 * random.random())) * 1000
    start_point = (length - segment_length - 10000) * random.random()

    segment = song[start_point:start_point + segment_length]
    return segment


def mix_songs(number_of_songs):
    song_names = random_songs(number_of_songs)
    songs = [AudioSegment.from_mp3(song_name) for song_name in song_names]
    segments = [random_segments(i) for i in songs]
    playlist = segments[0]

    playlist = speedup(playlist, playback_speed=1.5)

    for seg in segments:
        # WTF is going on here?
        playlist = playlist.append(seg, crossfade=1500)

    playlist.fade_out(1500).fade_in(1500)

    print len(playlist)
    playlist.export('mix_{}.mp3'.format(generate_rand_string()))
    play(playlist)

if __name__ == '__main__':
    mix_songs(int(sys.argv[1]))
