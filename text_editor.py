import tkinter
import tkinter.filedialog as dialog
import tkinter.messagebox as message
import os
from os.path import basename

class a_notepad:
            
    def __init__(self):
        
        # create base GUI
        self.window = tkinter.Tk()
        self.filename = 'Untitled'
        self.original = ''
        self.window.title(self.filename + " - Andrea's Notepad")  
        self.text = tkinter.Text(self.window)
        self.text.pack(expand = 1, fill = tkinter.BOTH)
        
        # add keyboard commands
        self.window.bind('<Control-n>', lambda e: self.new_save_check())
        self.window.bind('<Control-o>', lambda e: self.open_save_check())
        self.window.bind('<Control-s>', lambda e: self.save())
        self.window.bind('<Control-p>', lambda e: self.hello())
        self.window.bind('<Control-z>', lambda e: self.hello())
        self.window.bind('<Control-x>', lambda e: self.hello())
        self.window.bind('<Control-v>', lambda e: self.hello())
        self.window.bind('<Delete>', lambda e: self.hello())
        self.window.bind('<Control-f>', lambda e: self.hello())
        self.window.bind('<F3>', lambda e: self.hello())
        self.window.bind('<Control-h>', lambda e: self.hello())
        self.window.bind('<Control-g>', lambda e: self.hello())
        self.window.bind('<Control-a>', lambda e: self.hello())
        self.window.bind('<F5>', lambda e: self.hello())
        
        # handler for window manager exit
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.quit())
        
        # create menus 
        self.menubar = tkinter.Menu(self.window)
        
        # create File pulldown menu
        self.filemenu = tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command= lambda: self.new_save_check(), accelerator="Ctrl+N")
        self.filemenu.add_command(label="Open...", command= lambda: self.open_save_check(), accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command = lambda : self.save(), accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save As...", command = lambda :self.saveas())
        self.filemenu.add_command(label="Page Setup...", command=lambda: self.hello())
        self.filemenu.add_command(label="Print...", command=lambda: self.hello(), accelerator="Ctrl+P")
        self.filemenu.add_command(label="Exit", command = lambda : self.quit())
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
        # create Edit pulldown menu
        self.editmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=lambda: self.hello(), accelerator="Ctrl+Z")
        self.editmenu.add_command(label="Cut", command=lambda: self.cut(), accelerator="Ctrl+X")
        self.editmenu.add_command(label="Copy", command=lambda: self.copy(), accelerator="Ctrl+C")
        self.editmenu.add_command(label="Paste", command=lambda: self.paste(), accelerator="Ctrl+V")
        self.editmenu.add_command(label="Delete", command=lambda: self.delete(), accelerator="Del")
        self.editmenu.add_command(label="Find...", command=lambda: self.hello(), accelerator="Ctrl+F")
        self.editmenu.add_command(label="Find Next", command=lambda: self.hello(), accelerator="F3")
        self.editmenu.add_command(label="Replace...", command=lambda: self.hello(), accelerator="Ctrl+H")
        self.editmenu.add_command(label="Go To...", command=lambda: self.hello(), accelerator="Ctrl+G")
        self.editmenu.add_command(label="Select All", command=lambda: self.hello(), accelerator="Ctrl+A")
        self.editmenu.add_command(label="Time/Date", command=lambda: self.hello(), accelerator="F5")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        
        # create Format pulldown menu
        self.formatmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.formatmenu.add_command(label="Word Wrap", command=lambda: self.hello())
        self.formatmenu.add_command(label="Font...", command=lambda: self.hello())
        self.menubar.add_cascade(label="Format", menu=self.formatmenu)
        
        # create View pulldown menu
        self.viewmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Status Bar", command=lambda: self.hello())
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        
        # create Help pulldown menu
        self.helpmenu = tkinter.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About", command=lambda: self.hello())
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
    
        # render the menu
        self.window.config(menu=self.menubar)
        
        # execute
        self.window.mainloop()
        
    # hold for future functionality
    def hello(self):
        print ("hello!")
    
    # copy selected text
    def copy(self):
        print ('hey there')
    
    # cut selected text
    def cut(self):
        print ('bugger')
    
    # paste selected text
    def paste(self):
        print ('howdy')
        
    # delete selected text
    def delete(self):
        print('delete me')
          
    # close text editor
    def quit(self):
        if self.text_change():
            self.popupmsg(self.window.destroy)
        else:
            self.window.destroy() 
     
    # saves text to existing location if file exists - if file does not exist, then create file
    def save(self):
        data = self.text.get(1.0, 'end-1c')
        self.original = data
        if self.filename != 'Untitled':
            writer = open(self.file_ext(), 'w')
            writer.write(data)
            writer.close()         
        else:
            self.saveas()
    
    # saves text in editor to path designated by user in pop-up menu    
    def saveas(self):
        data = self.text.get(1.0, 'end-1c')
        self.original = data
        temp = self.filename
        self.filename = dialog.asksaveasfilename(parent=self.window, filetypes=[('Text', '*.txt')], title='Save as...')
        if self.filename == '':
            self.filename = temp
            self.window.title(self.filename + " - Andrea's Notepad")
        else:
            self.window.title(basename(self.file_ext()) + " - Andrea's Notepad")
            writer = open(self.file_ext(), 'w')
            writer.write(data)
            writer.close()
        
    # opens existing text document
    def open(self):
        temp = self.filename
        self.filename = dialog.askopenfilename(filetypes=[('Text', '*.txt')], title='Open')
        if self.filename == '':
            self.filename = temp
            self.window.title(self.filename + " - Andrea's Notepad")
        else: 
            data = open(self.filename, 'r+')
            text = data.read()
            self.original = text
            self.text.delete(1.0, 'end-1c')
            self.text.insert('1.0', text)
            self.window.title(basename(self.file_ext()) + " - Andrea's Notepad")
            
    # checks for changes to current text file prior to user opening an existing text document
    def open_save_check(self):
        if self.text_change():
            self.popupmsg(self.open)
        else:
            self.open()
       
    # checks for changes to current text file prior to user opening a new text document
    def new_save_check(self):
        if self.text_change():     
            self.popupmsg(self.new)         
        else:
            self.new()
            
    # handler function for missing extension for window title & file handling      
    def file_ext(self):
        if os.path.splitext(self.filename)[1] == '.txt':
            return self.filename
        else:
            return self.filename + '.txt'
    
    # custom save pop-up message box
    def popupmsg(self, comm):
        self.popup_window = tkinter.Toplevel(self.window)
        self.popup_window.title("Andrea's Notepad")
        self.popup_window.geometry('400x100')
        self.msg = tkinter.Label(self.popup_window, text="Do you wish to save changes to " + self.filename + "?")
        self.msg.pack(side = 'top', fill = 'both', expand = True)
        self.cancel_button = tkinter.Button(self.popup_window, text="Cancel", command=lambda: self.popup_window.destroy())
        self.cancel_button.pack(side='right', padx = 5, pady = 10)
        self.nosave_button = tkinter.Button(self.popup_window, text="Don't Save", command=lambda: mult_func(self.popup_window.destroy(), comm()))
        self.nosave_button.pack(side='right', padx = 5, pady = 10)
        self.save_button = tkinter.Button(self.popup_window, text="Save", command=lambda: mult_func(self.popup_window.destroy(), self.save(), comm()))
        self.save_button.pack(side = 'right', padx = 5, pady = 10)
        self.popup_window.grab_set()
    
    # clear all text from the text editor and start with blank document
    def new(self):
        self.text.delete(1.0, 'end-1c')
        self.filename = 'Untitled'
        self.window.title(self.filename + " - Andrea's Notepad")
    
    
    # detect that the text has been edited
    def text_change(self):
        data = self.text.get(1.0, 'end-1c')
        if self.filename == 'Untitled':
            if data == '':
                return False
            else:
                return True
        else:
            if self.original == data:
                return False
            else:
                return True
    
    
# multiple function handler
def mult_func(*args):
    for i in args:
        i
             
notepad = a_notepad()