'''
@author  jia1995
@date    2022/3/24
@context The editor's menu sidebar.
'''
import tkinter as tk

from click import command

class MenuBar(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        
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
    
    def __fileBar(self):
        self.fBar.add_command(label='新建文件',command=self.__newFile)
        self.fBar.add_command(label='打开文件',command=self.__openFile)
        self.fBar.add_command(label='保存文件',command=self.__saveFile)
        self.fBar.add_command(label='关闭窗口',command=self.__exitFile)
    
    def __editBar(self):
        self.eBar.add_command(label='剪切', command=self.__cut)
        self.eBar.add_command(label='复制', command=self.__copy)
        self.eBar.add_command(label='粘贴', command=self.__paste)
        self.eBar.add_separator()
        self.eBar.add_command(label='查找', command=self.__search)
        self.eBar.add_command(label='替换', command=self.__replace)
        self.eBar.add_separator()
        self.eBar.add_command(label='撤销', command=self.__undo)
        self.eBar.add_command(label='恢复', command=self.__recover)
    
    def __cut(self):
        ...
    
    def __copy(self):
        ...
    
    def __paste(self):
        ...
    
    def __search(self):
        ...

    def __replace(self):
        ...
    
    def __undo(self):
        ...
    
    def __recover(self):
        ...
    
    def __newFile(self):
        ...
    
    def __openFile(self):
        ...

    def __saveFile(self):
        ...
    
    def __exitFile(self):
        top = self.winfo_toplevel()
        top.quit()