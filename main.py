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
        Label(self, text = "Data2").grid(row = 2)
        Label(self, text = "Data3").grid(row = 3)
        Label(self, text = "Data4").grid(row = 4)
        Label(self, text = "Data5").grid(row = 5)
        data1 = Entry(self)
        data2 = Entry(self)
        data3 = Entry(self)
        data4 = Entry(self)
        data5 = Entry(self)
        data1.grid(row = 1, column = 1)
        data2.grid(row = 2, column = 1)
        data3.grid(row = 3, column = 1)
        data4.grid(row = 4, column = 1)
        data5.grid(row = 5, column = 1)
        bar = Button(self, text = "Bar Graph", fg = "Blue")#Button for create bar graph
        circle = Button(self, text = "Circle Graph", fg = "Purple")#Button for create circle graph
        bar.grid(row = 6, column = 1)
        circle.grid(row = 6, column = 2)


def main():
    
    root = Tk()
    root.geometry("250x150+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
