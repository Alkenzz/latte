from PyQt5 import QtCore, QtWidgets


class Latte_UI(object):
    def setup_UI(self, MainWindow):
        MainWindow.setObjectName('Latte')
        MainWindow.resize(589, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName('verticalLayout')
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName('tableWidget')
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.editPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.editPushButton.setObjectName('editPushButton')
        self.horizontalLayout.addWidget(self.editPushButton)
        self.newPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.newPushButton.setObjectName('newPushButton')
        self.horizontalLayout.addWidget(self.newPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslate_UI(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_UI(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate('Latte', 'Latte'))
        self.editPushButton.setText(_translate('Latte', 'Изменить'))
        self.newPushButton.setText(_translate('Latte', 'Создать новый'))