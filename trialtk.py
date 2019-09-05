from tkinter import *

window = Tk()
window.title('TKINTER')
window.geometry("750x200")

def close():
    window.destroy()
    exit()
tops = Frame(window, bd=0,  bg='YEllow', relief=RIDGE, pady=1)
tops.pack(side=BOTTOM)
Button(tops, text='exit', command = close, width=20).grid()
photo = PhotoImage(file='fav.png')
Label(tops, image=photo, bg='green').grid(row=1)
Label(tops, text='Enter the number ', fg='black', bg='red', font='none 12 bold').grid(row=2)
Entry(tops, width= 20, bg='white').grid(row=2, column=0)


window.mainloop()