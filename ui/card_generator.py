import sys
import os
import math
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import title
import text
import card
import data.utilities as utils
import random


class CardGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.generateButton.clicked.connect(self.generateCard)

        self.filename = '../data/cards_api.csv'
        self.n, self.a = title.parseExistingTitles(self.filename)
        self.p = text.splitDescriptions(self.filename)

    def initUI(self):
        self.generateButton = QPushButton("Generate")
        self.imageLabel = QLabel()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.generateButton)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.imageLabel)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Yu-Gi-Oh Bot')
        self.show()

    def generateCard(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        image_path = 'testcard.png'

        cardtype = ['Monster', 'Ritual', 'Fusion', 'Spell', 'Trap', 'Synchro', 'Xyz']
        subtype = ['normal', 'effect', 'divine', 'gemini', 'spirit', 'toon', 'tuner', 'union']
        attribute = ['None', 'Dark', 'Divine', 'Earth', 'Fire', 'Light', 'Water', 'Wind', 'Spell', 'Trap']
        traptype = ['None', 'Equip', 'Continuous', 'Counter', 'Quick-Play', 'Field', 'Ritual']

        rarity = ['common', 'rare', 'ultra', 'secret']
        template = ['Normal', 'Effect', 'Ritual', 'Fusion', 'Synchro', 'DarkSynchro', 'Xyz', 'Unity', 'Link',
                    'Token', 'Spell', 'Trap', 'Skill']

        card_title = title.createNewTitle(self.n, self.a)
        card_effect = text.generateCardText(self.p)

        card_id = random.choice(utils.getCardIDs(self.filename))
        card_picture = os.path.abspath('../data/cropped/' + str(card_id) + ".jpg")
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

        # if type is 'Spell' or type is 'Trap':
        #     url = card.constructRequest(name=card_title, cardtype=type, trapmagictype=random.choice(traptype),
        #                                 rarity=random.choice(rarity), carddescription=card_text)
        # else:
        #     url = card.constructRequest(name=card_title, cardtype=type, subtype=random.choice(subtype),
        #                                 attribute=random.choice(attribute), level=str(random.randint(0, 12)),
        #                                 rarity=random.choice(rarity), carddescription=card_text)

        # print(url)
        # card.downloadImage(url, image_path)
        pixmap = QPixmap(image_path)
        self.imageLabel.setPixmap(pixmap)

        QApplication.restoreOverrideCursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CardGenerator()
    sys.exit(app.exec_())
