# Файл, с интерфейсом Главного меню программы, присутствуют 8 кнопок

# Импорт модулей из библиотеки
from PyQt6 import QtCore, QtGui, QtWidgets

# Импорт файла ресурсов resource_rc
import resource_rc


class Ui_Main_Menu(object):
    def __init__(self):
        self.line = None
        self.Title3 = None
        self.c2_q_btn = None
        self.c3_q_btn = None
        self.complication3_btn = None
        self.complication2_btn = None
        self.c1_q_btn = None
        self.complication1_btn = None
        self.formLayout = None
        self.Go_btn = None
        self.horizontalLayout = None
        self.gridLayout_3 = None
        self.Title2 = None
        self.Title1 = None
        self.gridLayout_2 = None
        self.gridLayout = None
        self.centralwidget = None
        self.label = None
        self.pushButton = None

    def setupUi(self, Main_Menu_win):
        Main_Menu_win.setObjectName("MainWindow")
        Main_Menu_win.resize(640, 480)
        Main_Menu_win.setMinimumSize(QtCore.QSize(640, 480))
        Main_Menu_win.setMaximumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/recurce/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Main_Menu_win.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Main_Menu_win)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 480))
        self.centralwidget.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(25, 20, 30, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 5, 1)
        self.Title1 = QtWidgets.QLabel(self.centralwidget)
        self.Title1.setMinimumSize(QtCore.QSize(0, 60))
        self.Title1.setMaximumSize(QtCore.QSize(16777215, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 129, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 129, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 129, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        self.Title1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.Title1.setFont(font)
        self.Title1.setStyleSheet("font-weight: bold")
        self.Title1.setObjectName("Title1")
        self.gridLayout_2.addWidget(self.Title1, 0, 0, 1, 1)
        self.Title2 = QtWidgets.QLabel(self.centralwidget)
        self.Title2.setMinimumSize(QtCore.QSize(0, 80))
        self.Title2.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.Title2.setFont(font)
        self.Title2.setObjectName("Title2")
        self.gridLayout_2.addWidget(self.Title2, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Go_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Go_btn.setMinimumSize(QtCore.QSize(250, 40))
        self.Go_btn.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        self.Go_btn.setFont(font)
        self.Go_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color: rgb(95, 136, 240);\n"
                                  "border-radius: 14px;")
        self.Go_btn.setObjectName("Go_btn")
        self.horizontalLayout.addWidget(self.Go_btn)
        spacerItem = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.complication1_btn = QtWidgets.QPushButton(self.centralwidget)
        self.complication1_btn.setMinimumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.complication1_btn.setFont(font)
        self.complication1_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(95, 136, 240);\n"
                                             "border-radius: 11px;\n"
                                             "align=\"left\";")
        self.complication1_btn.setObjectName("complication1_btn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.complication1_btn)
        self.c1_q_btn = QtWidgets.QPushButton(self.centralwidget)
        self.c1_q_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.c1_q_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.c1_q_btn.setStyleSheet("image: url(:/recurce/coolicon.png);\n"
                                    "border-style: none;")
        self.c1_q_btn.setText("")
        self.c1_q_btn.setObjectName("c1_q_btn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.c1_q_btn)
        self.complication2_btn = QtWidgets.QPushButton(self.centralwidget)
        self.complication2_btn.setMinimumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        self.complication2_btn.setFont(font)
        self.complication2_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(95, 136, 240);\n"
                                             "border-radius: 11px;")
        self.complication2_btn.setObjectName("complication2_btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.complication2_btn)
        self.complication3_btn = QtWidgets.QPushButton(self.centralwidget)
        self.complication3_btn.setMinimumSize(QtCore.QSize(400, 35))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        self.complication3_btn.setFont(font)
        self.complication3_btn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                             "background-color: rgb(95, 136, 240);\n"
                                             "border-radius: 11px;")
        self.complication3_btn.setObjectName("complication3_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.complication3_btn)
        self.c3_q_btn = QtWidgets.QPushButton(self.centralwidget)
        self.c3_q_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.c3_q_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.c3_q_btn.setStyleSheet("image: url(:/recurce/coolicon.png);\n"
                                    "border-style: none;")
        self.c3_q_btn.setText("")
        self.c3_q_btn.setObjectName("c3_q_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.c3_q_btn)
        self.c2_q_btn = QtWidgets.QPushButton(self.centralwidget)
        self.c2_q_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.c2_q_btn.setMaximumSize(QtCore.QSize(40, 16777215))
        self.c2_q_btn.setStyleSheet("image: url(:/recurce/coolicon.png);\n"
                                    "border-style: none;")
        self.c2_q_btn.setText("")
        self.c2_q_btn.setObjectName("c2_q_btn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.c2_q_btn)
        self.Title3 = QtWidgets.QLabel(self.centralwidget)
        self.Title3.setMinimumSize(QtCore.QSize(0, 60))
        self.Title3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Title3.setFont(font)
        self.Title3.setStyleSheet("font-weight: bold")
        self.Title3.setObjectName("Title3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.Title3)
        self.gridLayout_3.addLayout(self.formLayout, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 3, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 5, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(95, 136, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("image: url(:/recurce/book.png);\n"
                                      "border: none;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 7, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 2)
        Main_Menu_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main_Menu_win)
        QtCore.QMetaObject.connectSlotsByName(Main_Menu_win)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Triad of The Mind"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><img src=\":/recurce/flag "
                                      "Pic.jpg\"/></p></body></html>"))
        self.Title1.setText(_translate("MainWindow", "Привет!"))
        self.Title2.setText(_translate("MainWindow",
                                       "<html><head/><body><p>Готовься снова погрузится в<br/>изучение языка Python! "
                                       "</p><p><br/></p></body></html>"))
        self.Go_btn.setText(_translate("MainWindow", "Выбор уровня"))
        self.complication1_btn.setText(_translate("MainWindow", "Падаван"))
        self.complication2_btn.setText(_translate("MainWindow", "Генерал - джедай (в разработке)"))
        self.complication3_btn.setText(_translate("MainWindow", "Магистр (в разработке)"))
        self.Title3.setText(_translate("MainWindow", "Основные этапы"))
        self.pushButton.setText(_translate("MainWindow", "                                 Книга знаний"))
