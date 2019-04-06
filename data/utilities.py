from pyexcel_ods3 import get_data
import pandas as pd
import requests
import urllib.request
import json
import os

def importFromCSV():
    # Import the ODS file to a dict.
    data = get_data('yugioh_boosters.ods')

    # Create a new Dataframe and Array to store the card names in.
    output = pd.DataFrame(columns=['card'])
    card_names = []

    # Add each card name in each deck series to the array of card names.
    for series in data:
        print(series)
        cards = data[series]
        cards.pop(0)  # The first entry is always the header row, so we can ignore this.
        for card in cards:
            if len(card) > 0:
                name = card[2]  # The name of the card in this data set is in the 3rd column.
                card_names.append(name)

    output['card'] = card_names
    output.to_csv('cards_ods.csv', index=False)  # Output to a CSV.


def importFromAPI():
    # Get the data for all cards from the API.
    response = requests.get('https://db.ygoprodeck.com/api/v4/cardinfo.php')

    # Create a new Dataframe and Array to store the card names in.
    output = pd.DataFrame(columns=['card'])
    card_names = []

    if response.status_code == 200:
        j = json.loads(response.content.decode('utf-8'))

        # The way this API structures its data means we have access the 1st element which contains all the cards.
        for card in j[0]:
            name = card['name']  # Get the name from each card. It is a 'dict' object.
            print(name)
            card_names.append(name)

        output['card'] = card_names
        output.to_csv('cards_api.csv', index=False)  # Output to a CSV.
    else:
        return None

def downloadImagesFromAPI():
    directory = 'images'

    if not os.path.exists(directory):  # Create an image directory if one does not already exist.
        os.makedirs(directory)

    # Get the data for all cards from the API.
    response = requests.get('https://db.ygoprodeck.com/api/v4/cardinfo.php')

    if response.status_code == 200:
        j = json.loads(response.content.decode('utf-8'))
        count = 1

        # The way this API structures its data means we have access the 1st element which contains all the cards.
        for card in j[0]:
            imageUrl = card['image_url']
            downloadLocation = directory + '/' + card['id'] + '.jpg'
            try:
                urllib.request.urlretrieve(imageUrl, downloadLocation)
                print("Downloaded Image " + str(count))
                count += 1
            except:
                print("Error occurred when downloading image " + card['id'])
                count -= 1

        print("Downloaded " + str(count) + " images")
    else:
        print("Error occurred when accessing card list.")

if __name__ == '__main__':
    downloadImagesFromAPI()
