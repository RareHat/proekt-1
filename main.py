from PyQt5.QtWidgets import *

app = QApplication([])


window = QWidget()
window.resize(506,700)

quest_lbl = QLabel ("У якому році перший канал отримав золоту кнопку Youtube")
v_1995 = QRadioButton("1995")
v_2010 = QRadioButton("2010")
v_2015 = QRadioButton("2015")
v_2025 = QRadioButton("2025")
quest_lbl = QLabel ("У якому році перший канал отримав діамантову кнопку Youtube")
w_2005 = QRadioButton("2005")
w_2010 = QRadioButton("2010")
w_2015 = QRadioButton("2015")
w_2025 = QRadioButton("2025")


main_line = QVBoxLayout()
main_line.addWidget(quest_lbl)

def show_win():
    win_msg = QMessageBox()
    win_msg.setText("правильно!!")
    win_msg.exec()

v_1995.clicked.connect(show_win)


horizontal_linia = QHBoxLayout()
horizontal_linia.addWidget(v_1995)
horizontal_linia.addWidget(v_2010)
main_line.addLayout(horizontal_linia)


horizontal_linia2 = QHBoxLayout()
horizontal_linia2.addWidget(v_2025)
horizontal_linia2.addWidget(v_2015)
main_line.addLayout(horizontal_linia2)
window.setLayout(main_line)

horizontal_linia3 = QHBoxLayout()
horizontal_linia3.addWidget(v_1995)
horizontal_linia3.addWidget(v_2010)
main_line.addLayout(horizontal_linia3)
window.show()
app.exec()