import tkinter as tk
from tkinter import *
expression=""
def press(num):
    global expression
    expression=expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression)) 
        equation.set(total)
        expression=""
    except:
        equation.set(total)
        expression

def clear():
    global expression
    expression=""
    equation.set("")

if __name__ == "__main__": 
    calc=tk.Tk()
    calc.geometry("400x300")
    calc.title("Calculator")
    calc.configure(background="orange")
    equation = StringVar()

    #label_result=tk.Entry(calc,text=" ")
    result_label=tk.Entry(calc,textvariable=equation)
    result_label.grid(columnspan=4,ipadx=60)
    button1=tk.Button(calc,text=1, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(1))
    button2=tk.Button(calc,text=2, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(2))
    button3=tk.Button(calc,text=3, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(3))
    button4=tk.Button(calc,text=4, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(4))
    button5=tk.Button(calc,text=5, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(5))
    button6=tk.Button(calc,text=6, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(6))
    button7=tk.Button(calc,text=7, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(7))
    button8=tk.Button(calc,text=8, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(8))
    button9=tk.Button(calc,text=9, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(9))
    button0=tk.Button(calc,text=0, height=1, width=7 ,    highlightcolor="white",   background="skyblue", command=lambda: press(0))

    button_rst=tk.Button(calc,text="Reset",height=1,width=7 ,background="skyblue")
    button_back=tk.Button(calc,text="Clear",height=1,width=7,background="skyblue",command=clear)
    button_sum=tk.Button(calc,text="+",height=1,width=7     ,background="skyblue", command=lambda: press("+"))
    button_sub=tk.Button(calc,text="-",height=1,width=7     ,background="skyblue", command=lambda: press("-"))
    button_mul=tk.Button(calc,text="*",height=1,width=7     ,background="skyblue", command=lambda: press("*"))
    button_div=tk.Button(calc,text="/",height=1,width=7     ,background="skyblue", command=lambda: press("/"))
    button_eq=tk.Button(calc,text="=" ,height=1,width=7     ,background="skyblue", command=equalpress)
    button_per=tk.Button(calc,text="%",height=1,width=7     ,background="skyblue", command=lambda: press("%")) 
    button_dec=tk.Button(calc,text=".",height=1,width=7     ,background="skyblue", command=lambda: press(".")) 
    button11=tk.Button(calc,text="",height=1,width=7,        background="skyblue",)
    # Widget layouts,height=3,width=3 
    #label_result.grid(row=0)
    button_rst.grid(row=1,column=0 )
    button_back.grid(row=1,column=1)
    button_per.grid(row=1, column=2)
    button_div.grid(row=1, column=3)
    button_sum.grid(row=3, column=3)
    button_sub.grid(row=4, column=3)
    button_mul.grid(row=5, column=3)
    button_eq.grid( row=6, column=3)
    button0.grid(row=6,column=1)
    button_dec.grid(row=6,column=2)
    button11.grid(row=6,column=0 )

    button1.grid(row=3,column=0)
    button2.grid(row=3,column=1)
    button3.grid(row=3,column=2)
    button4.grid(row=4,column=0)
    button5.grid(row=4,column=1)
    button6.grid(row=4,column=2)
    button7.grid(row=5,column=0)
    button8.grid(row=5,column=1)
    button9.grid(row=5,column=2)
    

    calc.mainloop()