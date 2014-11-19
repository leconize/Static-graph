'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
         
        self.parent = parent
        
        self.initUI()#call UI

    def initUI(self): # User Interface 
      
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        label = Label(self, text = "Graph creater")
        bar = Button(self, text = "Bar Graph", fg = "Blue")
        circle = Button(self, text = "Circle Graph", fg = "Purple")
        label.pack()
        bar.pack()
        circle.pack()
        
def main():
    
    root = Tk()
    root.geometry("250x150+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
