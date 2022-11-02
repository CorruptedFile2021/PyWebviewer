from PyWebviewer.core import WindowManager

manager = WindowManager() # Initializes The Windows Manager

manager.createWindow("Example",[1200,720],htmlFile="https://www.youtube.com") #Creates a Window, The htmlFile Parameter Can also Be a Url(must start with https://) or a HTML File
# To Add CSS to The Html File just make sure it is linked in the html file 

manager.run() # Starts the App and Opens all the Windows

