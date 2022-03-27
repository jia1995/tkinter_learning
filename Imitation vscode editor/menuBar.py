'''
@author  jia1995
@date    2022/3/24
@context The editor's menu sidebar.
'''
import tkinter as tk
from utils import *

class MenuBar(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        self.root = master
        top['menu'] = self.menuBar

        self.fBar = tk.Menu(self.menuBar, tearoff=0)
        self.eBar = tk.Menu(self.menuBar, tearoff=0)
        self.s1Bar = tk.Menu(self.menuBar, tearoff=0)
        self.s2Bar = tk.Menu(self.menuBar, tearoff=0)
        self.hBar = tk.Menu(self.menuBar, tearoff=0)
        self.menuBar.add_cascade(label='文件', menu=self.fBar)
        self.menuBar.add_cascade(label='编辑', menu=self.eBar)
        self.menuBar.add_cascade(label='选择', menu=self.s2Bar)
        self.menuBar.add_cascade(label='查看', menu=self.s1Bar)
        self.menuBar.add_cascade(label='帮助', menu=self.hBar)
        self.__fileBar()
        self.__editBar()
        self.__selectBar()
        self.__searchBar()
    
    def __searchBar(self):
        self.s1Bar.add_command(label='全屏',command=self.__fullScreen)
        self.s1Bar.add_command(label='退出全屏',command=self.__quitFullScreen)

    def __fullScreen(self):
        top = self.winfo_toplevel()
        top.attributes('-fullscreen', True)
    
    def __quitFullScreen(self):
        top = self.winfo_toplevel()
        top.attributes('-fullscreen', False)

    def __selectBar(self):
        self.s2Bar.add_command(label='全选', command=lambda:selectAll(self.root.text))
    
    def __fileBar(self):
        self.fBar.add_command(label='新建文件',command=lambda: newfile(self.root.text))
        self.fBar.add_command(label='打开文件',command=lambda:openfile(self.root.text))
        self.fBar.add_command(label='保存文件',command=lambda:savefile(self.root.text))
        self.fBar.add_command(label='关闭窗口',command=self.__exitFile)
    
    def __editBar(self):
        self.eBar.add_command(label='剪切', command=lambda: cut(self.root.text))
        self.eBar.add_command(label='复制', command=lambda: copy(self.root.text))
        self.eBar.add_command(label='粘贴', command=lambda:paste(self.root.text))
        self.eBar.add_separator()
        self.eBar.add_command(label='查找', command=self.__search)
        self.eBar.add_command(label='替换', command=self.__replace)
        self.eBar.add_separator()
        self.eBar.add_command(label='撤销', command=lambda: undo(self.root.text))
        self.eBar.add_command(label='恢复', command=lambda: redo(self.root.text))
    
    def __search(self):
        ...

    def __replace(self):
        ...
    
    def __exitFile(self):
        top = self.winfo_toplevel()
        top.quit()