'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    count = 0
    data = {}
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
         
        self.parent = parent
        
        self.initUI()#call UI


    def initUI(self): # User Interface 
      
        self.parent.title("Graph-Creater")
        self.pack(fill=BOTH, expand=1)
        
        label = Label(self, text = "Graph Creater")
        label.grid(row = 0, column = 1)
<<<<<<< HEAD
        '''name of input'''
        Label(self, text = "Data-name").grid(row = 1, column = 0)
        Label(self, text = "Data-name").grid(row = 2, column = 0)
        Label(self, text = "Data-name").grid(row = 3, column = 0)
        Label(self, text = "Data-name").grid(row = 4, column = 0)
        Label(self, text = "Data-name").grid(row = 5, column = 0)
        '''value of data'''
        Label(self, text = "Value").grid(row = 1, column = 2)
        Label(self, text = "Value").grid(row = 2, column = 2)
        Label(self, text = "Value").grid(row = 3, column = 2)
        Label(self, text = "Value").grid(row = 4, column = 2)
        Label(self, text = "Value").grid(row = 5, column = 2)
        data1 = Entry(self)
        data2 = Entry(self)
        data3 = Entry(self)
        data4 = Entry(self)
        data5 = Entry(self)
        showname1 = Entry(self)
        showname2 = Entry(self)
        showname3 = Entry(self)
        showname4 = Entry(self)
        showname5 = Entry(self)
        data1.grid(row = 1, column = 1)
        data2.grid(row = 2, column = 1)
        data3.grid(row = 3, column = 1)
        data4.grid(row = 4, column = 1)
        data5.grid(row = 5, column = 1)
        showname1.grid(row = 1, column = 4)
        showname2.grid(row = 2, column = 4)
        showname3.grid(row = 3, column = 4)
        showname4.grid(row = 4, column = 4)
        showname5.grid(row = 5, column = 4)
        bar = Button(self, text = "Bar Graph", fg = "Blue")#Button for create bar graph
        circle = Button(self, text = "Circle Graph", fg = "Purple")#Button for create circle graph
        bar.grid(row = 6, column = 4)
        circle.grid(row = 6, column = 1)
        paper = Canvas(self, width = 500, height = 250)
        paper.pack()
        def circle(x, y):
            paper.create_oval(x, x, y, y)
def main():
    
    root = Tk()
    root.geometry("350x150+300+300")
=======
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
        
    def on_button(self):
        self.count += 1
        self.data[self.data_name.get()] = self.value.get()
        print self.data

    def create_window(self):
        self.t = Toplevel(self)
        graph = Canvas(self.t, width = 600,height = 600, borderwidth=5,\
                       background='white')
        graph.pack()

def main():
    
    root = Tk()
    root.geometry("400x200+300+300")
>>>>>>> Test
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
