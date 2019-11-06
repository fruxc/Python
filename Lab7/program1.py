    
from tkinter import *

window = Tk()
window.geometry('1280x720')
window.title("Google")

label_0 = Label(window, text="Create your Google Account",width=23,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(window, text="First Name",width=23,font=("bold", 10))
label_1.place(x=1,y=130)

entry_1 = Entry(window)
entry_1.place(x=140,y=130)

label_2 = Label(window, text="Last Name",width=23,font=("bold", 10))
label_2.place(x=250,y=130)

entry_2 = Entry(window)
entry_2.place(x=400,y=130)

label_3 = Label(window, text="Your Email Address",width=23,font=("bold", 10))
label_3.place(x=25,y=180)

entry_3 = Entry(window)
entry_3.place(x=180,y=180)

label_4 = Label(window, text="You'll need to confirm this email belongs to you",width=50,font=("",8))
label_4.place(x=25,y=200)

Label_5 = Label(window, text="Enter Password", width=20, font=("bold",10))

Button(window, text='Submit',width=20,bg='lightgreen',fg='white').place(x=180,y=380)

window.mainloop()
