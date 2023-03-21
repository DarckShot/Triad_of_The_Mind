# Диалоговое окно, появляющееся при нажатия "Описания" для "Падаван" (знак вопроса)

# Импорт модулей из библиотеки
from PyQt6 import QtCore, QtGui, QtWidgets

# Импорт файла ресурсов resource_rc
import resource_rc


class Ui_Question_1(object):
    def __init__(self):
        self.OK_btn = None
        self.horizontalLayout = None
        self.text_1 = None
        self.verticalLayout = None
        self.gridLayout_2 = None

    def setupUi(self, Question_1):
        Question_1.setObjectName("Question_1")
        Question_1.resize(520, 341)
        Question_1.setMinimumSize(QtCore.QSize(520, 341))
        Question_1.setMaximumSize(QtCore.QSize(520, 341))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurce/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Question_1.setWindowIcon(icon)
        Question_1.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.gridLayout_2 = QtWidgets.QGridLayout(Question_1)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_1 = QtWidgets.QLabel(Question_1)
        self.text_1.setMinimumSize(QtCore.QSize(0, 248))
        self.text_1.setMaximumSize(QtCore.QSize(609, 363))
        self.text_1.setObjectName("text_1")
        self.verticalLayout.addWidget(self.text_1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.OK_btn = QtWidgets.QPushButton(Question_1)
        self.OK_btn.setMinimumSize(QtCore.QSize(0, 50))
        self.OK_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(18)
        self.OK_btn.setFont(font)
        self.OK_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(95, 136, 240);\n"
                                  "border-radius: 14px;")
        self.OK_btn.setObjectName("OK_btn")
        self.horizontalLayout.addWidget(self.OK_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Question_1)
        QtCore.QMetaObject.connectSlotsByName(Question_1)

    def retranslateUi(self, Question_1):
        _translate = QtCore.QCoreApplication.translate
        Question_1.setWindowTitle(_translate("Question_1", "Information"))
        self.text_1.setText(_translate("Question_1",
                                       "<html><head/><body><p><span style=\" font-size:20pt;\">Сложность "
                                       "&quot;Падаван&quot; предназначена</span></p><p><span style=\" "
                                       "font-size:20pt;\">для начала обучения Python.</span></p><p><span style=\" "
                                       "font-size:20pt;\">Выбирайте эту сложность, если у вас</span></p><p><span "
                                       "style=\" font-size:20pt;\">нет знаний в Python и вы хотите "
                                       "</span></p><p><span style=\" font-size:20pt;\">изучить его с "
                                       "нуля.</span></p></body></html>"))
        self.OK_btn.setText(_translate("Question_1", "OK"))

