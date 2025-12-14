import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from io import BytesIO

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 200, 100, 100)
        self.get_weather_button = QPushButton("Get Photo", self)
        self.description_label = QLabel(self)
        self.title_label = QLabel("Pls MAXIMISE this Window\nIf you dont see the full image,\nRESTORE the window and MAXIMISE it again", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Astronomy Pictures")

        vbox = QVBoxLayout()

        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.title_label)

        self.setLayout(vbox)


        self.description_label.setAlignment(Qt.AlignCenter)
        self.title_label.setAlignment(Qt.AlignCenter)


        self.get_weather_button.setObjectName("get_weather_button")
        self.description_label.setObjectName("description_label")
        self.title_label.setObjectName("title_label")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Calibri;
            }
            QPushButton#get_weather_button{
                font-size: 30px;
                font-weight: bold;
                border: 2px solid;
                background-color: hsl(0, 100%, 64%);
                border-radius: 10px;
            }
            QPushButton#get_weather_button:hover{
                background-color: hsl(0, 100%, 84%);
                border-radius: 10px;      
            }
            QLabel#title_label{
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        
        api_key = "ZzNVFa2eAsdZY26UGWVEKrxbmjiOjMXdKSSJbiHF"
        url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count=1"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            image = data[0]["url"]
            title = data[0]["title"]
            response2 = requests.get(image)
            image_data = BytesIO(response2.content)
            self.display_weather(image_data)
            self.display_title(title)



        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal Server Error:\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error ocurred:\n{http_error} ")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe requests timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many Redirects:\nCheck the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_title(self, data):
        self.title_label.clear()
        self.title_label.setText(data)

        
    def display_error(self, message):
        self.title_label.setText(message)

    def display_weather(self, data):
        pixmap = QPixmap()
        pixmap.loadFromData(data.read())

        self.description_label.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())