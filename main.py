'''Project Graph creater'''
from Tkinter import *

class Test(Frame):
    
    counter = 0
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

        self.n_window = Button(self, text = "Create new window", command = self.create_window)
        self.n_window.grid(row = 8, column =2)
        
    def on_button(self):
        print self.data1.get()

    def create_window(self):
        self.counter += 1
        t = Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = Label(t, text = "This is window #%s" % self.counter)
        l.pack(side = "top", fill = "both", expand = True, padx=100\
               ,pady = 100)



def main():
    
    root = Tk()
    root.geometry("350x150+300+300")
    app = Test(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
