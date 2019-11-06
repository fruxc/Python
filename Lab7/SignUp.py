from tkinter import *
#from tkinter.ttk import Style,Notebook
from PIL import Image, ImageTk




window=Tk()
window.title(" Create your Google Account ")
window.geometry("700x500")
window.configure(background="white")

#Contents of Signup tab
## Google logo
img1=ImageTk.PhotoImage(Image.open("google.png"))
imgGoogle=Label(window,image=img1)
imgGoogle.place(x=30,y=0)

## Google Sheild logo
img2=ImageTk.PhotoImage(Image.open("signupshield.png"))
imgGoogleSheild=Label(window,image=img2)
imgGoogleSheild.place(x=350,y=100)

## First Name Area
lblFirstName=Label(window,text="First Name",background="white")
lblFirstName.place(x=50,y=100)
edtFirstName=Entry(window)
edtFirstName.place(x=50,y=125)


## Last Name Area
lblLastname=Label(window,text="Last Name",background="white")
lblLastname.place(x=200,y=100)
edtULastname=Entry(window)
edtULastname.place(x=200,y=125)


## Username Area
lblUsername=Label(window,text="Username",background="white")
lblUsername.place(x=50,y=200)
edtUsername=Entry(window)
edtUsername.place(x=50,y=225)
lblExtensionUsername=Label(window,text="@gmail.com",background="white")
lblExtensionUsername.place(x=180,y=225)


## Password Area
lblPassword=Label(window,text="Password",background="white")
lblPassword.place(x=50,y=300)
edtPassword=Entry(window,show="*")
edtPassword.place(x=50,y=325)

## Confirm Password Area
lblConfirmPassword=Label(window,text="Confirm Password",background="white")
lblConfirmPassword.place(x=200,y=300)
edtConfirmPassword=Entry(window,show="*")
edtConfirmPassword.place(x=200,y=325)


## Goto Login Page
btnGoto=Button(window,text="Sign in instead!",background="white",fg="blue",relief=RAISED,borderwidth=0)
btnGoto.place(x=50,y=425)


## Submit Values Area
btnSignUp=Button(window,text="Next!",background="blue",fg="white")
btnSignUp.place(x=200,y=425)



window.mainloop()
