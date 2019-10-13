import text
import title


def lambda_handler(event, context):
    source_file = 'cards_api.csv'

    nouns, adjectives = title.parseExistingTitles(source_file)
    card_title = title.createNewTitle(nouns, adjectives)

    phrases = text.splitDescriptions(source_file)
    card_text = text.generateCardText(phrases)

    return {'title': card_title, 'text': card_text}


if __name__ == '__main__':
    print(lambda_handler(1, 2))
