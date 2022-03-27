'''
@author  jia1995
@date    2022/3/27
@context The Main editor place element.
'''
import tkinter as tk
from tkinter import *
from textwithLine import TextWithLine

def cut(editor, event=None):
    k = editor.tag_ranges('sel')
    if not k:
        idx = editor.index(tk.INSERT)
        line = idx.split('.')[0]
        editor.tag_add('sel',f'{line}.0',f'{int(line)+1}.0')
        editor.event_generate("<<Cut>>")
    else:
        editor.event_generate("<<Cut>>")

def copy(editor, event=None):
    k = editor.tag_ranges('sel')
    if not k:
        idx = editor.index(tk.INSERT)
        line = idx.split('.')[0]
        lens = len(editor.get('1.0', tk.END))
        editor.tag_add('sel',f'{line}.0',f'{line}.{lens}')
        editor.event_generate("<<Copy>>")
        editor.tag_remove('sel', '0.0', tk.END)
    else:
        editor.event_generate("<<Copy>>")

def paste(editor, event=None):
    editor.event_generate('<<Paste>>')

def selectAll(editor, event=None):
    editor.tag_add('sel','1.0',tk.END)

def undo(editor, event=None):
    editor.event_generate('<<Undo>>')

def redo(editor, event=None):
    editor.event_generate('<<Redo>>')

class TextEditor(tk.Frame):
    def __init__(self, master=None) -> None:
        tk.Frame.__init__(self, master)
        self.CreateText()
      
    def _create_right_popup_menu(self):
        PopupMenu = Menu(self.editbox.text, tearoff=0)
        PopupMenu.add_command(label='剪切',command=lambda:cut(self.editbox.text))
        PopupMenu.add_command(label='复制',command=lambda:copy(self.editbox.text))
        PopupMenu.add_command(label='粘贴',command=lambda:paste(self.editbox.text))
        PopupMenu.add_command(label='全选',command=lambda:selectAll(self.editbox.text))
        return PopupMenu

    def CreateText(self):
        self.editbox = TextWithLine(self.master)
        self.editbox.pack(expand=YES,side=RIGHT, fill=BOTH)
        PopupMenu = self._create_right_popup_menu()
        self.editbox.text.bind('<Button-3>',lambda event : PopupMenu.post(event.x_root, event.y_root))