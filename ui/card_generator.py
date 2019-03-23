import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import title
import card

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

        t = title.createNewTitle(self.n, self.a)
        url = card.constructRequest(name=t, cardtype='Monster', subtype='normal',
                           attribute='Light', level='1', rarity='Common')
        card.downloadImage(url, image_path)
        pixmap = QPixmap(image_path)
        self.imageLabel.setPixmap(pixmap)

        QApplication.restoreOverrideCursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CardGenerator()
    sys.exit(app.exec_())
