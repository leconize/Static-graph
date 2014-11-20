'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    def __init__(self, parent):
        Frame.__init__(self, parent,)
         
        self.parent = parent
        
        self.initUI()#call UI


    def initUI(self): # User Interface 
      
        self.parent.title("Simple")
        self.pack(fill=BOTH, expand=1)
        
        label = Label(self, text = "Graph Creater")
        label.grid(row = 0, column = 1)
        Label(self, text = "Data1").grid(row = 1)
        
        self.data1 = Entry(self)
        self.data1.grid(row = 1, column = 1)
        
        bar = Button(self, text = "Bar Graph", fg = "Blue")#Button for create bar graph
        circle = Button(self, text = "Circle Graph", fg = "Purple")#Button for create circle graph
        bar.grid(row = 6, column = 1)
        circle.grid(row = 6, column = 2)
        
        test = Button(self, text = "Testing", command=self.on_button)
        test.grid(row = 7, column =1)

        
    def on_button(self):
        print self.data1.get()


def main():
    
    root = Tk()
    root.geometry("250x150+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
