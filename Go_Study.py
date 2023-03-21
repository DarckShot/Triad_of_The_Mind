# Файл, с интерфейсом Начального экрана программы

# Импорт модулей из библиотеки
from PyQt6 import QtCore, QtGui, QtWidgets

# Импорт файла ресурсов resource_rc
import resource_rc


class Ui_Go_Study(object):
    def __init__(self):
        self.label_Title_3 = None
        self.go_studyButtob = None
        self.horizontalLayout = None
        self.verticalLayout_2 = None
        self.label_Title_2 = None
        self.label_Title = None
        self.logo = None
        self.horizontalLayout_2 = None
        self.verticalLayout = None
        self.verticalLayout_7 = None
        self.centralwidget = None

    def setupUi(self, Go_Study_win):
        Go_Study_win.setObjectName("MainWindow")
        Go_Study_win.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Go_Study_win.setEnabled(True)
        Go_Study_win.resize(640, 480)
        Go_Study_win.setMinimumSize(QtCore.QSize(640, 480))
        Go_Study_win.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurce/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Go_Study_win.setWindowIcon(icon)
        Go_Study_win.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(Go_Study_win)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setStyleSheet("background-color: rgb(95, 136, 240);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 40, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setMinimumSize(QtCore.QSize(70, 70))
        self.logo.setMaximumSize(QtCore.QSize(70, 70))
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title.sizePolicy().hasHeightForWidth())
        self.label_Title.setSizePolicy(sizePolicy)
        self.label_Title.setMinimumSize(QtCore.QSize(640, 60))
        self.label_Title.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_Title.setFont(font)
        self.label_Title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_Title.setStyleSheet("font-weight: bold; color:white")
        self.label_Title.setObjectName("label_Title")
        self.verticalLayout.addWidget(self.label_Title)
        self.label_Title_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title_2.sizePolicy().hasHeightForWidth())
        self.label_Title_2.setSizePolicy(sizePolicy)
        self.label_Title_2.setMinimumSize(QtCore.QSize(640, 0))
        self.label_Title_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title_2.setFont(font)
        self.label_Title_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_Title_2.setStyleSheet("color:white")
        self.label_Title_2.setObjectName("label_Title_2")
        self.verticalLayout.addWidget(self.label_Title_2)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 70, -1, 80)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        # Кнопка далее (переходит на Main Menu ())
        self.go_studyButtob = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy.setHeightForWidth(self.go_studyButtob.sizePolicy().hasHeightForWidth())
        self.go_studyButtob.setSizePolicy(sizePolicy)
        self.go_studyButtob.setMinimumSize(QtCore.QSize(40, 50))
        self.go_studyButtob.setMaximumSize(QtCore.QSize(40, 50))
        self.go_studyButtob.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.go_studyButtob.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.go_studyButtob.setStyleSheet("image: url(:/recurce/arrow.png);\n"
                                          "border: none;\n")
        self.go_studyButtob.setText("")
        self.go_studyButtob.setAutoDefault(False)
        self.go_studyButtob.setObjectName("go_studyButtob")
        self.horizontalLayout.addWidget(self.go_studyButtob)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_Title_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title_3.sizePolicy().hasHeightForWidth())
        self.label_Title_3.setSizePolicy(sizePolicy)
        self.label_Title_3.setMinimumSize(QtCore.QSize(640, 30))
        self.label_Title_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_Title_3.setFont(font)
        self.label_Title_3.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_Title_3.setStyleSheet("color:white")
        self.label_Title_3.setObjectName("label_Title_3")
        self.verticalLayout_2.addWidget(self.label_Title_3)
        self.verticalLayout_7.addLayout(self.verticalLayout_2)
        Go_Study_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Go_Study_win)
        QtCore.QMetaObject.connectSlotsByName(Go_Study_win)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Triad of The Mind"))
        self.logo.setText(_translate("MainWindow",
                                     "<html><head/><body><p align=\"center\"><img "
                                     "src=\":/recurce/logo.png\"/></p></body></html>"))
        self.label_Title.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Triad of The Mind</p></body></html>"))
        self.label_Title_2.setText(_translate("MainWindow",
                                              "<html><head/><body><p align=\"center\"><span style=\" "
                                              "font-size:14pt;\">Обучение языку программирования Python "
                                              "3.8</span></p></body></html>"))
        self.label_Title_3.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Начало обучения</p></body></html>"))
