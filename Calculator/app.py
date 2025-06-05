import tkinter as tk

calculation = ""

def addToSpace(symbol):
    global calculation
    calculation+=str(symbol)
    textResult.delete(1.0,"end")
    textResult.insert(1.0,calculation)

def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        
        textResult.delete(1.0,"end")
        textResult.insert(1.0,calculation)
    except:
        clear()
        textResult.insert(1.0,"Error")
        
def clear():
    global calculation
    calculation=""
    textResult.delete(1.0,"end")

def clearOne():
    global calculation
    calculation = calculation[:-1]  # remove last character
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)


root= tk.Tk()
root.geometry("350x250")

textResult=tk.Text(root,height=2,width=19,font=("Arial",24))
textResult.grid(columnspan=5)

btn_1=tk.Button(root,text="1",command=lambda:addToSpace(1),width=5,font=("Arial",14)) #lambda allow to pass params
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",command=lambda:addToSpace(2),width=5,font=("Arial",14)) #lambda allow to pass params
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",command=lambda:addToSpace(3),width=5,font=("Arial",14)) #lambda allow to pass params
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",command=lambda:addToSpace(4),width=5,font=("Arial",14)) #lambda allow to pass params
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",command=lambda:addToSpace(5),width=5,font=("Arial",14)) #lambda allow to pass params
btn_5.grid(row=3,column=2)

btn6=tk.Button(root,text="6",command=lambda:addToSpace(6),width=5,font=("Arial",14)) #lambda allow to pass params
btn6.grid(row=3,column=3)

btn7=tk.Button(root,text="7",command=lambda:addToSpace(7),width=5,font=("Arial",14)) #lambda allow to pass params
btn7.grid(row=4,column=1)


btn8=tk.Button(root,text="8",command=lambda:addToSpace(8),width=5,font=("Arial",14)) #lambda allow to pass params
btn8.grid(row=4,column=2)

btn9=tk.Button(root,text="9",command=lambda:addToSpace(9),width=5,font=("Arial",14)) #lambda allow to pass params
btn9.grid(row=4,column=3)

btn0=tk.Button(root,text="0",command=lambda:addToSpace(0),width=5,font=("Arial",14)) #lambda allow to pass params
btn0.grid(row=5,column=2)

btnOpen=tk.Button(root,text="(",command=lambda:addToSpace("("),width=5,font=("Arial",14)) #lambda allow to pass params
btnOpen.grid(row=5,column=1)

btnClose=tk.Button(root,text=")",command=lambda:addToSpace(")"),width=5,font=("Arial",14)) #lambda allow to pass params
btnClose.grid(row=5,column=3)

btnplus=tk.Button(root,text="+",command=lambda:addToSpace("+"),width=5,font=("Arial",14)) #lambda allow to pass params
btnplus.grid(row=2,column=4)


btnminus=tk.Button(root,text="-",command=lambda:addToSpace("-"),width=5,font=("Arial",14)) #lambda allow to pass params
btnminus.grid(row=3,column=4)


btnmul=tk.Button(root,text="X",command=lambda:addToSpace("*"),width=5,font=("Arial",14)) #lambda allow to pass params
btnmul.grid(row=4,column=4)

btndiv=tk.Button(root,text="/",command=lambda:addToSpace("/"),width=5,font=("Arial",14)) #lambda allow to pass params
btndiv.grid(row=5,column=4)

btnclear=tk.Button(root,text="C",command=clear,width=5,font=("Arial",14)) #lambda allow to pass params
btnclear.grid(row=6,column=1)

btndel=tk.Button(root,text="del",command=clearOne,width=5,font=("Arial",14)) #lambda allow to pass params
btndel.grid(row=6,column=2)

btnequal=tk.Button(root,text="=",command=evaluate,width=13,font=("Arial",14)) #lambda allow to pass params
btnequal.grid(row=6,column=3,columnspan=11)

root.mainloop()
