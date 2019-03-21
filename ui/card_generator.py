import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QApplication
from PyQt5.QtCore import Qt
import title

class CardGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.generateButton.clicked.connect(self.generateTitle)

    def initUI(self):
        self.generateButton = QPushButton("Generate")
        self.titleLabel = QLabel()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.generateButton)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.titleLabel)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Yu-Gi-Oh Bot')
        self.show()

    def generateTitle(self):
        QApplication.setOverrideCursor(Qt.WaitCursor)

        n, a = title.parseExistingTitles('../data/cards.csv')
        t = title.createNewTitle(n, a)

        self.titleLabel.setText(t)

        QApplication.restoreOverrideCursor()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CardGenerator()
    sys.exit(app.exec_())
