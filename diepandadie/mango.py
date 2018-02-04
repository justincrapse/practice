from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.iceice

results = db.blue.find({})
search_strings = []
for doc in results:
    title = doc['title']
    mix = doc['mix']
    mix = mix if mix != 'Original Mix' else ''
    artist = ' '.join(doc['artists'])
    track = 'track:"{} {}'.format(title, mix).strip() + '"'
    search_str = '{} {}'.format(track, artist)
    search_strings.append(search_str)

print(search_strings[0])

# connect to spotify, search for a track and get results


"""
SPOTIFY CLEANSING:
words to ignore:
Extended
& and 'and'
Original Mix
"""