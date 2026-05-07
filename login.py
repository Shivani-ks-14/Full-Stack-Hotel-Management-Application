from tkinter import *
from tkinter import messagebox
import hotel_pack.home as home
#---------------------------------------------------------

def loginfn():
    login = Tk()
    login.title("Login page")
    login.geometry("1920x1080")


    # Define bg image and icon
    bg = PhotoImage(file="background.png")
    #defining a logo for login pg
    #icon=PhotoImage(file="icon.png")
    # Keep references to images to prevent garbage collection
    login.bg = bg
    #login.icon = icon
    #login.iconphoto(True,icon)

    # Create a label as a container for the background image
    bg_label = Label(login, image=bg)
    bg_label.config(bg='#00162e')
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    # Label welcome
    label1 = Label(bg_label,
                   text='Customised Hotel Management-data management made easy!!',
                   font=('Constantia', 20, 'bold'),
                   fg='white')
    label1.pack(fill=X, padx=20, pady=20)
    label1.config(bg='#050a2b')  

    # Label username
    uselabel = Label(bg_label,
                     text='Username',
                     font=('Times New Roman Greek', 20, 'bold'),
                     fg='white')
    uselabel.place(x=100, y=150)
    uselabel.config(bg='#050a2b')  

    # username entry
    username = Entry(bg_label,
                     font=('arial', 20),
                     fg='black',
                     bg='white')
    username.place(x=300, y=155)

    # Label password
    passwdlabel = Label(bg_label,
                        text='Password',
                        font=('Times New Roman Greek', 20, 'bold'),
                        fg='white')
    passwdlabel.place(x=100, y=200)
    passwdlabel.config(bg='#050a2b')  

    # passwd entry
    passwd = Entry(bg_label,
                   font=('arial', 20),
                   fg='black',
                   bg='white',
                   show='*')
    passwd.place(x=300, y=200)

    # login command
    def loginc():
        usernamel = username.get()
        passwdl = passwd.get()
        if usernamel in ['user','admin'] and passwdl == 'stayinn':
            login.destroy()
            home.homefn()
        elif usernamel == "" or passwdl == "":
            messagebox.showerror('ERROR', 'All fields are required  !!!')
        else:
            messagebox.showerror('ERROR', 'Invalid username or password !!!')

    # button login
    loginbutton = Button(bg_label,
                         text='LOGIN',
                         font=('Times New Roman Greek', 20),
                         fg='white',
                         bg='#050a2b',
                         command=loginc)
    loginbutton.place(x=700, y=400)

    # code block watermark
    codelabel = Label(bg_label,
                      text='created by CodeBlocks',
                      font=('Constantia', 20, 'bold'),
                      fg='#8baab0')
    codelabel.place(x=900, y=550)
    codelabel.config(bg='#050a2b')  

    # Main loop
    login.mainloop()

loginfn()
