# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'osma_web_services_dock.ui'
#
# Created: Tue Mar 24 16:08:53 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_OsmaDockWidget(object):
    def setupUi(self, OsmaDockWidget):
        OsmaDockWidget.setObjectName(_fromUtf8("OsmaDockWidget"))
        OsmaDockWidget.resize(304, 653)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OsmaDockWidget.sizePolicy().hasHeightForWidth())
        OsmaDockWidget.setSizePolicy(sizePolicy)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.wmtsTab = QtGui.QWidget()
        self.wmtsTab.setObjectName(_fromUtf8("wmtsTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.wmtsTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.loadLayersWmtsButton = QtGui.QPushButton(self.wmtsTab)
        self.loadLayersWmtsButton.setObjectName(_fromUtf8("loadLayersWmtsButton"))
        self.gridLayout_2.addWidget(self.loadLayersWmtsButton, 2, 0, 1, 1)
        self.addWmtsButton = QtGui.QPushButton(self.wmtsTab)
        self.addWmtsButton.setObjectName(_fromUtf8("addWmtsButton"))
        self.gridLayout_2.addWidget(self.addWmtsButton, 2, 1, 1, 1)
        self.zoomExtentWmtsBox = QtGui.QCheckBox(self.wmtsTab)
        self.zoomExtentWmtsBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zoomExtentWmtsBox.setChecked(True)
        self.zoomExtentWmtsBox.setObjectName(_fromUtf8("zoomExtentWmtsBox"))
        self.gridLayout_2.addWidget(self.zoomExtentWmtsBox, 2, 2, 1, 1)
        self.wmtsTreeView = QtGui.QTreeView(self.wmtsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wmtsTreeView.sizePolicy().hasHeightForWidth())
        self.wmtsTreeView.setSizePolicy(sizePolicy)
        self.wmtsTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wmtsTreeView.setDragEnabled(False)
        self.wmtsTreeView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.wmtsTreeView.setObjectName(_fromUtf8("wmtsTreeView"))
        self.wmtsTreeView.header().setDefaultSectionSize(80)
        self.gridLayout_2.addWidget(self.wmtsTreeView, 1, 0, 1, 3)
        self.wmtsSearchLineEdit = QtGui.QLineEdit(self.wmtsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wmtsSearchLineEdit.sizePolicy().hasHeightForWidth())
        self.wmtsSearchLineEdit.setSizePolicy(sizePolicy)
        self.wmtsSearchLineEdit.setInputMask(_fromUtf8(""))
        self.wmtsSearchLineEdit.setText(_fromUtf8(""))
        self.wmtsSearchLineEdit.setObjectName(_fromUtf8("wmtsSearchLineEdit"))
        self.gridLayout_2.addWidget(self.wmtsSearchLineEdit, 0, 0, 1, 3)
        self.tabWidget.addTab(self.wmtsTab, _fromUtf8(""))
        self.wmsTab = QtGui.QWidget()
        self.wmsTab.setObjectName(_fromUtf8("wmsTab"))
        self.gridLayout_3 = QtGui.QGridLayout(self.wmsTab)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.addWmsButton = QtGui.QPushButton(self.wmsTab)
        self.addWmsButton.setObjectName(_fromUtf8("addWmsButton"))
        self.gridLayout_3.addWidget(self.addWmsButton, 2, 1, 1, 1)
        self.loadLayersWmsButton = QtGui.QPushButton(self.wmsTab)
        self.loadLayersWmsButton.setObjectName(_fromUtf8("loadLayersWmsButton"))
        self.gridLayout_3.addWidget(self.loadLayersWmsButton, 2, 0, 1, 1)
        self.zoomExtentWmsBox = QtGui.QCheckBox(self.wmsTab)
        self.zoomExtentWmsBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.zoomExtentWmsBox.setChecked(False)
        self.zoomExtentWmsBox.setObjectName(_fromUtf8("zoomExtentWmsBox"))
        self.gridLayout_3.addWidget(self.zoomExtentWmsBox, 2, 2, 1, 1)
        self.wmsTreeView = QtGui.QTreeView(self.wmsTab)
        self.wmsTreeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.wmsTreeView.setProperty("showDropIndicator", False)
        self.wmsTreeView.setDragEnabled(False)
        self.wmsTreeView.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.wmsTreeView.setDefaultDropAction(QtCore.Qt.LinkAction)
        self.wmsTreeView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.wmsTreeView.setObjectName(_fromUtf8("wmsTreeView"))
        self.wmsTreeView.header().setDefaultSectionSize(80)
        self.wmsTreeView.header().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.wmsTreeView, 1, 0, 1, 3)
        self.wmsSearchLineEdit = QtGui.QLineEdit(self.wmsTab)
        self.wmsSearchLineEdit.setObjectName(_fromUtf8("wmsSearchLineEdit"))
        self.gridLayout_3.addWidget(self.wmsSearchLineEdit, 0, 0, 1, 3)
        self.tabWidget.addTab(self.wmsTab, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.accessLabel = QtGui.QLabel(self.tab)
        self.accessLabel.setText(_fromUtf8(""))
        self.accessLabel.setWordWrap(True)
        self.accessLabel.setObjectName(_fromUtf8("accessLabel"))
        self.gridLayout_4.addWidget(self.accessLabel, 1, 2, 1, 1)
        self.personLabel = QtGui.QLabel(self.tab)
        self.personLabel.setText(_fromUtf8(""))
        self.personLabel.setWordWrap(True)
        self.personLabel.setObjectName(_fromUtf8("personLabel"))
        self.gridLayout_4.addWidget(self.personLabel, 2, 2, 1, 1)
        self.addrLabel = QtGui.QLabel(self.tab)
        self.addrLabel.setText(_fromUtf8(""))
        self.addrLabel.setWordWrap(True)
        self.addrLabel.setObjectName(_fromUtf8("addrLabel"))
        self.gridLayout_4.addWidget(self.addrLabel, 6, 2, 1, 1)
        self.phoneLabel = QtGui.QLabel(self.tab)
        self.phoneLabel.setText(_fromUtf8(""))
        self.phoneLabel.setWordWrap(True)
        self.phoneLabel.setObjectName(_fromUtf8("phoneLabel"))
        self.gridLayout_4.addWidget(self.phoneLabel, 14, 2, 1, 1)
        self.positionLabel = QtGui.QLabel(self.tab)
        self.positionLabel.setText(_fromUtf8(""))
        self.positionLabel.setWordWrap(True)
        self.positionLabel.setObjectName(_fromUtf8("positionLabel"))
        self.gridLayout_4.addWidget(self.positionLabel, 4, 2, 1, 1)
        self.twLogoLabel = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twLogoLabel.sizePolicy().hasHeightForWidth())
        self.twLogoLabel.setSizePolicy(sizePolicy)
        self.twLogoLabel.setMaximumSize(QtCore.QSize(10777215, 10777215))
        self.twLogoLabel.setText(_fromUtf8(""))
        self.twLogoLabel.setPixmap(QtGui.QPixmap(_fromUtf8(":/plugins/OsmaWebServices/resources/thinkwhere_logo.png")))
        self.twLogoLabel.setScaledContents(False)
        self.twLogoLabel.setOpenExternalLinks(True)
        self.twLogoLabel.setObjectName(_fromUtf8("twLogoLabel"))
        self.gridLayout_4.addWidget(self.twLogoLabel, 19, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 19, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 19, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem2, 16, 2, 1, 1)
        self.abstractLabel = QtGui.QLabel(self.tab)
        self.abstractLabel.setText(_fromUtf8(""))
        self.abstractLabel.setScaledContents(False)
        self.abstractLabel.setWordWrap(True)
        self.abstractLabel.setObjectName(_fromUtf8("abstractLabel"))
        self.gridLayout_4.addWidget(self.abstractLabel, 17, 2, 1, 1)
        self.titleLabel = QtGui.QLabel(self.tab)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName(_fromUtf8("titleLabel"))
        self.gridLayout_4.addWidget(self.titleLabel, 0, 2, 1, 1)
        self.emailLabel = QtGui.QLabel(self.tab)
        self.emailLabel.setText(_fromUtf8(""))
        self.emailLabel.setWordWrap(True)
        self.emailLabel.setObjectName(_fromUtf8("emailLabel"))
        self.gridLayout_4.addWidget(self.emailLabel, 18, 2, 1, 1)
        self.countryLabel = QtGui.QLabel(self.tab)
        self.countryLabel.setText(_fromUtf8(""))
        self.countryLabel.setWordWrap(True)
        self.countryLabel.setObjectName(_fromUtf8("countryLabel"))
        self.gridLayout_4.addWidget(self.countryLabel, 10, 2, 1, 1)
        self.cityLabel = QtGui.QLabel(self.tab)
        self.cityLabel.setText(_fromUtf8(""))
        self.cityLabel.setWordWrap(True)
        self.cityLabel.setObjectName(_fromUtf8("cityLabel"))
        self.gridLayout_4.addWidget(self.cityLabel, 8, 2, 1, 1)
        self.faxLabel = QtGui.QLabel(self.tab)
        self.faxLabel.setText(_fromUtf8(""))
        self.faxLabel.setWordWrap(True)
        self.faxLabel.setObjectName(_fromUtf8("faxLabel"))
        self.gridLayout_4.addWidget(self.faxLabel, 15, 2, 1, 1)
        self.postcodeLabel = QtGui.QLabel(self.tab)
        self.postcodeLabel.setText(_fromUtf8(""))
        self.postcodeLabel.setObjectName(_fromUtf8("postcodeLabel"))
        self.gridLayout_4.addWidget(self.postcodeLabel, 13, 2, 1, 1)
        self.orgLabel = QtGui.QLabel(self.tab)
        self.orgLabel.setText(_fromUtf8(""))
        self.orgLabel.setWordWrap(True)
        self.orgLabel.setObjectName(_fromUtf8("orgLabel"))
        self.gridLayout_4.addWidget(self.orgLabel, 5, 2, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        OsmaDockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(OsmaDockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(OsmaDockWidget)

    def retranslateUi(self, OsmaDockWidget):
        OsmaDockWidget.setWindowTitle(_translate("OsmaDockWidget", "OSMA Web Services", None))
        self.loadLayersWmtsButton.setText(_translate("OsmaDockWidget", "Load Layers", None))
        self.addWmtsButton.setText(_translate("OsmaDockWidget", "Add Selected", None))
        self.zoomExtentWmtsBox.setText(_translate("OsmaDockWidget", "Zoom to extent", None))
        self.wmtsSearchLineEdit.setToolTip(_translate("OsmaDockWidget", "Search WMTS Layers...", None))
        self.wmtsSearchLineEdit.setPlaceholderText(_translate("OsmaDockWidget", "Search WMTS layers_wms...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wmtsTab), _translate("OsmaDockWidget", "WMTS", None))
        self.addWmsButton.setText(_translate("OsmaDockWidget", "Add Selected", None))
        self.loadLayersWmsButton.setText(_translate("OsmaDockWidget", "Load Layers", None))
        self.zoomExtentWmsBox.setText(_translate("OsmaDockWidget", "Zoom to extent", None))
        self.wmsSearchLineEdit.setToolTip(_translate("OsmaDockWidget", "Search WMS Layers", None))
        self.wmsSearchLineEdit.setPlaceholderText(_translate("OsmaDockWidget", "Search WMS layers_wms...", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wmsTab), _translate("OsmaDockWidget", "WMS", None))
        self.titleLabel.setText(_translate("OsmaDockWidget", "Scottish Government OSMA Web Services", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("OsmaDockWidget", "About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    OsmaDockWidget = QtGui.QDockWidget()
    ui = Ui_OsmaDockWidget()
    ui.setupUi(OsmaDockWidget)
    OsmaDockWidget.show()
    sys.exit(app.exec_())

