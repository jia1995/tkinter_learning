'''
@author  jia1995
@date    2022/3/24
@context The editor's main eidtor.
'''
import tkinter as tk
from tkinter import ttk
from menuBar import MenuBar
from leftSidebar import LeftSideBar
from bottomSidebar import BottomSideBar
from notebook import CustomNotebook

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        winWidth = 600
        winHeight = 400
        # 获取屏幕分辨率
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        self.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        self.menu = MenuBar(self)
        self.leftSide = LeftSideBar(self)
        self.bottom = BottomSideBar(self)
        self.bottom.pack(side=tk.BOTTOM,fill=tk.BOTH)
        self.leftSide.pack(side=tk.LEFT,fill=tk.BOTH)
        self.menu.pack()
        self.text = CustomNotebook(self, width=200, height=150)
        self.text.pack(fill=tk.BOTH, expand=True)
        self.mainloop()
    
if __name__ =='__main__':
    app = App()