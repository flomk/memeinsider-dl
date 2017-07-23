from hashlib import md5
import json
from requests import get

urls = [
    'https://cdn.memeinsider.co/the-buzzfeed-effect.pdf',
    'https://cdn.memeinsider.co/flat-earth-theory.pdf',
    'https://cdn.memeinsider.co/the-internet-s-biggest-music-nerd.pdf',
    'https://cdn.memeinsider.co/facebook-an-untapped-market.pdf',
    'https://cdn.memeinsider.co/ken-bone-legend-interview-january.pdf',
    'https://cdn.memeinsider.co/shitposting-gone-too-far.pdf'
]

headers = {"Range": "bytes=0-10000"}
json_hashes = []
for url in urls:
    r = get(url, headers=headers).content
    md5_hash = md5(r).hexdigest()
    name = url.split('/')[-1]
    issue_hash = {
        name: md5_hash
    }
    json_hashes.append(issue_hash)
    # print(name + " has md5 of: " + md5_hash)
with open('data.txt', 'w') as outfile:  
    json.dump(json_hashes, outfile)
# print(json.dumps(json_hashes, indent=4))