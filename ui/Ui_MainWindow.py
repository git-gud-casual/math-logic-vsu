# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 780)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(640, 780))
        MainWindow.setMaximumSize(QSize(640, 780))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 10, 610, 732))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.coeffTable = QTableWidget(self.layoutWidget)
        self.coeffTable.setObjectName(u"coeffTable")
        self.coeffTable.setMinimumSize(QSize(400, 0))
        self.coeffTable.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_2.addWidget(self.coeffTable)

        self.horizontalSpacer_2 = QSpacerItem(80, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.freeCoeffTable = QTableWidget(self.layoutWidget)
        if (self.freeCoeffTable.columnCount() < 1):
            self.freeCoeffTable.setColumnCount(1)
        self.freeCoeffTable.setObjectName(u"freeCoeffTable")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.freeCoeffTable.sizePolicy().hasHeightForWidth())
        self.freeCoeffTable.setSizePolicy(sizePolicy1)
        self.freeCoeffTable.setMinimumSize(QSize(0, 400))
        self.freeCoeffTable.setMaximumSize(QSize(125, 400))
        self.freeCoeffTable.setMidLineWidth(0)
        self.freeCoeffTable.setRowCount(0)
        self.freeCoeffTable.setColumnCount(1)

        self.horizontalLayout_2.addWidget(self.freeCoeffTable)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.addLineBtn = QPushButton(self.layoutWidget)
        self.addLineBtn.setObjectName(u"addLineBtn")

        self.verticalLayout_2.addWidget(self.addLineBtn)

        self.deleteLineBtn = QPushButton(self.layoutWidget)
        self.deleteLineBtn.setObjectName(u"deleteLineBtn")

        self.verticalLayout_2.addWidget(self.deleteLineBtn)

        self.loadFromFileBtn = QPushButton(self.layoutWidget)
        self.loadFromFileBtn.setObjectName(u"loadFromFileBtn")

        self.verticalLayout_2.addWidget(self.loadFromFileBtn)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.answersPlainText = QPlainTextEdit(self.layoutWidget)
        self.answersPlainText.setObjectName(u"answersPlainText")
        self.answersPlainText.setEnabled(True)
        self.answersPlainText.setMinimumSize(QSize(0, 150))
        self.answersPlainText.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.answersPlainText)

        self.getAnswersBtn = QPushButton(self.layoutWidget)
        self.getAnswersBtn.setObjectName(u"getAnswersBtn")

        self.verticalLayout_2.addWidget(self.getAnswersBtn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Systems Of Linear Equations", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0435\u043d\u0442\u044b \u043f\u0440\u0438 \u043f\u0435\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0435\u043d\u0442\u044b", None))
        self.addLineBtn.setText(QCoreApplication.translate("MainWindow", u"Add Line", None))
        self.deleteLineBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Line", None))
        self.loadFromFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load From File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Answers", None))
        self.getAnswersBtn.setText(QCoreApplication.translate("MainWindow", u"Get Answers", None))
    # retranslateUi

