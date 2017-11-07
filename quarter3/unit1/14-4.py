import tkinter

class Slideshow:
    def __init__(self):
        self.count = 0
        root = tkinter.Tk()
        root.geometry("1200x300")
        label1 = tkinter.Label(root,wraplength = 1150, justify='left')
        label2 = tkinter.Label(root)
        label1.pack()
        label2.pack(side = "bottom")
        self.label1 = label1
        self.label2 = label2
        self.root = root
        self.delays = [5,  4,4,5,5  ,5,   2]
        self.questions = [
'Directions \n\
Start a text document and Save As per#.14-4.joe666666.bob777777.sue888888 \n\
In the document, type this header: \n\
Name 1              Date \n\
Name 2 \n\
Name 3 \n\n\
14-4',

'Name of writer \n\
1.\tWhy can liters be used for reaction coeeficient units with gases as \n\
\twell as moles and molecules?',

'Name of writer \n\
2.\tDetermine the volume of hydrogen gas needed to react completely with \n\
\t5.00 L of oxygen gas to form water.',

'Name of writer \n\
3.\tDetermine how many moles of water vapor will be produced at 1.00 atm and 200°C \n\
\tby the complete combustion of 10.5 L of methane gas (CH4).',

'Name of writer \n\
4.\tSolid potassium metal will react with Cl2 gas to form ionic potassium chloride.\n\
\tHow many liters of Cl2 gas are needed to completely react with 0.204 g of potassium at STP?',

'Name of writer \n\
5.\tWhen calcium carbonate is heated, it decomposes to form solid calcium oxide and carbon dioxide gas.  \n\
\tHow many liters of carbon dioxide will be produced at STP if 2.38 kg of calcium carbonate reacts completely?',

'Save, Close, Copy, Paste into turnin folder, logout, or shutdown']
        self.question = self.questions.pop(0)
        self.delay = 60*self.delays.pop(0)
        root.after(1, self.showQuestion)
        root.mainloop()

    def showQuestion(self):       
        self.label1.configure(text=self.question,font=("Helvetica", 16))
        self.label2.configure(text=str(self.count)+'/'+str(self.delay),font=("Helvetica", 24))
        if self.count >= self.delay:
            if len(self.questions) > 0:
                self.count = 0
                self.question = self.questions.pop(0)
                self.delay = 60*self.delays.pop(0)
                self.root.after(1000, self.showQuestion)
            else:
                self.root.after(1000, self.root.quit)
        else:
            self.count += 1
            self.root.after(1000, self.showQuestion)
            
    def quit(self):
        self.root.quit()

if __name__ == "__main__":
    app=Slideshow()
