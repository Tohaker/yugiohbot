import pandas as pd
from textblob import TextBlob
import random


def parseExistingTitles(file):

    # Read in the card names from a CSV file to a list, ignoring empty rows within the 'Card Name' column.
    existing_names = pd.read_csv(file)['card'].dropna().values.tolist()

    nouns = []
    adjectives = []

    # Read each card name into a TextBlob and extract the noun into a list.
    for name in existing_names:
        blob = TextBlob(name)
        # print(blob.tags)

        for word, pos in blob.tags:
            if pos == 'NNP':
                nouns.append(word)  # Only add words which are Proper Nouns to the list.
            elif pos == 'JJ':
                adjectives.append(word)  # Only add words which are Adjectives to the list.

    nouns = dedup(nouns)
    adjectives = dedup(adjectives)

    return nouns, adjectives


# Removes duplicates from a list while still preserving the order.
def dedup(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def createNewTitle(nouns, adjectives):
    nouns_adjectives_dict = {'nouns': nouns, 'adjectives': adjectives}

    no_sections = random.randint(1, 2)  # Select how many sections the title will have. Min 1, Max 2.
    title_section = []

    for i in range(no_sections):
        no_components = random.randint(1, 2)  # Select how many components each section will have. Min 1, Max 2.
        component = []

        j = 0
        while j < no_components:
            if len(component) < 1:
                random_pos = random.choice(list(nouns_adjectives_dict.keys()))  # Choose either a noun or an adjective
                random_word = random.choice(nouns_adjectives_dict[random_pos])  # Select a random value from the POS
                component.append(random_word)

                if random_pos is 'adjectives' and no_components < 2:
                    no_components += 1  # An adjective can't be the only word, so we add an extra one if one is chosen.
            else:
                component.append(random.choice(nouns))  # Get a new random noun

            j += 1

        title_section.append(component)

    return title_section


if __name__ == '__main__':
    n, a = parseExistingTitles('data/cards_api.csv')

    print(n)
    print(a)
    print(createNewTitle(n, a))
