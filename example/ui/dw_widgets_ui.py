# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_widgets.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from qtpy import QtCore, QtGui, QtWidgets


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(879, 548)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_81 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.gridLayout.addWidget(self.label_81, 0, 1, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_82.setFont(font)
        self.label_82.setObjectName("label_82")
        self.gridLayout.addWidget(self.label_82, 0, 2, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_56.setMinimumSize(QtCore.QSize(0, 0))
        self.label_56.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.gridLayout.addWidget(self.label_56, 1, 0, 1, 1)
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setAlternatingRowColors(True)

        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(item.flags() | ~QtCore.Qt.ItemIsSelectable | ~QtCore.Qt.ItemIsSelectable)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 1, 1, 1, 1)
        self.listWidgetDis = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidgetDis.setEnabled(False)
        self.listWidgetDis.setObjectName("listWidgetDis")
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDis.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidgetDis.addItem(item)
        self.gridLayout.addWidget(self.listWidgetDis, 1, 2, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_57.setMinimumSize(QtCore.QSize(0, 0))
        self.label_57.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout.addWidget(self.label_57, 2, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_3 = QtWidgets.QTreeWidgetItem(item_2)
        item_4 = QtWidgets.QTreeWidgetItem(item_3)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidget, 2, 1, 1, 1)
        self.treeWidgetDis = QtWidgets.QTreeWidget(self.dockWidgetContents)
        self.treeWidgetDis.setEnabled(False)
        self.treeWidgetDis.setObjectName("treeWidgetDis")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDis)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidgetDis)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidgetDis, 2, 2, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_58.setMinimumSize(QtCore.QSize(0, 0))
        self.label_58.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.gridLayout.addWidget(self.label_58, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 1)
        self.tableWidgetDis = QtWidgets.QTableWidget(self.dockWidgetContents)
        self.tableWidgetDis.setEnabled(False)
        self.tableWidgetDis.setObjectName("tableWidgetDis")
        self.tableWidgetDis.setColumnCount(2)
        self.tableWidgetDis.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetDis.setItem(2, 1, item)
        self.gridLayout.addWidget(self.tableWidgetDis, 3, 2, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Widgets"))
        self.label_81.setText(_translate("DockWidget", "Enabled"))
        self.label_82.setText(_translate("DockWidget", "Disabled"))
        self.label_56.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_56.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_56.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_56.setText(_translate("DockWidget", "ListWidget"))
        self.listWidget.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.listWidget.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.listWidget.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidget.item(1)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidget.item(2)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidget.item(3)
        item.setText(_translate("DockWidget", "New Item"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidgetDis.isSortingEnabled()
        self.listWidgetDis.setSortingEnabled(False)
        item = self.listWidgetDis.item(0)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidgetDis.item(1)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidgetDis.item(2)
        item.setText(_translate("DockWidget", "New Item"))
        item = self.listWidgetDis.item(3)
        item.setText(_translate("DockWidget", "New Item"))
        self.listWidgetDis.setSortingEnabled(__sortingEnabled)
        self.label_57.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_57.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_57.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_57.setText(_translate("DockWidget", "TreeWidget"))
        self.treeWidget.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.treeWidget.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.treeWidget.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.treeWidget.setSortingEnabled(True)
        self.treeWidget.headerItem().setText(0, _translate("DockWidget", "New Column"))
        self.treeWidget.headerItem().setText(1, _translate("DockWidget", "New Column"))
        self.treeWidget.headerItem().setText(2, _translate("DockWidget", "New Column"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("DockWidget", "Test"))
        self.treeWidget.topLevelItem(0).child(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(0).child(0).child(1).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).child(2).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).child(3).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(0).child(0).child(4).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(2).child(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(2).child(0).child(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(2).child(0).child(0).child(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.topLevelItem(2).child(1).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(2).child(2).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(2).child(3).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidget.topLevelItem(5).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.treeWidgetDis.setSortingEnabled(True)
        self.treeWidgetDis.headerItem().setText(0, _translate("DockWidget", "New Column"))
        self.treeWidgetDis.headerItem().setText(1, _translate("DockWidget", "New Column"))
        __sortingEnabled = self.treeWidgetDis.isSortingEnabled()
        self.treeWidgetDis.setSortingEnabled(False)
        self.treeWidgetDis.topLevelItem(0).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidgetDis.topLevelItem(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidgetDis.topLevelItem(0).child(0).setText(1, _translate("DockWidget", "Test"))
        self.treeWidgetDis.topLevelItem(0).child(0).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidgetDis.topLevelItem(1).setText(0, _translate("DockWidget", "New Item"))
        self.treeWidgetDis.topLevelItem(1).child(0).setText(0, _translate("DockWidget", "New Subitem"))
        self.treeWidgetDis.setSortingEnabled(__sortingEnabled)
        self.label_58.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.label_58.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.label_58.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        self.label_58.setText(_translate("DockWidget", "TableWidget"))
        self.tableWidget.setToolTip(_translate("DockWidget", "This is a tool tip"))
        self.tableWidget.setStatusTip(_translate("DockWidget", "This is a status tip"))
        self.tableWidget.setWhatsThis(_translate("DockWidget", "This is \"what is this\""))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("DockWidget", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("DockWidget", "New Column"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("DockWidget", "1.23"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("DockWidget", "Hello"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("DockWidget", "1,45"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("DockWidget", "Olá"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("DockWidget", "12/12/2012"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("DockWidget", "Oui"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidgetDis.verticalHeaderItem(0)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidgetDis.verticalHeaderItem(1)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidgetDis.verticalHeaderItem(2)
        item.setText(_translate("DockWidget", "New Row"))
        item = self.tableWidgetDis.horizontalHeaderItem(0)
        item.setText(_translate("DockWidget", "New Column"))
        item = self.tableWidgetDis.horizontalHeaderItem(1)
        item.setText(_translate("DockWidget", "New Column"))
        __sortingEnabled = self.tableWidgetDis.isSortingEnabled()
        self.tableWidgetDis.setSortingEnabled(False)
        item = self.tableWidgetDis.item(0, 0)
        item.setText(_translate("DockWidget", "1.23"))
        item = self.tableWidgetDis.item(0, 1)
        item.setText(_translate("DockWidget", "Hello"))
        item = self.tableWidgetDis.item(1, 0)
        item.setText(_translate("DockWidget", "1,45"))
        item = self.tableWidgetDis.item(1, 1)
        item.setText(_translate("DockWidget", "Olá"))
        item = self.tableWidgetDis.item(2, 0)
        item.setText(_translate("DockWidget", "12/12/2012"))
        item = self.tableWidgetDis.item(2, 1)
        item.setText(_translate("DockWidget", "Oui"))
        self.tableWidgetDis.setSortingEnabled(__sortingEnabled)
