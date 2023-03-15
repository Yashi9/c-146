# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:38:46 2023

@author: DELL
"""

from tkinter import *

root = Tk()

root.title("Fibonacci Series")
root.geometry("400x200")


enter = Entry(root)
label_series = Label(root, text = "Fibonacci Series :")
label_sum  = Label(root) 

def fibonacci() : 
    input = int(enter.get())
    sum = 0 
    sum_2 = 0 
    first_no = 0 
    sec_no = 1
    counter = 1
    while(counter <= input):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "Fibonmacci sum : " + str(sum_2)
        counter = counter + 1
        first_no = sec_no 
        sec_no = sum
        sum = first_no + sec_no  
        sum_2 = sum + sum_2 
        
btn = Button(root , text = "Show Series" , command =fibonacci , fg = "black" ,bg = "yellow" )

enter.pack()
btn.pack()
label_series.pack()
label_sum.pack()

root.mainloop()