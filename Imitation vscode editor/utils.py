'''
@author  jia1995
@date    2022/3/27
@context The appendix utils function.
'''
import os
import tkinter as tk
import platform
from textEidtor import TextEditor
from tkinter import filedialog

def cut(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    textWidget = editor.datax[filename].editbox.text
    k = textWidget.tag_ranges('sel')
    if not k:
        idx = textWidget.index(tk.INSERT)
        line = idx.split('.')[0]
        textWidget.tag_add('sel',f'{line}.0',f'{int(line)+1}.0')
        textWidget.event_generate("<<Cut>>")
    else:
        textWidget.event_generate("<<Cut>>")

def copy(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    textWidget = editor.datax[filename].editbox.text
    k = textWidget.tag_ranges('sel')
    if not k:
        idx = textWidget.index(tk.INSERT)
        line = idx.split('.')[0]
        lens = len(textWidget.get('1.0', tk.END))
        textWidget.tag_add('sel',f'{line}.0',f'{line}.{lens}')
        textWidget.event_generate("<<Copy>>")
        textWidget.tag_remove('sel', '0.0', tk.END)
    else:
        textWidget.event_generate("<<Copy>>")

def paste(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    textWidget = editor.datax[filename].editbox.text
    textWidget.event_generate('<<Paste>>')

def selectAll(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    textWidget = editor.datax[filename].editbox.text
    textWidget.tag_add('sel','1.0',tk.END)

def undo(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    texteditor = editor.datax[filename]
    textWidget = texteditor.editbox.text
    textWidget.event_generate('<<Undo>>')

def redo(editor, event=None):
    if editor.select()=='': return
    filename = editor.tab(editor.select(), "text")
    texteditor = editor.datax[filename]
    textWidget = texteditor.editbox.text
    textWidget.event_generate('<<Redo>>')

def newfile(editor):
    frame = tk.Frame(editor)
    texteditor = TextEditor(frame)
    editor.add(frame,text='Untitled')
    editor.select(frame)
    filename = editor.tab(editor.select(), "text")
    editor.datax[filename] = texteditor
    editor.origin_data[filename] = texteditor.editbox.get(1.0, tk.END)


def openfile(editbox, path=None):
    systype = platform.system() # 判断系统类型
    if path and os.path.exists(path):
        basedir = path
    elif systype == 'Windows':
        basedir = 'c:\\'
    else:
        basedir = '/'
    filename = filedialog.askopenfilename(initialdir=basedir)
    frame = tk.Frame(editbox)
    texteditor = TextEditor(frame)
    editbox.add(frame,text=filename)
    editbox.select(frame)
    try:
        fobj_r = open(filename, 'rb')
    except IOError as errmsg:
        print('*** Failed open file:', errmsg)
    else:
        texteditor.editbox.delete(1.0, tk.END)
        texteditor.editbox.insert(tk.INSERT, fobj_r.read())
        fobj_r.close()
        editbox.datax[filename] = texteditor
        editbox.origin_data[filename] = texteditor.editbox.get(1.0, tk.END)

def saveas(editbox, filename='Untitled-1'):
    filename1 = filedialog.asksaveasfilename(initialfile=filename)
    tid = editbox.select()
    filename = editbox.tab(tid, "text")
    textWidget = editbox.datax[filename]
    save_data = textWidget.editbox.text.get(1.0, tk.END)
    with open(filename1, 'w') as f:
        f.write(save_data)
        f.flush()
    del editbox.datax[filename]
    del editbox.origin_data[filename]
    editbox.datax[filename1] = textWidget
    editbox.origin_data[filename1] = save_data
    editbox.tab('current', text=filename1)
    f.close()

def savefile(editbox):
    try:
        filename = editbox.tab(editbox.select(), "text")
        textWidget = editbox.datax[filename]
        save_data = textWidget.editbox.text.get(1.0, tk.END)
        try:
            if os.path.exists(filename):
                with open(filename,'w') as f:
                    f.write(save_data)
                    f.flush()
                f.close()
                editbox.origin_data[filename] = save_data
            else:
                saveas(editbox)
        except Exception:
            pass
    except Exception:
        pass