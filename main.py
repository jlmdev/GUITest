from tkinter import *
# from tkinter import ttk
# from tkinter import messagebox
window = Tk()

btn = Button(window, text='This is a Button widget', fg='blue')
btn.place(x=80, y=100)

window.title('Hello Python')
window.geometry('300x200+10+20')
window.mainloop()


# def main():
#     pass
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     main()
