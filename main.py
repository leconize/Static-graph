'''Project Graph creater'''
from Tkinter import *
from PIL import Image,ImageTk
import tkMessageBox
import ttk

class App(Frame):
    
    data = []
    limit = 0
    def __init__(self, parent):
        Frame.__init__(self, parent)
         
        self.parent = parent
        
        self.initUI()#call UI

    def get_data(self):
        '''
        get value and value's name save them in to dic for calculate function
        '''
        name, value = self.data_name.get(), self.value.get()
        if name =="":
            tkMessageBox.showerror('Error', 'Please input the name')
            return
        try:
            int(value)
        except:
            tkMessageBox.showerror('Error', 'the value can not be word')
            return
        if self.limit == 10:
            tkMessageBox.showerror('Error', 'Data limit at 10')
        self.data.append((name, int(value)))
        self.limit += 1
        self.table.insert('', 'end', values = [name, int(value)])

    def remove(self):
        xxx = self.table.focus()
        self.data.remove(self.data[self.table.index(xxx)])
        self.table.delete(xxx)
    def reset(self):
        map(self.table.delete, self.table.get_children())
        self.data = []
#-----------------------------------------------------------------------------------------------------------------------

    def initUI(self): # User Interface
        '''
        Main window of the program insert name and value to create the graph
        '''
        self.parent.title("Graph-Creater")
        self.pack(fill=BOTH, expand=1)

        get_frame = Frame(self, relief=RAISED, borderwidth=1, background = 'khaki')
        get_frame.pack(side = LEFT, fill='both', expand = True, padx = 5, pady = 5)
        label = Label(self, text = "Graph Creater", background = "khaki")
        label.grid(row = 0, column = 1, in_=get_frame)

        Label(self, text = "Name", background = 'khaki').grid(row = 1, in_=get_frame)
        Label(self, text = "Value", background = 'khaki').grid(row = 2,column = 0,in_=get_frame)
        
        self.data_name = Entry(self)
        self.data_name.grid(row = 1, column = 1, in_=get_frame)

        self.value = Entry(self)
        self.value.grid(row = 2, column = 1, in_=get_frame)

        get_value = Button(self, text = "Get_data", bg = "Navy", fg = "Deepskyblue", command = self.get_data)
        get_value.grid(row = 6, column =0, in_=get_frame, padx = 6)
        reset_value = Button(self, text = "Reset_value", bg = "Navy", fg = "firebrick1",command = self.reset)
        reset_value.grid(row = 6, column =1, in_=get_frame)
        remove_value = Button(self, text = "Remove_value", bg = "Navy", fg = "Darkorange", command = self.remove)
        remove_value.grid(row = 6, column = 2, in_= get_frame, pady = 10, padx = 6)
        self.grid_rowconfigure(6, weight = 1, pad = 1)
        
        bar = Button(self, text = "Bar Graph",bg = "dark slate gray", fg = "Aquamarine", command = lambda x = 1 : Graph(self, self.data, x))
        circle = Button(self, text = "Circle Graph", bg ="dark slate gray", fg = "Aquamarine",  command = lambda x = 0 : Graph(self, self.data, x))
        bar.grid(row = 8, column = 0, in_=get_frame, padx = 10)
        circle.grid(row = 8, column = 1, in_=get_frame)

        frame = ttk.Frame(self, relief=RAISED, borderwidth=10)
        frame.pack(side =BOTTOM)

        self.table = ttk.Treeview(self, columns=['Name', 'Value'], show = "headings")
        self.table.grid(row = 0, column=0, in_=frame)

        for column in ['Name', 'Value']:
            self.table.heading(column, text=column.title())
        
#---------------------------------------------------------------------------------------------------------------------------------------
class Graph:
    '''
    This Class will draw a bargraph and circlegraph from the data
    '''
    color = ["Tomato", "Chartreuse", "Darkturquoise", "Deeppink", "Gold", "Maroon","DarkBlue", "DarkKhaki", "SandyBrown", "LightSalmon", "IndianRed"]
    
    def __init__(self, tk, data, mode):
        self.graph = Toplevel(tk)
        self.data = data
        self.count = len(data)
        self.value = [i[1] for i in self.data]
        if mode == 1:
            self.draw_bar()
        else:
            self.draw_circle()
        self.namebox()
        self.cal()
    def draw_circle(self):
        '''
        Draw the Circle graph from the data
        '''
        all_value = 0
        for name, value in self.data:
            all_value += float(value)    
        graph = Canvas(self.graph, width = 600,height = 600, borderwidth=5, background='white')
        start = 0
        for i in xrange(self.count):
            extent = float(self.data[i][1])*360/all_value
            print start, extent
            graph.create_arc((150,150,450,450), outline = self.color[i], fill = self.color[i]\
                         , start = start, extent = extent)
            start += extent
        graph.pack(side= LEFT)
        #Button(self.t, text = "Exit", command = self.t.destroy).pack()

    def draw_bar(self):
        '''
        Draw the Bar graph from the data
        '''
        graph = Canvas(self.graph, width = 600, height= 600, borderwidth = 5, background = 'white')
        size = 575
        bar_width = 500/(self.count*3+1)
        x_1 = bar_width+50
        temp = 0
        level = 10
        while max(self.value) > temp:
            for i in [1, 2 ,5]:
                temp = level*i
                if temp >= max(self.value):
                    break
            level *= 10
        scale = 500.0/temp
        for x in xrange(self.count):
            graph.create_rectangle(x_1,575-float(self.data[x][1])*scale, x_1+bar_width*2, 575, fill = self.color[x])
            x_1 = x_1+bar_width*3
        #y-axis
        graph.create_line(50,25,50,575)
        #y-axis arrow
        graph.create_line(50,25,60,35)
        graph.create_line(50,25,40,35)
        for i in xrange(5):
            mark = (temp-(temp/5)*i)*scale
            graph.create_text(25,575-mark, text=str(temp-(temp/5)*i))
            graph.create_line(45,575-mark,55,575-mark)
        #x-axis
        graph.create_line(50,575,550,575)
        #x-axis arrow
        graph.create_line(550,575,540,585)
        graph.create_line(550,575,540,565)
        graph.pack(side = LEFT)
        #self.cal(self.graph)
#----------------------------------------------------------------------------------------------------------------------- 
    def namebox(self):
        '''
        Show the name and value of the Data
        '''
        box = Canvas(self.graph, width = 200, height = 300, background = 'white')
        name_list = [i[0] for i in self.data]
        temp = [10,30]
        for i in xrange(self.count):
            box.create_rectangle(10,temp[0],30,temp[1], fill = self.color[i])
            box.create_text(40+(len(name_list[i])*2.5),(temp[0]+temp[1])/2, text = name_list[i])
            temp = map(lambda x : x+30, temp)  
        frame = ttk.Frame(self.graph, relief=RAISED, borderwidth=10)
        frame.pack(side = LEFT, fill = Y, expand = 1)
        box.pack(side =TOP, anchor = NE)
    
    def cal(self):
        '''
        calcurate  the Statistic value that include max min average and medium
        '''
        lis = [self.data[i][1] for i in xrange(self.count)]
        maximum, minimum, average = max(lis), min(lis), sum(lis)/len(lis)
        lis.sort()
        if len(lis)%2 == 0:
            medium = (lis[len(lis)/2]+lis[len(lis)/2-1])/2
        else:
            medium = lis[len(lis)/2]
        ans = Listbox(self.graph)
        ans.insert(END, "Maximum" +" "+" = " + str(maximum))
        ans.insert(END, "Minimum" +" "+" = " + str(minimum))
        ans.insert(END, "Average" + " "+ " = " + str(average))
        ans.insert(END, "Medium" + " "+ " = " + str(medium))
        Label(self.graph, text = 'Statistic value').pack(side=TOP, anchor = N)
        ans.pack(side = TOP, fill = 'both' ,expand= 1)
#-----------------------------------------------------------------------------------------------------------------        
def main():
    '''
    Call the main window
    '''
    root = Tk()
    img = Image.open("icon2.jpg")
    tkpi = ImageTk.PhotoImage(img)
    label_image = Label(root, image=tkpi)
    label_image.pack(side = TOP, padx = 5, pady = 5)
    root.resizable(width=FALSE, height=FALSE)
    root.configure(background = 'white')
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
