'''
@author  jia1995
@date    2022/3/24
@context The editor's bottom sidebar.
'''
import tkinter as tk

class BottomSideBar(tk.Frame):
    def __init__(self, master, height=20, bg='blue') -> None:
        tk.Frame.__init__(self, master, height=height, bg=bg)