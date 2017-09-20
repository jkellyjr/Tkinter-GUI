#!/usr/bin/python

import Tkinter


class IntroApp_TK(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.textLabelVariable = Tkinter.StringVar()
        textLabel = Tkinter.Label(self, textvariable = self.textLabelVariable, anchor = 'w',  fg = 'green', bg = 'blue')
        textLabel.grid(column = 0, row = 0, columnspan = 5, sticky = 'ew')
        self.textLabelVariable.set('Please enter your message below:')

        self.msgEntryVariable = Tkinter.StringVar()
        self.msgEntry = Tkinter.Entry(self, textvariable = self.msgEntryVariable)
        self.msgEntry.grid(column = 0, row = 1, columnspan = 3, sticky = 'ew')
        self.msgEntry.bind("<Return>", self.onPressEnter)

        button = Tkinter.Button(self, text = "Send", command = self.onButtonClick)
        button.grid(column = 4, row = 1)

        self.targetLabelVariable = Tkinter.StringVar()
        targetLabel = Tkinter.Label(self, textvariable = self.targetLabelVariable, anchor = 'w', fg = 'black', bg = 'green')
        targetLabel.grid(column = 0, row = 2, columnspan = 5, sticky = 'ew')

        self.grid_columnconfigure(0, weight = 1)
        self.resizable(True, False)
        # self.update()
        # self.geometry(self.geometry())
        self.msgEntry.focus_set()
        self.msgEntry.selection_range(0, Tkinter.END)


    def onPressEnter(self, event):
        self.targetLabelVariable.set('Are you sure you want to send: '+ self.msgEntryVariable.get())
        self.msgEntryVariable.set('')
        self.msgEntry.focus_set()
        self.msgEntry.selection_range(0, Tkinter.END)

    def onButtonClick(self):
        self.targetLabelVariable.set('Are you sure you want to send: '+ self.msgEntryVariable.get())
        self.msgEntryVariable.set('')
        self.msgEntry.focus_set()
        self.msgEntry.selection_range(0, Tkinter.END)


if __name__ == "__main__":
    app = IntroApp_TK(None)
    app.title('Coo Coo Cachu Its All For The Big Blue')
    app.mainloop()
