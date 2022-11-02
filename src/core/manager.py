import os   
import codecs
from PySide6 import QtCore, QtWidgets, QtGui
from src.core.gui import MainScreen
import sys
from pathlib import Path
class WindowManager():
    def __init__(self):
        self.Buttons = []
        self.allWindows = []
        self.app = QtWidgets.QApplication([])
        self.currentPath = Path().absolute()
        
    def createWindow(self,WindowName:str,windowSize:list,htmlFile:str):
        self.windowName = WindowName
        self.htmlFile = htmlFile
        self.windowSize1 = windowSize[0]
        self.windowSize2 = windowSize[1]
        self.Window = MainScreen(windowTitle=self.windowName)
        
        self.allWindows.append(self.Window)
        self.Window.resize(self.windowSize1,self.windowSize2)

        # Adds Data From Provided HTML file and Puts it in the Window

        self.view = MainScreen.LoadWebData(htmlFile=self.htmlFile)
        self.view.setParent(self.Window)
       
        self.view.setFixedSize(1920,1080)
        self.view.setMinimumSize(self.windowSize1,self.windowSize2)
    
   
    def run(self):
        for window in self.allWindows:
            window.show()
        
        sys.exit(self.app.exec())
        



        



