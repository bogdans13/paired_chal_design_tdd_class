from lib.music_history import MusicListeningHistory


'''
test if there is no input given at all
'''

def test_no_music_input_passed():
    no_music = MusicListeningHistory()
    assert no_music.musictracker == []


'''
test to see if we can add one song that was listened
'''

# def test_first_song_listened():
#     no_music = MusicListeningHistory()
#     no_music.addtotracker('Hit me baby one more time')
#     no_music = no_music.musictracker
# first_song.musictracker()
# assert musictracker == ['Hit me baby one more time']    



def test_first_song():
    first_song = MusicListeningHistory()
    first_song.addtotracker("single ladies")
    assert first_song.musictracker == ['single ladies']
    
'''
test to see behaviour of multiple songs are added at once
'''
def test_listened_to_many_songs():
    each_song = MusicListeningHistory()
    each_song.addtotracker('Hit me baby one more time')
    each_song.addtotracker('set fire to the rain')
    each_song.addtotracker('single ladies')
    assert each_song.musictracker == ['Hit me baby one more time', 'set fire to the rain', 'single ladies']
