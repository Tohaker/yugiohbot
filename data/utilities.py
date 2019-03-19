from pyexcel_ods3 import get_data
import pandas as pd

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
output.to_csv('cards.csv')  # Output to a CSV.
