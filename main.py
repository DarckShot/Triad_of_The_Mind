# Файл, объеденяющий все окна

import sys

# Импорт модулей из библиотеки
import time

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QRadioButton

# Импорт классов из файлов всех окон
from Go_Study import Ui_Go_Study
from Main_Menu import Ui_Main_Menu
from Question_1 import Ui_Question_1
from Teory import Ui_Teory
from padavan_l1_1 import Ui_Padavan_l1_1
from padavan_l1_2 import Ui_Padavan_l1_2
from padavan_l1_3 import Ui_Padavan_l1_3
from Information_1Level import Ui_Information_1Level
from Level_Menu import Ui_Level_Menu

Level1 = 0

# Открытие Go_Study
app = QtWidgets.QApplication(sys.argv)

Go_Study_win = QtWidgets.QMainWindow()
ui = Ui_Go_Study()
ui.setupUi(Go_Study_win)
Go_Study_win.show()

'''Блок подключений интерфесов'''
global Main_Menu_win
Main_Menu_win = QtWidgets.QMainWindow()
ui1 = Ui_Main_Menu()
ui1.setupUi(Main_Menu_win)

global Form
Form = QtWidgets.QWidget()
ui2 = Ui_Teory()
ui2.setupUi(Form)

global Question_1
Question_1 = QtWidgets.QDialog()
ui3 = Ui_Question_1()
ui3.setupUi(Question_1)

global padavan_1_1
padavan_1_1 = QtWidgets.QMainWindow()
ui4 = Ui_Padavan_l1_1()
ui4.setupUi(padavan_1_1)

global padavan_1_2
padavan_1_2 = QtWidgets.QMainWindow()
ui5 = Ui_Padavan_l1_2()
ui5.setupUi(padavan_1_2)

global padavan_1_3
padavan_1_3 = QtWidgets.QMainWindow()
ui6 = Ui_Padavan_l1_3()
ui6.setupUi(padavan_1_3)

global Information_1Level_win
Information_1Level_win = QtWidgets.QMainWindow()
ui7 = Ui_Information_1Level()
ui7.setupUi(Information_1Level_win)

global Level_Menu_win
Level_Menu_win = QtWidgets.QMainWindow()
ui8 = Ui_Level_Menu()
ui8.setupUi(Level_Menu_win)
''''''

'''Logic'''


def proverka_L1():
    global Level1
    Level1 += 1
    print(Level1)
    return Level1


def proverka_L1_RUN(Level1):
    if Level1 >= 3:
        ui5.proverka.clicked.connect(lambda: show_Information_1Level())
        ui5.pushButton_2.clicked.connect(lambda: show_padavan_1_3())


# Функция запуска окна Main_Menu и закрытия Go_Study
def show_Main_Menu_Window():
    Go_Study_win.close()
    Main_Menu_win.show()


# Функция запуска окна Teory
def show_Teory_Window():
    Form.show()


# Функция запуска диалогового окна "Падаван"
def show_btn_1_question():
    Question_1.show()


# Функция запуска окна padavan_1_1 и закрытия Main_Menu
def show_padavan_1_1():
    Main_Menu_win.close()
    padavan_1_1.show()


# Функция запуска окна padavan_1_2 и закрытия Main_Menu
def show_padavan_1_2():
    padavan_1_1.close()
    padavan_1_2.show()


# Функция запуска окна padavan_1_3 и закрытия Main_Menu
def show_padavan_1_3():
    padavan_1_2.close()
    padavan_1_3.show()


# Функция перехода из уровня в Main_Menu
def show_Main_Menu_Window_сlose():
    padavan_1_1.close()
    padavan_1_2.close()
    padavan_1_3.close()
    Level_Menu_win.close()
    Main_Menu_win.show()


# Функция, показывающая результат проверки 1 левела
def show_Information_1Level():
    Information_1Level_win.show()


# Функция, показывающая результат проверки 1 левела
def show_Main_Menu__Level_Menu():
    Main_Menu_win.close()
    Level_Menu_win.show()


def show_Level_Menu__padavan1():
    Level_Menu_win.close()
    padavan_1_1.show()


''''''

'''Блок работы с кнопками'''

# При нажатии кнопки "Далее" в окне Go_Study использовать функцию show_Main_Menu_Window()
ui.go_studyButtob.clicked.connect(lambda: show_Main_Menu_Window())

# При нажатии кнопки "Книга знаний" использовать функцию show_Teory_Window()
ui1.pushButton.clicked.connect(lambda: show_Teory_Window())
# При нажатии кнопки "1 знак вопроса" использовать функцию show_btn_1_question()
ui1.c1_q_btn.clicked.connect(lambda: show_btn_1_question())
# При нажатии кнопки "Выбор уровня" использовать функцию show_Main_Menu__Level_Menu()
ui1.Go_btn.clicked.connect(lambda: show_Main_Menu__Level_Menu())
# При нажатии кнопки "Падаван" использовать функцию show_padavan_1_1()
ui1.complication1_btn.clicked.connect(lambda: show_padavan_1_1())

# При нажатии кнопки "стрелки вниз" закрыть окно
ui2.back_btn.clicked.connect(lambda: Form.close())

# При нажатии кнопки "OK" закрыть окно
ui3.OK_btn.clicked.connect(lambda: Question_1.close())

# При нажатии кнопки "Далее" использовать функцию show_padavan_1_2()
ui4.pushButton_2.clicked.connect(lambda: show_padavan_1_2())
# При нажатии кнопки "Домой" использовать функцию show_Main_Menu_Window_сlose()
ui4.pushButton_3.clicked.connect(lambda: show_Main_Menu_Window_сlose())
# При нажатии кнопки "Книга" использовать функцию show_Teory_Window()
ui4.pushButton.clicked.connect(lambda: show_Teory_Window())

# Проверка ответов при нажатии "Проверка"
ui5.q1_ask1.toggled.connect(lambda: proverka_L1())
ui5.q1_ask1.move(100, 100)
ui5.q2_ask4.toggled.connect(lambda: proverka_L1())
ui5.q2_ask4.move(100, 100)
ui5.q3_ask4.toggled.connect(lambda: proverka_L1())
ui5.q3_ask4.move(100, 100)
ui5.proverka.clicked.connect(lambda: proverka_L1_RUN(Level1))
# При нажатии кнопки "Домой" использовать функцию show_Main_Menu_Window_сlose()
ui5.pushButton_3.clicked.connect(lambda: show_Main_Menu_Window_сlose())
# При нажатии кнопки "Книга" использовать функцию show_Teory_Window()
ui5.pushButton.clicked.connect(lambda: show_Teory_Window())

# При нажатии кнопки "Домой" использовать функцию show_Main_Menu_Window_сlose()
ui6.pushButton_3.clicked.connect(lambda: show_Main_Menu_Window_сlose())
# При нажатии кнопки "Книга" использовать функцию show_Teory_Window()
ui6.pushButton.clicked.connect(lambda: show_Teory_Window())

# При нажатии кнопки "1" использовать функцию show_Level_Menu__padavan1()
ui8.pushButton_2.clicked.connect(lambda: show_Level_Menu__padavan1())
# При нажатии кнопки "Книга" использовать функцию show_Teory_Window()
ui8.pushButton.clicked.connect(lambda: show_Teory_Window())
# При нажатии кнопки "Домой" использовать функцию show_Main_Menu_Window_сlose()
ui8.pushButton_3.clicked.connect(lambda: show_Main_Menu_Window_сlose())
''''''

sys.exit(app.exec())
