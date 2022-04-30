from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
window = Tk()


def button1_clicked():
    label1.config(text='Clicked!!')


button1 = Button(window, text='Click Me!', fg='blue', command=button1_clicked)
button1.place(x=80, y=100)

label1 = Label(window, text='This is a Label widget', fg='red', font=('Helvetica', 16))
label1.place(x=60, y=50)

text_field = Entry(window, fg='yellow', bd=5)
text_field.place(x=80, y=150)

window.title('Hello Python')
window.geometry('300x200+10+20')
window.mainloop()
