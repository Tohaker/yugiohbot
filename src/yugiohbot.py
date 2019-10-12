from src import title, text
from build.src import card
import src.data.utilities as utils
import random
import os
import boto3

s3 = boto3.client('s3')
filename = 'data/cards_api.csv'

def uploadToS3(file):
    success = s3.upload_file(file, 'yu-gi-oh-images', 'generated/' + file)
    print('Upload to S3: ' + str(success))


def downloadImageFromS3(file):
    success = s3.download_file('yu-gi-oh-images', 'cropped/' + file, file)
    print("Download " + file + "from S3: " + str(success))


def setup(filename):
    n, a = title.parseExistingTitles(filename)
    p = text.splitDescriptions(filename)
    return n, a, p


def main(n, a, p, image_path):

    cardtype = ['Monster', 'Ritual', 'Fusion', 'Spell', 'Trap', 'Synchro', 'Xyz']
    subtype = ['normal', 'effect', 'divine', 'gemini', 'spirit', 'toon', 'tuner', 'union']
    attribute = ['None', 'Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind', 'Spell', 'Trap']
    traptype = ['None', 'Equip', 'Continuous', 'Counter', 'Quick-Play', 'Field', 'Ritual']

    rarity = ['common', 'rare', 'ultra', 'secret']
    template = ['Normal', 'Effect', 'Ritual', 'Fusion', 'Synchro', 'DarkSynchro', 'Xyz', 'Unity', 'Link',
                'Token', 'Spell', 'Trap', 'Skill']

    card_title = title.createNewTitle(n, a)
    card_effect = text.generateCardText(p)

    card_id = random.choice(utils.getCardIDs(filename))

    card_image_path = str(card_id) + ".jpg"
    print(card_image_path)
    downloadImageFromS3(card_image_path)
    card_picture = os.path.abspath(card_image_path)

    card_rarity = random.choice(rarity)
    card_template = random.choice(template)
    card_attribute = random.choice(attribute)
    card_type = random.choice(cardtype)

    attack = int(round(random.randint(0, 7000), -2))
    defense = int(round(random.randint(0, 7000), -2))
    card_serial = random.randint(0, 9999999999)

    print(card_title)
    print(card_effect)
    print(card_picture)

    card.fillInNeoCardMaker(name=card_title, rarity=card_rarity, template=card_template, attribute=card_attribute,
                            level=str(random.randint(0, 12)), picture=card_picture, type=card_type,
                            effect=card_effect,
                            atk=str(attack), defense=str(defense), creator='YuGiOh-Bot', year='2019',
                            serial=str(card_serial), filename=image_path)

    os.remove(card_image_path)

if __name__ == '__main__':
    n, a, p = setup(filename)
    for i in range(10):
        image = 'results/' + str(i) + '.jpg'
        main(n, a, p, image)