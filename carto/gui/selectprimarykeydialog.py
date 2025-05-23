import os

from qgis.core import Qgis
from qgis.gui import QgsMessageBar

from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog, QSizePolicy, QFileDialog


WIDGET, BASE = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "selectprimarykeydialog.ui")
)


class SelectPrimaryKeyDialog(BASE, WIDGET):
    def __init__(self, columns, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)

        self.btnSetPrimaryKey.clicked.connect(self.okClicked)
        self.btnSkip.clicked.connect(self.reject)

        self.initGui(columns)

        self.pk = None

    def initGui(self, columns):
        self.comboPK.addItems(columns)

    def okClicked(self):
        self.pk = self.comboPK.currentText()
        self.accept()
