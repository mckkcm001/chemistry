# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 07:58:34 2016

@author: chris
"""

from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.unit_label = Label(frame, text="Unit")
        self.unit_label.pack(side=LEFT)
        self.unit_entry = Entry(frame,width=3)
        self.unit_entry.pack(side=LEFT)
        
        self.lesson_label = Label(frame, text="Lesson")
        self.lesson_label.pack(side=LEFT)
        self.lesson_entry = Entry(frame,width=3)
        self.lesson_entry.pack(side=LEFT)

        self.period_label = Label(frame, text="Period")
        self.period_label.pack(side=LEFT)
        self.period_entry = Entry(frame,width=3)
        self.period_entry.pack(side=LEFT)

        self.lesson_button = Button(frame, text="Make Lesson", command=self.make_lesson)
        self.lesson_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.quit_button.pack(side=LEFT)
    
    
    
    def make_lesson(self):
        print( "Make Lesson for Unit {0} Lesson {1} Period {2}".
                format(self.unit_entry.get(),self.lesson_entry.get(),self.period_entry.get()))

root = Tk()

app = App(root)

root.mainloop()
root.destroy()