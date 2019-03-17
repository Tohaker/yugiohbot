import pandas as pd
from textblob import TextBlob

# Read in the card names from a CSV file to a list.
existing_names = pd.read_csv('data/bewd.csv')['Card Name'].dropna().values.tolist()

nouns = []

# Read each card name into a TextBlob and extract the noun into a list.
for name in existing_names:
    blob = TextBlob(name)
    print(blob.tags)
    # nouns.append(blob.tags)

print(nouns)
