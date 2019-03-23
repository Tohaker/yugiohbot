# We can generate a card image using the following API:
# https://www.yugiohcardmaker.net/ycmaker/createcard.php?name=&cardtype=Monster&subtype=normal&attribute=Light&level=1
# &rarity=Common&picture=&circulation=&set1=&set2=&type=&carddescription=&atk=&def=&creator=&year=2019&serial=

import requests
import shutil

def constructRequest(**kwargs):
    base_url = "https://www.yugiohcardmaker.net/ycmaker/createcard.php?"
    url_args = ['name', 'cardtype', 'subtype', 'attribute', 'level', 'rarity', 'picture', 'circulation', 'set1', 'set2',
                'type', 'carddescription', 'atk', 'def', 'creator', 'year', 'serial']
    url_dict = {}

    for arg in url_args:
        index = url_args.index(arg)
        kw = kwargs.get(arg) if kwargs.get(arg) is not None else ""  # Check if the Key Word argument has been supplied.
        url_dict[arg] = kw  # Build up a dictionary of all the arguments.

        # The last parameter doesn't need an '&'
        if index < len(url_args) - 1:
            base_url += arg + '=' + kw + '&'
        else:
            base_url += arg + '=' + kw

    return base_url

def downloadImage(url, path):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

if __name__ == '__main__':
    url = constructRequest(name='hello', cardtype='Monster', subtype='normal',
                           attribute='Light', level='1', rarity='Common')
    downloadImage(url, 'image.jpg')
