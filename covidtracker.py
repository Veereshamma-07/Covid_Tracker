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

'''
Explain the purpose of the UiComponents method in the Window class.

Answer: The UiComponents method is responsible for setting up the graphical user interface (GUI) components of the application. It creates and configures a combo box for selecting countries, labels for displaying COVID-19 statistics, and connects the combo box to the get_cases method.
How does the combo box in this project dynamically load country names?

Answer: The country list contains names of countries. The UiComponents method iterates through the list, converts each country name to uppercase using i.upper(), and adds it to the combo box using self.combo_box.addItem(i).
Explain the purpose of the get_cases method.

Answer: The get_cases method is triggered when the user selects a country from the combo box. It retrieves COVID-19 statistics (total cases, recovered cases, and total deaths) for the selected country from the Worldometer website using web scraping with BeautifulSoup and updates the corresponding labels in the GUI.
What is the role of the requests library in this project?

Answer: The requests library is used to send HTTP requests to the Worldometer website and retrieve the HTML content of the page. This HTML content is then processed using BeautifulSoup to extract the relevant COVID-19 statistics.
How are the COVID-19 statistics displayed in the PyQt5 application?

Answer: The COVID-19 statistics (total cases, recovered cases, and total deaths) are displayed in the application's GUI using QLabel widgets. These labels are updated dynamically in the get_cases method based on the data fetched from the Worldometer website.
How could you enhance error handling in the get_cases method?

Answer: Error handling in the get_cases method could be improved by adding try-except blocks to capture and handle potential exceptions that may occur during the HTTP request or HTML parsing. This would make the application more robust and prevent crashes in case of network issues or changes in the website structure.
What are the potential challenges or limitations of using web scraping in this project?

Answer: Web scraping is subject to changes in the structure of the website, and if the Worldometer site undergoes modifications, the scraping logic may break. Additionally, web scraping may not be as reliable or efficient as using an official API, and it may raise ethical concerns if not done in accordance with the website's terms of use.

'''