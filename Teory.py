# Меню с теорией 1 части и кнопкой "Назад"

# Импорт модулей из библиотеки
from PyQt6 import QtCore, QtGui, QtWidgets

# Импорт файла ресурсов resource_rc
import resource_rc


class Ui_Teory(object):
    def __init__(self):
        self.horizontalLayout_4 = None
        self.line = None
        self.code_3 = None
        self.horizontalLayout_2 = None
        self.frame_3 = None
        self.text_3 = None
        self.label = None
        self.horizontalLayout = None
        self.frame_2 = None
        self.text_2 = None
        self.code_1 = None
        self.text_1 = None
        self.Title2 = None
        self.Title1 = None
        self.verticalLayout_4 = None
        self.scrollAreaWidgetContents = None
        self.scrollArea = None
        self.verticalLayout_3 = None
        self.frame = None
        self.verticalLayout_2 = None
        self.Main_Title = None
        self.horizontalLayout_3 = None
        self.verticalLayout = None
        self.back_btn = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 720)
        Form.setMinimumSize(QtCore.QSize(640, 720))
        Form.setMaximumSize(QtCore.QSize(640, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurce/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Main_Title = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.Main_Title.setFont(font)
        self.Main_Title.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "color: rgb(85,116,226);\n"
                                      "font-weight: bold;")
        self.Main_Title.setObjectName("Main_Title")
        self.horizontalLayout_3.addWidget(self.Main_Title)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setMaximumSize(QtCore.QSize(640, 720))
        self.frame.setStyleSheet("\n"
                                 "/* VERTICAL SCROLLBAR */\n"
                                 " QScrollBar:vertical {\n"
                                 "    border: none;\n"
                                 "    background:rgb(255, 255, 255);\n"
                                 "    width: 14px;\n"
                                 "    margin: 15px 0 15px 0;\n"
                                 "    border-radius: 0px;\n"
                                 " }\n"
                                 "\n"
                                 "/*  HANDLE BAR VERTICAL */\n"
                                 "QScrollBar::handle:vertical {    \n"
                                 "    background-color:rgb(85,116,226);\n"
                                 "    min-height: 30px;\n"
                                 "    border-radius: 7px;\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:hover{    \n"
                                 "    background-color:rgb(85,116,226);\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:pressed {    \n"
                                 "    background-color:rgb(85,116,226);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN TOP - SCROLLBAR */\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "    height: 15px;\n"
                                 "    border-top-left-radius: 7px;\n"
                                 "    border-top-right-radius: 7px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:hover {    \n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:pressed {    \n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN BOTTOM - SCROLLBAR */\n"
                                 "QScrollBar::add-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "    height: 15px;\n"
                                 "    border-bottom-left-radius: 7px;\n"
                                 "    border-bottom-right-radius: 7px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:hover {    \n"
                                 "    background-color:rgb(255, 255, 255);\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:pressed {    \n"
                                 "    background-color:rgb(85,116,226);\n"
                                 "}\n"
                                 "\n"
                                 "/* RESET ARROW */\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(640, 720))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 613, 1800))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 1800))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(-1, 15, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Title1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Title1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.Title1.setFont(font)
        self.Title1.setStyleSheet("font-weight: bold;")
        self.Title1.setObjectName("Title1")
        self.verticalLayout_4.addWidget(self.Title1)
        self.Title2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Title2.setMinimumSize(QtCore.QSize(0, 120))
        self.Title2.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Title2.setFont(font)
        self.Title2.setStyleSheet("font-weight: bold;")
        self.Title2.setObjectName("Title2")
        self.verticalLayout_4.addWidget(self.Title2)
        self.text_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text_1.setMinimumSize(QtCore.QSize(0, 180))
        self.text_1.setMaximumSize(QtCore.QSize(16777215, 180))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.text_1.setFont(font)
        self.text_1.setMouseTracking(True)
        self.text_1.setIndent(-1)
        self.text_1.setObjectName("text_1")
        self.verticalLayout_4.addWidget(self.text_1)
        self.code_1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.code_1.setMinimumSize(QtCore.QSize(0, 60))
        self.code_1.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.code_1.setFont(font)
        self.code_1.setStyleSheet("border-radius: 20px;\n"
                                  "background-color: rgb(71,91,142);\n"
                                  "color: rgb(255, 255, 255);")
        self.code_1.setObjectName("code_1")
        self.verticalLayout_4.addWidget(self.code_1)
        self.text_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text_2.setMinimumSize(QtCore.QSize(0, 400))
        self.text_2.setMaximumSize(QtCore.QSize(16777215, 380))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.text_2.setFont(font)
        self.text_2.setObjectName("text_2")
        self.verticalLayout_4.addWidget(self.text_2)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 170))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frame_2.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(71,91,142);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(170, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.text_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.text_3.setMinimumSize(QtCore.QSize(0, 220))
        self.text_3.setMaximumSize(QtCore.QSize(16777215, 220))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.text_3.setFont(font)
        self.text_3.setLineWidth(1)
        self.text_3.setObjectName("text_3")
        self.verticalLayout_4.addWidget(self.text_3)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setStyleSheet("border-radius: 20px;\n"
                                   "background-color: rgb(71,91,142);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(80, 20, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.code_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.code_3.setFont(font)
        self.code_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "")
        self.code_3.setObjectName("code_3")
        self.horizontalLayout_2.addWidget(self.code_3)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.back_btn = QtWidgets.QPushButton(Form)
        self.back_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.back_btn.setStyleSheet("image: url(:/recurce/btn_Down.png);\n"
                                    "border: none;")
        self.back_btn.setText("")
        self.back_btn.setObjectName("back_btn")
        self.horizontalLayout_4.addWidget(self.back_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Teory"))
        self.Main_Title.setText(_translate("Form", "<html><head/><body><p align=\"center\">Теория</p></body></html>"))
        self.scrollArea.setWhatsThis(_translate("Form",
                                                "<html><head/><body><p>При выводе переменной, </p><p>в консоль "
                                                "выведется ее значение, </p><p>любого типа данных (логический, "
                                                "</p><p>строковый, целочисленный и т.п.), </p><p>например: "
                                                "</p></body></html>"))
        self.Title1.setText(_translate("Form", "<html><head/><body><p>Книга с теорией</p></body></html>"))
        self.Title2.setText(_translate("Form",
                                       "<html><head/><body><p>Вывод. Стандартные типы данных</p><p>действия с "
                                       "ними</p></body></html>"))
        self.text_1.setText(_translate("Form",
                                       "<html><head/><body><p align=\"justify\">Для осуществления вывода "
                                       "информации</p><p align=\"justify\">в консоль в Python используется "
                                       "такая</p><p align=\"justify\">команда, как:</p></body></html>"))
        self.code_1.setText(_translate("Form", "<html><head/><body><p align=\"center\">print()</p></body></html>"))
        self.text_2.setText(_translate("Form",
                                       "<html><head/><body><p align=\"justify\">Рассмотрим несколько способов "
                                       "ввода</p><p align=\"justify\">для разных типов данных.</p><p "
                                       "align=\"justify\">Для начала, рассмотрим классический</p><p "
                                       "align=\"justify\">вывод предложения “Hello World!”,"
                                       "</p><p align=\"justify\">чтобы вывести в консоль строку</p><p "
                                       "align=\"justify\">необходимо записать строку в \'\'.</p><p "
                                       "align=\"justify\">Приведем пример программы,"
                                       "</p><p align=\"justify\">выводящей в консоль “Hello World!”:</p><p "
                                       "align=\"justify\"><br/></p></body></html>"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"justify\">print(“Hello world!“) <br/># В консоли "
                                      "появится <br/># “Hello World!”</p></body></html>"))
        self.text_3.setText(_translate("Form",
                                       "<html><head/><body><p align=\"justify\">При выводе переменной, "
                                       "в консоль</p><p align=\"justify\">выведется ее значение, любого типа</p><p "
                                       "align=\"justify\">данных (логический,строковый,"
                                       "</p><p align=\"justify\">целочисленный и т.п.), например:</p></body></html>"))
        self.code_3.setText(_translate("Form",
                                       "<html><head/><body><p>a = 2 #Целочисленный тип </p><p># данных<br/>b = “123” "
                                       "#Строковый тип </p><p># данных<br/>c = True #Логический тип </p><p># "
                                       "данных</p><p>print(a) #В консоли появится </p><p># “2”<br/>print(b) #В "
                                       "консоли появится </p><p># “123”<br/>print(c) #В консоли появится </p><p># "
                                       "“True”</p></body></html>"))
        self.back_btn.setWhatsThis(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
