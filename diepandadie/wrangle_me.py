from lxml import etree
from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('mongodb://localhost:27017')
db = client.beatport

db.top100.drop()

root = etree.HTML(open('my_data/beatport100.html').read())
tree = etree.ElementTree(root)
for i in range(1, 101):
    item_path = '//ul[@class="bucket-items  ec-bucket"]/li[{}]'.format(i)
    rank = tree.xpath('{}//div[@class="buk-track-num"]'.format(item_path))[0].text
    title = tree.xpath('{}//span[@class="buk-track-primary-title"]'.format(item_path))[0].text
    mix = tree.xpath('{}//span[@class="buk-track-remixed"]'.format(item_path))[0].text
    artists = tree.xpath('{}//p[@class="buk-track-artists"]/a'.format(item_path))
    artists = [i.text for i in artists]
    remixers = tree.xpath('{}//p[@class="buk-track-remixers"]/a'.format(item_path))
    remixers = [i.text for i in remixers]
    label = tree.xpath('{}//p[@class="buk-track-labels"]/a'.format(item_path))[0].text
    genre = tree.xpath('{}//p[@class="buk-track-genre"]/a'.format(item_path))[0].text
    release_date = tree.xpath('{}//p[@class="buk-track-released"]'.format(item_path))[0].text

    print(rank, title, '\t', mix, '\t', artists, '\t', remixers, label, '\t', genre, '\t', release_date)

    json_insert = {
        'rank': rank,
        'title': title,
        'mix': mix,
        'artists': artists,
        'remixers': remixers,
        'label': label,
        'genre': genre,
        'release_date': release_date
    }

    db.top100.insert(json_insert)

