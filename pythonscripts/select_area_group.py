#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter as tk
import pkgutil
import importlib
import types
import scraper
import group_generator as gg
import random
import math
               
class simpleapp_tk(tk.Tk):
    def __init__(self,master):
        tk.Tk.__init__(self,master)
        self.master = master
        self.grid()
        self.initialize()
        self.assess=[]      
        self.skill_rows = 0
        
    def initialize(self):
        self.display_units()
        self.display_assess()
        self.display_groupsize()
        self.display_areas()    
        self.display_buttons()
        
    def sel_unit(self):
        selection = "You selected " + str(self.v_unit.get())
        self.label_unit.config(text = selection)
    def sel_ass(self):
        selection = "You selected " + str(self.v_ass.get())
        self.label_ass.config(text = selection)
    def sel_gs(self):
        selection = "You selected " + str(self.v_gs.get())
        self.label_gs.config(text = selection)
    def sel_area(self):
        selection = "You selected " + str(self.v_area.get())
        self.label_area.config(text = selection)
        self.display_skills(self.v_area.get())
    def sel_skill(self):
        selection = "You selected " + str(self.v_skill.get())
        self.label_skill.config(text = selection)
        
    def make_assess(self):   
        teachers=[['chris.mckinnon','pass42015f',['1','2','5']],
                  ['elizabeth.cummings','scooter5',['1','2','5','6']],
                  ['o.belarma','dunlay5355',['1','3','4','5','6']],
                  ['arron.white','worms',['2','3']],
                  ]
        for t in teachers:
            for p in t[2]:
                roster = scraper.get_roster(t[0],t[1],p)                           
                print( "Make assessment for {} Period {} Unit {} Lesson {}".format(t[0],p,self.v_unit.get(),self.v_ass.get()))
                gg.make_practice(t[0],roster,p,self.v_gs.get(),self.v_unit.get(),self.v_ass.get(),self.assess)

        print 'done'
        self.assess=[]
        
    def add_problem(self):
        print( "Add problem {} from area {} for Unit {} Lesson {}".format(self.v_skill.get(),self.v_area.get(),self.v_unit.get(),self.v_ass.get()))
        self.assess.append((self.v_area.get(),self.v_skill.get())) 
        print self.assess
        
    def display_units(self):
        self.UNITS = [
        ("Unit 1", "Unit1"),
        ("Unit 2", "Unit2"),
        ("Unit 3", "Unit3"),
        ("Unit 4", "Unit4"),
        ("Unit 5", "Unit5"),
        ("Unit 6", "Unit6"),
        ("Unit 7", "Unit7"),
        ("Unit 8", "Unit8"),
        ]
        self.v_unit = tk.StringVar()
        self.v_unit.set("Unit1")
        r=0
        for text, mode in self.UNITS:
            b = tk.Radiobutton(self.master, text=text, variable=self.v_unit, value=mode, command=self.sel_unit)
            b.grid(row=r, column=0)
            r+=1
        self.label_unit = tk.Label(self.master)  
        self.label_unit.grid(row=r, column=0)
        
    def display_assess(self):
        self.ASSESS = [
        ("Group 1", "Group1"),
        ("Group 2", "Group2"),
        ("Group 3", "Group3"),
        ("Group 4", "Group4"),
        ]
        self.v_ass = tk.StringVar()
        self.v_ass.set("Group1")
        r=0
        for text, mode in self.ASSESS:
            b = tk.Radiobutton(self.master, text=text, variable=self.v_ass, value=mode, command=self.sel_ass)
            b.grid(row=r, column=1)
            r+=1
        self.label_ass = tk.Label(self.master)  
        self.label_ass.grid(row=r, column=1)
        
    def display_groupsize(self):
        self.GROUPS = [
        ("Groups of 2", "2"),
        ("Groups of 3", "3"),
        ("Groups of 4", "4"),
        ("Groups of 5", "5"),
        ("Groups of 6", "6"),
        ]
        self.v_gs = tk.StringVar()
        self.v_gs.set("2")
        r=0
        for text, mode in self.GROUPS:
            b = tk.Radiobutton(self.master, text=text, variable=self.v_gs, value=mode, command=self.sel_gs)
            b.grid(row=r, column=2)
            r+=1
        self.label_gs = tk.Label(self.master)  
        self.label_gs.grid(row=r, column=2)
        
    def display_areas(self):
        self.AREAS = [(name,name) for _, name, _ in pkgutil.iter_modules(['discussion'])]  
        self.v_area = tk.StringVar()
        self.v_area.set(self.AREAS[0][0])
        r=0
        for text, mode in self.AREAS:
            b = tk.Radiobutton(self.master, text=text, variable=self.v_area, value=mode, command=self.sel_area)
            b.grid(row=r, column=3)
            r+=1
        self.label_area = tk.Label(self.master)  
        self.label_area.grid(row=r, column=3)
                
    def display_skills(self,area):    
        if self.skill_rows > 0:
            for b in self.skill_button:
                b.grid_remove()
            self.label_skill.config(text = "")    
        mod = importlib.import_module('discussion.'+area)
        SKILLS = [(k,k) for k in mod.__dict__  if type(mod.__dict__[k]) == types.ClassType]
            
        self.v_skill = tk.StringVar()
        self.v_skill.set(SKILLS[0][0])
        self.skill_rows=0
        self.skill_button=[]
        for text, mode in SKILLS:
            self.skill_button.append(tk.Radiobutton(self.master, text=text, variable=self.v_skill, value=mode, command=self.sel_skill))
            self.skill_button[-1].grid(row=self.skill_rows, column=4)
            self.skill_rows +=1
        self.label_skill = tk.Label(self.master)  
        self.label_skill.grid(row=self.skill_rows, column=3)
    
    def display_buttons(self):
        self.problem_button = tk.Button(self.master, text="Add Problem", command=self.add_problem)
        self.problem_button.grid(row=1, column=5)
        
        self.quiz_button = tk.Button(self.master, text="Make Assessment", command=self.make_assess)
        self.quiz_button.grid(row=2, column=5)
        
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()