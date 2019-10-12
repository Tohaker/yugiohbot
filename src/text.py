import pandas as pd
import nltk.data
import re
import random


def generateCardText(phrases):
    rand = random.sample(range(1, len(phrases)), random.randint(1, 5))
    text = []
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    prohibited = [',', ':', ';', '-']

    for selection in rand:
        p = phrases[selection]
        r = random.randint(0, len(p) - 1)

        sel = p[r]
        text.append(sel)  # Get a random phrase from the random text selection

    lastchar = text[-1][-1:]
    if lastchar in prohibited:
        lastletter = lastchar
        new_selection = ''

        while lastletter in prohibited:
            selection = phrases[random.randint(0, len(phrases))]
            new_r = random.randint(0, len(selection) - 1)
            new_selection = selection[new_r]
            lastletter = new_selection[-1:]  # Here we make sure the final phrase ends with a period

        text.append(new_selection)

    seperator = ' '
    result = seperator.join(text)
    sentences = tokenizer.tokenize(result)
    sentences = [sent.capitalize() for sent in sentences]  # Capitalize each sentence.
    result = seperator.join(sentences)

    return result


def splitDescriptions(file):
    existing_desc = pd.read_csv(file)['desc'].dropna().values.tolist()
    phrases = []
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    for desc in existing_desc:
        sentences = tokenizer.tokenize(desc)
        p = []
        for sentence in sentences:
            new_sentence = sentence.replace(',', ',,').replace(';', ';;').replace(':', '::').replace('- ', '-- ')
            p = re.split(', |; |: |- ', new_sentence)

        phrases.append(p)

    return phrases


if __name__ == '__main__':
    p = splitDescriptions('data/cards_api.csv')
    for i in range(5):
        print(generateCardText(p))
