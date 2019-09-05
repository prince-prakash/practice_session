from tkinter import *
import time
import random


window = Tk()
window.geometry("1250x750")
window.title("Food Billing")
window.iconbitmap('food.ico')
window.configure(bg='Yellow')

###################################Calculator_Definitions#############################

set_text = StringVar()
operator = ' '

def cal(number):
    global operator
    operator = operator + str(number)
    set_text.set(operator)


def cel():
    global operator
    operator =''
    set_text.set('')

def  eq():
    global operator
    sum = str(eval(operator))
    set_text.set(sum)
    operator =' '

######################################Receipt_Definitions###############################

receipt1 = StringVar()

def com_receipt():
    receipt.delete("1.0", END)
    x = random.randint(100000, 900000)
    ref = str(x)
    receipt1.set(ref)

    receipt.insert(END, 'Receipt Ref:\t\t\t'+receipt1.get())



######################################Definitions#######################################

frame1 = Frame(window, bd=20, pady=1, bg='green', relief=GROOVE)
frame1.pack(side=TOP)
Label(frame1, text='Food Billing System', bg='orange', font =('comic scan', 60, 'bold')).grid(row=0)

###############################Main_Frame###############################
frame2 = Frame(window, bd=10, pady=5, bg='Yellow', relief=RIDGE)
frame2.pack(side=LEFT)

#############################Total_Cost##################################       This Frame Should be coded always at First
frame5= Frame(frame2, pady=5, bg='Yellow')
frame5.pack(side=BOTTOM)
Label(frame5, text='Cost of Drinks', bg='Yellow', font=('Arial',15,'bold')).grid(row=0,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=0,column=1,sticky=E)
Label(frame5, text='Cost of Food', bg='Yellow', font=('Arial',15,'bold')).grid(row=1,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=1,column=1,sticky=E)
Label(frame5, text='Service Charge', bg='Yellow', font=('Arial',15,'bold')).grid(row=2,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=2,column=1,sticky=E)
Label(frame5, text='\tPaid Tax', bg='Yellow', font=('Arial',15,'bold')).grid(row=0,column=2,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=0,column=3,sticky=E)
Label(frame5, text='\tSubCost', bg='Yellow', font=('Arial',15,'bold')).grid(row=1,column=2,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=1,column=3,sticky=E)
Label(frame5, text='\tTotal Cost', bg='Yellow', font=('Arial',15,'bold')).grid(row=2,column=2,sticky=W)
Entry(frame5,width=30,bd=5,state=DISABLED).grid(row=2,column=3,sticky=E)

###############################Drinks###############################
frame3 = Frame(frame2, bd=10, pady=5, bg='Yellow', relief=RIDGE)
frame3.pack(side=LEFT)
Checkbutton(frame3, text='Sprite', font=('Arial',20,'italic'),bg='Yellow').grid(row=0,sticky=W)
Entry(frame3,width=10,bd=8,state=DISABLED).grid(row=0,column=1,sticky=E)
Checkbutton(frame3, text='Pepsi', font=('Arial',20,'italic'),bg='Yellow').grid(row=1,sticky=W)
Entry(frame3,width=10,bd=8,state=DISABLED).grid(row=1,column=1,sticky=E)
Checkbutton(frame3, text='Coke', font=('Arial',20,'italic'),bg='Yellow').grid(row=2,sticky=W)
Entry(frame3,width=10,bd=8,state=DISABLED).grid(row=2,column=1,sticky=E)
Checkbutton(frame3, text='Mojito', font=('Arial',20,'italic'),bg='Yellow').grid(row=3,sticky=W)
Entry(frame3,width=10,bd=8,state=DISABLED).grid(row=3,column=1,sticky=E)
Checkbutton(frame3, text='Cappacino', font=('Arial',20,'italic'),bg='Yellow').grid(row=4,sticky=W)
Entry(frame3,width=10,bd=8,state=DISABLED).grid(row=4,column=1,sticky=E)

#############################FOOD##################################
frame4= Frame(frame2, bd=10, pady=5, bg='Yellow', relief=RIDGE)
frame4.pack(side=RIGHT)
Checkbutton(frame4, text='HotDog', font=('Arial',20,'italic'),bg='Yellow').grid(row=0,sticky=W)
Entry(frame4,width=10,bd=8,state=DISABLED).grid(row=0,column=1,sticky=E)
Checkbutton(frame4, text='Pasta', font=('Arial',20,'italic'),bg='Yellow').grid(row=1,sticky=W)
Entry(frame4,width=10,bd=8,state=DISABLED).grid(row=1,column=1,sticky=E)
Checkbutton(frame4, text='Rice', font=('Arial',20,'italic'),bg='Yellow').grid(row=2,sticky=W)
Entry(frame4,width=10,bd=8,state=DISABLED).grid(row=2,column=1,sticky=E)
Checkbutton(frame4, text='Sandwich', font=('Arial',20,'italic'),bg='Yellow').grid(row=3,sticky=W)
Entry(frame4,width=10,bd=8,state=DISABLED).grid(row=3,column=1,sticky=E)
Checkbutton(frame4, text='French Fries', font=('Arial',20,'italic'),bg='Yellow').grid(row=4,sticky=W)
Entry(frame4,width=10,bd=8,state=DISABLED).grid(row=4,column=1,sticky=E)

############################Main_Frame######################################
frame6 = Frame(window, bd=10, pady=1, bg='Yellow', relief=RIDGE)
frame6.pack(side=RIGHT)

############################Frame3.1######################################
frame9 = Frame(frame6, bd=5, pady=1, bg='yellow',relief=RIDGE)
frame9.pack(side=TOP)

############################Calculator_1######################################
frame7 = Frame(frame9, pady=1, bg='Yellow')
frame7.pack(side=TOP)
cal_e = Entry(frame7,width=55, textvariable=set_text, justify=RIGHT).grid(row=0)

############################Calculator_1.1######################################
frame8 = Frame(frame9, bd=2, bg='Yellow', relief=RIDGE)
frame8.pack(side=BOTTOM)
button_1 = Button(frame8,text='1',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(1)).grid(row=0, column=0)
button_2 = Button(frame8,text='2',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(2)).grid(row=0, column=1)
button_3 = Button(frame8,text='3',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(3)).grid(row=0, column=2)
button_a = Button(frame8,text='+',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal('+')).grid(row=0, column=3)
button_4 = Button(frame8,text='4',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(4)).grid(row=1, column=0)
button_5 = Button(frame8,text='5',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(5)).grid(row=1, column=1)
button_6 = Button(frame8,text='6',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(6)).grid(row=1, column=2)
button_s = Button(frame8,text='-',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal('-')).grid(row=1, column=3)
button_7 = Button(frame8,text='7',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(7)).grid(row=2, column=0)
button_8 = Button(frame8,text='8',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(8)).grid(row=2, column=1)
button_9 = Button(frame8,text='9',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(9)).grid(row=2, column=2)
button_m = Button(frame8,text='*',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal('*')).grid(row=2, column=3)
button_c = Button(frame8,text='C',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=cel).grid(row=3, column=0)
button_0 = Button(frame8,text='0',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal(0)).grid(row=3, column=1)
button_e = Button(frame8,text='=',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=eq).grid(row=3, column=2)
button_d = Button(frame8,text='/',bd=5,bg='yellow',pady=5, padx=30, justify=CENTER, command=lambda: cal('/')).grid(row=3, column=3)

############################Receipt_buttons######################################
frame11 = Frame(frame6, pady=1, bg='yellow')
frame11.pack(side=BOTTOM)
Button(frame11,text='Total Cost',bd=5,bg='yellow',pady=10, padx=20, justify=CENTER).grid(row=0, column=0)
Button(frame11,text='Receipt',bd=5,bg='yellow',pady=10, padx=20, justify=CENTER, command=com_receipt).grid(row=0, column=1)
Button(frame11,text='Exit',bd=5,bg='yellow',pady=10, padx=20, justify=CENTER).grid(row=0, column=2)
Button(frame11,text='Reset',bd=5,bg='yellow',pady=10, padx=20, justify=CENTER).grid(row=0, column=3)

############################Receipt######################################
frame10 = Frame(frame6, pady=1, bg='yellow')
frame10.pack(side=BOTTOM)
receipt = Text(frame10, width=40, height=10, font=('arial', 12, 'bold')).grid(row=0,column= 0)

window.mainloop()