#-----------------------------------------------------------------------------
#importing required modules
from tkinter import *
import mysql.connector as s
import hotel_pack.button_commands as bc
from tkinter import ttk
from tkinter import messagebox
#------------------------------------------------------------------------------
#home pg

def homefn(): 
    home=Tk()
    home.geometry('1920x1080')
    home.title('HOME PAGE')

    # Define image
    bg = PhotoImage(file="background.png")

    # Create a label as a container for the background image
    bg_label = Label(home, image=bg)
    bg_label.config(bg='#00162e')
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    #-------------------------------------------------------------------------------

    #button check in 
    cin=Button(home,
               text='Check In',
               font=('Times New Roman Greek',20,'bold'),
               fg='white',
               bg='#040436',
               width=20,
               command=bc.checkin)
    cin.place(x=100,y=100)

    #------------------------------------------------

    #button check out
    cout=Button(home,
                text='Check Out',
                font=('Times New Roman Greek',20,'bold'),
                fg='white',
                bg='#040436',
                width=20,
                command=bc.chkout)
    cout.place(x=100,y=550)
    #--------------------------------------------------

    #button view guest details
    view=Button(home,
                text='View Guest Details',
                font=('Times New Roman Greek',20,'bold'),
                fg='white',
                bg='#040436',
                width=20,
               command=bc.viewguest)
    view.place(x=100,y=250)

    #-----------------------------------------------------

    #button room status
    status=Button(home,
                text='Room Status',
                font=('Times New Roman Greek',20,'bold'),
                fg='white',
                bg='#040436',
                width=20,
                command=bc.room_status)
    status.place(x=100,y=400)

    #---------------------------------------------------

    #logout button function
    def logout():
        messagebox.showinfo(title='logout info',message='''  Logged Out!!!
        Thank You!''')
        home.destroy()
       

    #button logout
    lot=Button(home,
               text='Logout',
               font=('Times New Roman Greek',20,'bold'),
               fg='white',
               bg='#040436',
               width=15,
               command=logout
               )
    lot.place(x=1050,y=600)

    # Main loop
    home.mainloop()
