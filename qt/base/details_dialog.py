# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2010-02-05
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog

from core.gui.details_panel import DetailsPanel

from .details_table import DetailsModel

class DetailsDialog(QDialog):
    def __init__(self, parent, app):
        QDialog.__init__(self, parent, Qt.Tool)
        self.app = app
        self.model = DetailsPanel(self, app)
        self._setupUi()
        self.tableModel = DetailsModel(self.model)
        # tableView is defined in subclasses
        self.tableView.setModel(self.tableModel)
        self.model.connect()
    
    def _setupUi(self): # Virtual
        pass
    
    # model --> view
    def refresh(self):
        self.tableModel.reset()
    
