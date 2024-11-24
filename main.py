from tkinter import *
from PIL import Image ,ImageTk
from tkinter import messagebox
window = Tk()
window.config(bg="gold")
window.geometry("500x500")
upload = Image.open("app_img.jpg")
cash_tally = ImageTk.PhotoImage(upload)
label = Label (window, image =cash_tally)
label.pack()

welcome = Label(window, text="hey user welcome to the denominaton calculator" , bg= "gold")
welcome.pack()

def confirmation():
    messagebox.showinfo("Warning" ,"do you want to calculate the denomination count")
button = Button(window, text="lets get started", bg="purple", 
            command=confirmation)
button.pack()
window.mainloop()