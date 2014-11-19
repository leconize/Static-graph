'''Project Graph creater'''
from tkinter import *
window = Tk()
label = Label(window, text = "Graph creater")
bar = Button(window, text = "Bar Graph", fg = "Blue")#Button for create bar graph
circle = Button(window, text = "Circle Graph", fg = "Purple")#Button for create circle graph
label.pack()
bar.pack()
circle.pack()
