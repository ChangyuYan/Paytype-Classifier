from tkinter import *

DEFAULT_FONT = ("courier", 20)
CIPHER_TYPES = {'RSA' }
DEFAULT_CIPHER = ('RSA')
PARA_HEIGHT = 4
TEXT_HEIGHT = 4


class PayTypeClassifier:
    
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x800")
        self.master.title("Pay Type Classifier")
        
        
        ####### Choose File ####### 
        instruction1 = Label(master = master, font=DEFAULT_FONT,
                           text="Choose File: ")
        instruction1.grid(row=0, sticky="W")
    
        
    
    def say_hi(self, value):
        print("Hi!")
        print(value)
        
        
    def run(self):
        self.master.mainloop()

my_gui = PayTypeClassifier(Tk())
my_gui.run()


