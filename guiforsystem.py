from tkinter import *

window=Tk()
window.title("Attendence System")
window.geometry('300x250')
Label(text="Choose login or Register ",bg="blue",width="300",height="2",font=("Arial Bold",13)).pack()
Label(text="").pack()
import biomaetricsSignup.py as test
Button(text="Sign In",height="2",width="30",command=test).pack()
Label(text="").pack()
Button(text="Sign Up",height="2",width="30").pack()
window.mainloop()
