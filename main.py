from PyQt5.QtWidgets import *
import requests
import webbrowser
# Create app and set name
app = QApplication([])
# Create elements and set them into the variables
window = QWidget()
window.setWindowTitle("EasyWeather")
window.setGeometry(60, 60, 600, 400)
layout = QVBoxLayout()
button = QPushButton("Show weather report")
button1 = QPushButton("Save weather report to a file")
textbox = QLineEdit()
textbox.setPlaceholderText("Place")
label = QLabel("EasyWeather")
label.setStyleSheet("font-size: 40px;")
# label.setAlignment(Qt.AlignCenter) not working
layout.addWidget(label)
layout.addWidget(textbox)
layout.addWidget(button)
layout.addWidget(button1)

# Execute search fn if button clicked
def search():
    alert = QMessageBox()
    if textbox.text() == "":
        alert.setText("Error: You didn't provide location.")
        alert.exec_()
        return
    r = requests.get(url="https://MaTYAPI.matymt.repl.co/weather/" + textbox.text())
    # TODO: API not working!
    data = r.json()
    status = data["success"]
    if status == False:
        alert.setText("Error: Location not found.")
        alert.exec_()
        return
    result = data["result"]
    contents = result[0]
    location = contents["location"]
    current = contents["current"]
    temperature = current["temperature"]
    skytext = current["skytext"]
    city = location["name"]
    winddisplay = current["winddisplay"]
    feelslike = current["feelslike"]

    alert.setText("Current weather for " + city + ":\n\n" + skytext + "\nTemperature: " + temperature + "°C\nFeels like: " + feelslike + "°C\nWind: " + winddisplay)
    alert.exec_()
button.clicked.connect(search)

def save_to_a_file():
    alert = QMessageBox()
    if textbox.text() == "":
        alert.setText("Error: You didn't provide location.")
        alert.exec_()
        return
    r = requests.get(url="https://MaTYAPI.matymt.repl.co/weather/" + textbox.text())
    data = r.json()
    status = data["success"]
    if status == False:
        alert.setText("Error: Location not found.")
        alert.exec_()
        return
    result = data["result"]
    contents = result[0]
    location = contents["location"]
    current = contents["current"]
    temperature = current["temperature"]
    skytext = current["skytext"]
    city = location["name"]
    winddisplay = current["winddisplay"]
    feelslike = current["feelslike"]

    dialog = QFileDialog()
    dir = dialog.getExistingDirectory(window, 'Select a directory')
    file = open(dir + "/weather for " + city + ".txt", "a")
    file.write("Weather for " + city + ":\n\n" + skytext + "\nTemperature: " + temperature + "°C\nFeels like: " + feelslike + "°C\nWind: " + winddisplay)
    alert.setText("Report saved to " + dir + "/weather for " + city + ".txt")
    alert.exec_()
    webbrowser.open(dir + "/weather for " + city + ".txt")

button1.clicked.connect(save_to_a_file)

window.setLayout(layout)
window.show()
app.exec_()
