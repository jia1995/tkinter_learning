'''
@author  jia1995
@date    2022/3/27
@context Text with line.
@src    https://codingdict.com/questions/194275
'''
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)

class CustomText(ScrolledText):
    def __init__(self, *args, **kwargs):
        ScrolledText.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if args[0] == 'get' and (args[1] == 'sel.first' and args[2] == 'sel.last') and not self.tag_ranges('sel'): return

        # avoid error when deleting
        if args[0] == 'delete' and (args[1] == 'sel.first' and args[2] == 'sel.last') and not self.tag_ranges('sel'): return
        cmd = (self._orig,) + args
        try:
            result = self.tk.call(cmd)
        except:
            result = self.tk.call((self._orig, 'edit', 'separator'))
            # print(cmd)
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")
        # return what the actual widget returned
        return result

class TextWithLine(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = CustomText(self, undo=True,autoseparators=True, maxundo=-1)
        self.filename = ''
        self.path = ''
        
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)
        self.linenumbers.pack(side="left", fill="y")
        self.text.pack(side="right", fill="both", expand=True)
        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)

    def _on_change(self, event):
        self.linenumbers.redraw()
    
    def insert(self, index, chars, *args):
        self.text.insert(index, chars, *args)
    
    def get(self,index1, index2 = ...):
        return self.text.get(index1, index2)
    
    def delete(self, index1, index2=...):
        self.text.delete(index1, index2)

if __name__ == "__main__":
    root = tk.Tk()
    TextWithLine(root).pack(side="top", fill="both", expand=True)
    root.mainloop()