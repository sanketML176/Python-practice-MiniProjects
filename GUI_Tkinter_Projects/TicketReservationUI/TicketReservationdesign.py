from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DbReservationConnectClass import DBConnect
from ListReservation import ListTickets

dbConnect = DBConnect()
root=Tk()

ttk.Label(root, text="Full Name:").grid(row=0, column=0, pady=10, padx=10)
EntryFullName = ttk.Entry(root, width=30, font=("Arial", 16))
EntryFullName.grid(row=0, column=1, columnspan=2,pady=10)
root.title('Ticket Reservation')

# Set Style
root.configure(background="#e1d8b2")
style=ttk.Style()
style.theme_use("classic")
style.configure("TLable", background="#e1d8b2")
style.configure("TButton", background="#e1d8b2")
style.configure("TRadioButton", background="#e1d8b2")

SpanGender=StringVar()
SpanGender.set("Male")
ttk.Label(root, text="Gender").grid(row=1, column=0)
ttk.Radiobutton(root, text='Male', variable=SpanGender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text='Female', variable=SpanGender, value="Female").grid(row=1, column=2)

TextComments= Text(root, width=30, height=6, font=('Arial', 16))
TextComments.grid(row=3, column=1, columnspan=2)
ttk.Label(root, text="Comments").grid(row=3, column=0)

buButton=ttk.Button(root, text='Submit')
buButton.grid(row=4,column=3)
buList=ttk.Button(root, text='List Res.')
buList.grid(row=4,column=2)

def ButtonClick():
    print("Full Name: {}".format(EntryFullName.get()))
    print("Gender   : {}".format(SpanGender.get()))
    print("Comments : {}".format(TextComments.get(1.0,'end')))
    msg=dbConnect.Add(EntryFullName.get(),SpanGender.get(),TextComments.get(1.0,'end'))
    messagebox.showinfo(title="Add info", message=msg)
    EntryFullName.delete(0, 'end')
    TextComments.delete(1.0,'end')

def ButtonList():
    listTickets =ListTickets()

buButton.config(command=ButtonClick)
buList.config(command=ButtonList)

root.mainloop()

listTickets=ListTickets()
