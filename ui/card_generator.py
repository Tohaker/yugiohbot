import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import title
import card
import random

class CardGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.generateButton.clicked.connect(self.generateCard)

        self.n, self.a = title.parseExistingTitles('../data/cards_api.csv')

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

        image_path = 'image.jpg'

        cardtype = ['Monster', 'Ritual', 'Fusion', 'Spell', 'Trap', 'Synchro', 'Xyz']
        subtype = ['normal', 'effect', 'divine', 'gemini', 'spirit', 'toon', 'tuner', 'union']
        attribute = ['Light', 'Dark', 'Fire', 'Water', 'Wind', 'Earth', 'Divine']
        traptype = ['None', 'Equip', 'Continuous', 'Counter', 'Quick-Play', 'Field', 'Ritual']
        rarity = ['Common', 'Rare', 'Super Rare', 'Ultra Rare', 'Secret Rare', 'Ultimate Rare']

        t = title.createNewTitle(self.n, self.a)
        print(t)

        type = random.choice(cardtype)
        if type is 'Spell' or type is 'Trap':
            url = card.constructRequest(name=t, cardtype=type, trapmagictype=random.choice(traptype),
                                        rarity=random.choice(rarity))
        else:
            url = card.constructRequest(name=t, cardtype=type, subtype=random.choice(subtype),
                    attribute=random.choice(attribute), level=str(random.randint(0, 12)), rarity=random.choice(rarity))

        print(url)
        card.downloadImage(url, image_path)
        pixmap = QPixmap(image_path)
        self.imageLabel.setPixmap(pixmap)

        QApplication.restoreOverrideCursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CardGenerator()
    sys.exit(app.exec_())
