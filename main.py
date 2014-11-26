'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    count = 0
    data = {}
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
         
        self.parent = parent
        
        self.initUI()#call UI

    def on_button(self):
        self.count += 1
        self.data[self.data_name.get()] = self.value.get()
        print self.data

    def create_window(self):
        self.t = Toplevel(self)
        graph = Canvas(self.t, width = 600,height = 600, borderwidth=5,\
                       background='white')
        graph.pack()

    def initUI(self): # User Interface 
      
        self.parent.title("Graph-Creater")
        self.pack(fill=BOTH, expand=1)
        
        label = Label(self, text = "Graph Creater")
        label.grid(row = 0, column = 1)

        Label(self, text = "Name").grid(row = 1)
        Label(self, text = "Value").grid(row = 1,column = 2)
        
        self.data_name = Entry(self)
        self.data_name.grid(row = 1, column = 1)

        self.value = Entry(self)
        self.value.grid(row = 1, column = 3)
        
        bar = Button(self, text = "Bar Graph", fg = "Blue")
        circle = Button(self, text = "Circle Graph", fg = "Purple")
        bar.grid(row = 6, column = 1)
        circle.grid(row = 6, column = 2)
        
        test = Button(self, text = "Get_data", command=self.on_button)
        test.grid(row = 7, column =1)

        self.n_window = Button(self, text = "Drawing Canvas", command = self.create_window)
        self.n_window.grid(row = 8, column =2)


def main():
    
    root = Tk()
    root.geometry("400x200+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
