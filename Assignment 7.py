song = {
    'title': 'The Ballroom Blitz',
    'artist': {
        'name': 'The Sweet',
        'members': ['Andy Scott', 'Steve Mann', 'Bruce Bisland', 'Paul Manzi', 'Lee Small']
    },
    'album': 'Desolation Boulevard',
    'genre': 'Glam Rock',
    'year': 1974,
    'track': 1,
    'discNumber': 1,
    'compilation': False,
    'fileInfo': {
        'duration': '4:07',
        'fileSize': '9.3 MB',
        'bitRate': '256 kbps',
        'sampleRate': '44.100 kHz',
        'channels': 'Stereo'
    },
    'copyright': '1988 Capitol Records, LLC'
}

for key in song:
    if isinstance(song[key], dict):
        value = song[key]
        print(key, ':')
        for key in value:
            print('  ', key, ':', value[key])
    else:
        print(key, ':', song[key])
