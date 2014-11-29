'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    count = 0
    data = {}
    color = ["Tomato", "Chartreuse", "Darkturquoise", "Deeppink", "Gold"]
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
         
        self.parent = parent
        
        self.initUI()#call UI

    def on_button(self):
        '''
        get value and value's name save them in to dic for calculate function
        '''
        self.count += 1
        self.data[self.data_name.get()] = self.value.get()
        print self.data

    def create_window(self):
        '''
        prototype function made for create graph
        '''
        self.t = Toplevel(self)
        graph = Canvas(self.t, width = 600,height = 600, borderwidth=5, background='white')
        graph.create_arc((10,10,152,152), outline = "#FAF402", fill = "#FAF402"\
                         , start = 100, extent = 100)
        graph.pack()

    def initUI(self): # User Interface
      
        self.parent.title("Graph-Creater")
        self.pack(fill=BOTH, expand=1)
        
        label = Label(self, text = "Graph Creater")
        label.grid(row = 0, column = 1)

        Label(self, text = "Name").grid(row = 1)
        Label(self, text = "Value").grid(row = 1,column = 2)

        self.data_name = StringVar()
        self.data_name = Entry(self)
        self.data_name.grid(row = 1, column = 1)

        self.value = DoubleVar()
        self.value = Entry(self)
        self.value.grid(row = 1, column = 3)
        
        bar = Button(self, text = "Bar Graph",bg = "Darkolivegreen", fg = "Aliceblue")
        circle = Button(self, text = "Circle Graph", bg ="Darkolivegreen", fg = "Aquamarine",  command = self.create_window)
        bar.grid(row = 6, column = 1)
        circle.grid(row = 6, column = 2)
        
        test = Button(self, text = "Get_data", bg = "Navy", fg = "Deepskyblue", command = self.on_button)
        test.grid(row = 7, column =1)


def main():
    
    root = Tk()
    root.geometry("400x200+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
