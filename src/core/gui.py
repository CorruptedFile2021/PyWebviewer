from PySide6 import QtCore, QtWidgets, QtGui , QtWebEngineCore , QtWebEngineQuick , QtWebEngineWidgets
import os
from pathlib import Path
class MainScreen(QtWidgets.QWidget):
    def __init__(self,windowTitle:str):
        super().__init__()
        self.WindowTitle = windowTitle
        self.setWindowTitle(windowTitle)
        
    
    @classmethod
    def LoadWebData(self,htmlFile:str):
        if htmlFile.startswith("http") == False:
                with open(f"{htmlFile}") as f:
                    self.htmlData = f.read()
        self.view = QtWebEngineWidgets.QWebEngineView()
        
        self.view.setUrl(f"{htmlFile}")
        
        
        
        
        return self.view
    
   


