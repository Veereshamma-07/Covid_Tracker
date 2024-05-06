#importing libraries
from PyQt5.QtWidgets import*
from PyQt5 import QtCore,QtGui
from  PyQt5.QtGui import*
from PyQt5.QtCore import*
from bs4 import BeautifulSoup as BS
import requests
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Covid tracker")

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        # calling method
        self.UiComponents()

        # Showing all the widgets
        self.show()

    # methods for widgets
    def UiComponents(self):

        # countries list/ user can add other countries as well
        self.country = ["India", "US", "Spain", "China", "Russia", "Pakistan", "Nepal", "Italy", "UK", "Brazil"]

        # creating a combo box widget
        self.combo_box = QComboBox(self)

        # setting geometry to combo box
        self.combo_box.setGeometry(100, 50, 200, 40)

        # setting font
        self.combo_box.setFont(QFont('Times', 10))

        # adding items to combo box
        for i in self.country:
            i = i.upper()
            self.combo_box.addItem(i)

        # adding action to the combo box
        self.combo_box.activated.connect(self.get_cases)

        # Creating label to show the total cases
        self.label_total = QLabel("Total Cases", self)
        self.label_total.setAlignment(Qt.AlignCenter)
        self.label_total.setGeometry(100, 120, 200, 40)
        self.label_total.setStyleSheet("border: 2px solid black;")

        # Creating label to show the recovered cases
        self.label_reco = QLabel("Recovered Cases", self)
        self.label_reco.setAlignment(Qt.AlignCenter)
        self.label_reco.setGeometry(100, 180, 200, 40)
        self.label_reco.setStyleSheet("border: 2px solid black;")

        # Creating label to show the death cases
        self.label_death = QLabel("Total Deaths", self)
        self.label_death.setAlignment(Qt.AlignCenter)
        self.label_death.setGeometry(100, 240, 200, 40)
        self.label_death.setStyleSheet("border: 2px solid black;")

    def get_cases(self):
        # getting country name
        index = self.combo_box.currentIndex()
        country_name = self.country[index].lower()

        # creating url using country name
        url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

        # getting the request from url
        data = requests.get(url)

        # converting the text
        soup = BS(data.text, "html.parser")

        # finding meta info for cases
        cases = soup.find_all("div", class_="maincounter-number")

        # getting total cases number
        total = cases[0].span.text

        # getting recovered cases number
        recovered = cases[2].span.text

        # getting death cases number
        deaths = cases[1].span.text

        # showing data through labels
        self.label_total.setText("Total Cases: " + total)
        self.label_reco.setText("Recovered Cases: " + recovered)
        self.label_death.setText("Total Deaths: " + deaths)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

