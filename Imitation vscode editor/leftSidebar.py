'''
@author  jia1995
@date    2022/3/24
@context The editor's left sidebar.
'''
import tkinter as tk

class LeftSideBar(tk.Frame):
    def __init__(self, master, width=40, bg='gray'):
        tk.Frame.__init__(self, master, width=width, bg=bg)