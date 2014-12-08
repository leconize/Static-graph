'''Project Graph creater'''
from Tkinter import *

class App(Frame):
    
    count = 0
    data = []
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
        name, value = self.data_name.get(), self.value.get()
        self.data.append((name, value))
        print self.data

    def drawing_circle(self):
        '''
        prototype function made for create graph
        '''
        all_value = 0
        for name, value in self.data:
            all_value += float(value)    
        self.t = Toplevel(self)
        graph = Canvas(self.t, width = 600,height = 600, borderwidth=5, background='white')
        start = 0
        for i in xrange(self.count):
            extent = float(self.data[i][1])*360/all_value
            print start, extent
            graph.create_arc((10,10,152,152), outline = self.color[i], fill = self.color[i]\
                         , start = start, extent = extent)
            start += extent
        graph.pack()

    def draw_bar(self):
        '''
        Create bar graph from data
        '''
        self.bar = Toplevel(self)
        graph = Canvas(self.bar, width = 600, height= 600, borderwidth = 5, background = 'white')
        bar_width = 500/(self.count*2+1)
        x_1 = bar_width
        if max([float(self.data[i][1]) for i in xrange(self.count)]) > 500:
            scale = 500/max([float(self.data[i][1]) for i in xrange(self.count)])
        else:
            scale = 1
        for x in xrange(self.count):
            graph.create_rectangle(x_1, 550-float(self.data[x][1])*scale, x_1+bar_width, 550, fill = self.color[x])
            x_1 = x_1+bar_width+bar_width/2
        graph.pack()
    def initUI(self): # User Interface
        '''
        User interface function
        '''
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
        
        bar = Button(self, text = "Bar Graph",bg = "Darkolivegreen", fg = "Aliceblue", command = self.draw_bar)
        circle = Button(self, text = "Circle Graph", bg ="Darkolivegreen", fg = "Aquamarine",  command = self.drawing_circle)
        bar.grid(row = 6, column = 1)
        circle.grid(row = 6, column = 2)
        
        get_value = Button(self, text = "Get_data", bg = "Navy", fg = "Deepskyblue", command = self.on_button)
        get_value.grid(row = 7, column =1)

        
    

def main():
    root = Tk()
    root.geometry("400x200+300+300")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
