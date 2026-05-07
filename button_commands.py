#commands for home buttons

#import statements
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, StringVar, OptionMenu
import mysql.connector as s

#connection to sql
mc=s.connect(host='localhost',user='root',passwd='Pewsql@2704',database='hotel_manage')
cr=mc.cursor()
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#newguest function
def cinguest():
    try:
        #capturing the entry values
        name1=name.get()
        phno1=phno.get()
        ano1=ano.get()
        roomno1=roomno.get()

        #getting availability
        sql='select availability from rooms where roomno=%s;'
        values=(roomno.get(),)
        cr.execute(sql,values)
        roomav=cr.fetchall()
        
        #checking all fields
        if name1=='' or phno1=='' or ano1=='' or roomno1=='':
            messagebox.showerror('error','All fields are required!!')
            checkinpg.destroy()
        #checking validity of input
        elif len(phno1)!=10 or phno1.isdigit()==False:
            messagebox.showerror('error','Enter valid contact number!!')
            checkinpg.destroy()
        elif len(ano1)!=12 or ano1.isdigit()==False:
            messagebox.showerror('error','Enter valid aadhar number!!')
            checkinpg.destroy()
        #checking validity of room no
        elif int(roomno1)<101 or int(roomno1)>120:
            messagebox.showerror('error','Enter valid room number!!')
            checkinpg.destroy()
            
        #checking for availability
        elif roomav[0][0]=='occupied':
            messagebox.showerror('error','The room is already occupied !!')
            checkinpg.destroy()
            
        #entering into database
        else:
            sql='select roomtypeid from rooms where roomno=%s;'
            cr.execute(sql,(roomno.get(),))
            roomtype=cr.fetchall()
            sql='INSERT INTO guest VALUES (%s, %s, %s, %s,current_date,%s);'
            values=(name.get(),phno.get(),ano.get(),roomno.get(),roomtype[0][0])
            cr.execute(sql, values)
            sql="update rooms set availability='occupied' where roomno=%s;"
            values=(roomno.get(),)
            cr.execute(sql,values)
            mc.commit()
        
            #closing window
            checkinpg.destroy()

            messagebox.showinfo('Success','Checked in successfully')
    except:
        messagebox.showerror('ERROR','Enter valid data')
        checkinpg.destroy()
    
#command check in
def checkin():
    global name,phno,ano,roomno,checkinpg  # Declare the variables as global before defining them
    checkinpg=Tk()
    checkinpg.geometry('700x450+600+100')
    checkinpg.title('CHECK IN PAGE')
    checkinpg.config(background='#09094a')
#-------------------------------------------------
    #label customer name
    namelabel=Label(checkinpg,
                    text='Guest Name',
                    font=('Times New Roman Greek',20,'bold'),
                    fg='white',
                    bg='#09094a',
                    padx=20,
                    pady=20)
    namelabel.place(x=50,y=50)

    #entry name
    name=Entry(checkinpg,
               font=('arial',20),
               fg='black',
               bg='white')
    name.place(x=250,y=65)

#----------------------------------------------------

    #label phno
    phnolabel=Label(checkinpg,
                text='Contact No',
                font=('Times New Roman Greek',20,'bold'),
                fg='white',
                bg='#09094a',
                padx=20,
                pady=20)
    phnolabel.place(x=50,y=100)

    #phno entry
    phno=Entry(checkinpg,
               font=('arial',20),
               fg='black',
               bg='white')
    phno.place(x=250,y=115)

#--------------------------------------------------
    #label aadhar no
    anolabel=Label(checkinpg,
            text='Aadhar no',
            font=('Times New Roman Greek',20,'bold'),
            fg='white',
            bg='#09094a',
            padx=20,
            pady=20)
    anolabel.place(x=50,y=150)

    #entry aadhar no
    ano=Entry(checkinpg,
               font=('arial',20),
               fg='black',
               bg='white')
    ano.place(x=250,y=165)

#---------------------------------------------------
    #label roomno
    roomlabel=Label(checkinpg,
            text='Room No',
            font=('Times New Roman Greek',20,'bold'),
            fg='white',
            bg='#09094a',
            padx=20,
            pady=20)
    roomlabel.place(x=50,y=200)

    #entry room no
    roomno=Entry(checkinpg,
               font=('arial',20),
               fg='black',
               bg='white')
    roomno.place(x=250,y=215)
#----------------------------------------------------
    #button check in
    checkin=Button(checkinpg,
                   text='Check In Guest',
                   font=('Times New Roman Greek',15,'bold'),
                   fg='white',
                   bg='#453e59',
                   command=cinguest
                   )
    checkin.place(x=450,y=300)
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------- 
#view guest details using treeview widget
def viewguest():
    #window
    view=Tk()
    view.geometry('700x450+600+100')
    view.title('VIEW GUEST DETAILS')
    view.config(background='#09094a')

    #create treeview
    guest=ttk.Treeview(view)

    #define columns
    guest['columns']=('name','phno','ano','roomno','checkindate')

    #format columns
    guest.column('#0',width=0,stretch=NO)
    guest.column('name',anchor=CENTER,width=120)
    guest.column('phno',anchor=CENTER,width=120)
    guest.column('ano',anchor=CENTER,width=120)
    guest.column('roomno',anchor=CENTER,width=120)
    guest.column('checkindate',anchor=CENTER,width=120)

    #create headings
    #to change font ttk.style
    style=ttk.Style()
    style.configure("Treeview.Heading", font=('Times New Roman Greek', 10, 'bold'))

    guest.heading('#0',text='',anchor=CENTER)
    guest.heading('name',text='Name',anchor=CENTER)
    guest.heading('phno',text='Phone no',anchor=CENTER)
    guest.heading('ano',text='Aadhar no',anchor=CENTER)
    guest.heading('roomno',text='Room no',anchor=CENTER)
    guest.heading('checkindate',text='Check in date',anchor=CENTER) 

    #style option to background colors, foreground colors, and row heights
    #background-sets the background color for the content area
    #foreground-sets the foreground color (text color) 
    #rowheight-Sets the height of each row
    #fieldbackground-Sets the background color for the cells

    style.configure('Treeview',background='#d3d3d3',foreground='black',rowheight=25, fieldbackground="#d3d3d3")
    style.map("Treeview", background=[("selected", "#347083")])

    #extract records from sql
    cr.execute('select * from guest;')
    data=cr.fetchall()

    #add records into table by loop
    c=0
    for record in data:
        guest.insert(parent='',
                     index='end',
                     iid=c,
                     text='',
                     values=(record[0],record[1],record[2],record[3],record[4]))
        c+=1
    guest.place(x=50,y=100,height=275,width=600)

    #creating a vertical scrollbar
    sb=ttk.Scrollbar(view,orient='vertical',command=guest.yview)

    #attaching the scrollbar to treeview
    guest.configure(yscrollcommand=sb.set)

    #place the scrollbar
    sb.place(x=650,y=100,height=275)

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#room status
def room_status():
    #window
    status=Tk()
    status.geometry('700x450+600+100')
    status.title('ROOM STATUS')
    status.config(background='#09094a')
    
    #show vacancies command
    def show_vac():
        vac=ttk.Treeview(status)
        vac['columns']=('roomno','roomtype','price')

        #format columns
        vac.column('#0',width=0,stretch=NO)
        vac.column('roomno',anchor=CENTER,width=170)
        vac.column('roomtype',anchor=CENTER,width=170)
        vac.column('price',anchor=CENTER,width=170)

        #create headings
        vac.heading('#0',text='',anchor=CENTER)
        vac.heading('roomno',text='Room no',anchor=CENTER)
        vac.heading('roomtype',text='Type description',anchor=CENTER)
        vac.heading('price',text='Price',anchor=CENTER)

        #to change font ttk.style
        style=ttk.Style()
        style.configure("Treeview.Heading", font=('Times New Roman Greek', 10, 'bold'))

        #style options
        style.configure('Treeview',background='#d3d3d3',foreground='black',rowheight=25, fieldbackground="#d3d3d3")
        style.map("Treeview", background=[("selected", "#347083")])

        #retrieve records from sql
        cr.execute('''select roomno,type_description,
                    price from rooms join room_type
                    where rooms.roomtypeid=room_type.roomtypeid
                    and rooms.availability="vacant";''')
        data=cr.fetchall()

        #insert records into treeview table by loop
        c=0
        for record in data:
            vac.insert(parent='',
                          index='end',
                          iid=c,
                          text='',
                          values=(record[0],record[1],record[2]))
            c+=1
        vac.place(x=100,y=130,height=275,width=510)

        vac_label=Label(status,
            text='Vacant rooms',
            font=('arial',10,'bold'),
            fg='black',
            bg='white',
            bd=10)
        vac_label.place(x=100,y=92,width=525)
        #creating a vertical scrollbar
        sb=ttk.Scrollbar(status,orient='vertical',command=vac.yview)

        #attaching the scrollbar to treeview
        vac.configure(yscrollcommand=sb.set)

        #place the scrollbar
        sb.place(x=610,y=130,height=275)

    def show_occ():
        occ=ttk.Treeview(status)
        occ['columns']=('roomno','roomtype')

        #format columns
        occ.column('#0',width=0,stretch=NO)
        occ.column('roomno',anchor=CENTER,width=255)
        occ.column('roomtype',anchor=CENTER,width=255)

        #create headings
        occ.heading('#0',text='',anchor=CENTER)
        occ.heading('roomno',text='Room no',anchor=CENTER)
        occ.heading('roomtype',text='Type description',anchor=CENTER)

        #to change font ttk.style
        style=ttk.Style()
        style.configure("Treeview.Heading", font=('Times New Roman Greek', 10, 'bold'))

        #style options
        style.configure('Treeview',background='#d3d3d3',foreground='black',rowheight=25, fieldbackground="#d3d3d3")
        style.map("Treeview", background=[("selected", "#347083")])

        #retrieve records from sql
        cr.execute('''select roomno,type_description
                    from rooms join room_type
                    where rooms.roomtypeid=room_type.roomtypeid
                    and rooms.availability="occupied";''')
        data=cr.fetchall()

        #insert records into treeview table by loop
        c=0
        for record in data:
            occ.insert(parent='',
                          index='end',
                          iid=c,
                          text='',
                          values=(record[0],record[1]))
            c+=1
        occ.place(x=100,y=130,height=275,width=510)

        occ_label=Label(status,
            text='Occupied rooms',
            font=('arial',10,'bold'),
            fg='black',
            bg='white',
            bd=10)

        occ_label.place(x=100,y=92,width=525)

        #creating a vertical scrollbar
        sb=ttk.Scrollbar(status,orient='vertical',command=occ.yview)

        #attaching the scrollbar to treeview
        occ.configure(yscrollcommand=sb.set)

        #place the scrollbar
        sb.place(x=610,y=130,height=275)
    def show_all():
        #create treeview widget
        roomst=ttk.Treeview(status)

        #define columns
        roomst['columns']=('roomno','status','roomtype')

        #format columns
        roomst.column('#0',width=0,stretch=NO)
        roomst.column('roomno',anchor=CENTER,width=170)
        roomst.column('status',anchor=CENTER,width=170)
        roomst.column('roomtype',anchor=CENTER,width=170)

        #create headings
        roomst.heading('#0',text='',anchor=CENTER)
        roomst.heading('roomno',text='Room no',anchor=CENTER)
        roomst.heading('status',text='Status',anchor=CENTER)
        roomst.heading('roomtype',text='Type description',anchor=CENTER)
        #to change font ttk.style
        style=ttk.Style()
        style.configure("Treeview.Heading", font=('Times New Roman Greek', 10, 'bold'))

        #style options
        style.configure('Treeview',background='#d3d3d3',foreground='black',rowheight=25, fieldbackground="#d3d3d3")
        style.map("Treeview", background=[("selected", "#347083")])

        #retrieve records from sql
        cr.execute('''select roomno,availability,
                    type_description from rooms join room_type
                    where rooms.roomtypeid=room_type.roomtypeid''')
        data=cr.fetchall()

        #insert records into treeview table by loop
        c=0
        for record in data:
            roomst.insert(parent='',
                          index='end',
                          iid=c,
                          text='',
                          values=(record[0],record[1],record[2]))
            c+=1
        roomst.place(x=100,y=130,height=275,width=510)

        all_label=Label(status,
            text='rooms',
            font=('arial',10,'bold'),
            fg='black',
            bg='white',
            bd=10)

        all_label.place(x=100,y=92,width=525)

        #creating a vertical scrollbar
        sb=ttk.Scrollbar(status,orient='vertical',command=roomst.yview)

        #attaching the scrollbar to treeview
        roomst.configure(yscrollcommand=sb.set)

        #place the scrollbar
        sb.place(x=610,y=130,height=275)
    show_all()
    #button show all rooms
    all_rooms=Button(status,
               text='Show all rooms',
               font=('Times New Roman Greek',10,'bold'),
               fg='white',
               bg='#453e59',
               command=show_all
               )
    all_rooms.place(x=100,y=30)

    #button show vacancies
    vac=Button(status,
               text='Show Vacancies',
               font=('Times New Roman Greek',10,'bold'),
               fg='white',
               bg='#453e59',
               command=show_vac
               )
    vac.place(x=300,y=30)

    #button occupied rooms
    occ=Button(status,
               text='Occupied rooms',
               font=('Times New Roman Greek',10,'bold'),
               fg='white',
               bg='#453e59',
               command=show_occ
               )
    occ.place(x=500,y=30)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#check out window
def checkout(ro,n,ph,an,ci):
    global ano,rno #declaring the variables as global
    checkoutpg=Tk()
    checkoutpg.geometry('700x450+600+100')
    checkoutpg.title("CHECK_OUT PAGE")
    checkoutpg.configure(background='#09094a')
#------------------------------------------------------------

    #label for roomno
    rn=Label(checkoutpg,
        text="Room Number\t"+str(ro),
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    rn.place(x=20,y=50)
 #-------------------------------------------------------------
    
    #label for phoneno
    n=Label(checkoutpg,
            text="Name\t\t"+str(n),
            font=('Times New Roman Greek',20,'bold'),
            fg='white',
            bg='#09094a',
            padx=20,
            pady=20)
    n.place(x=20,y=110)
#-------------------------------------------------------------
    #label for aadharno
    an=Label(checkoutpg,
        text="Aadhar Number\t"+str(an),
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    an.place(x=20,y=170)
#-------------------------------------------------------------
    #label for phoneno
    ph=Label(checkoutpg,
        text="Phone Number\t"+str(ph),
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    ph.place(x=20,y=230)
#-------------------------------------------------------------
    #label for checkout date
    cd=Label(checkoutpg,
        text="Checked in date\t"+str(ci),
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    cd.place(x=20,y=300)
   
#-------------------------------------------------------------
    def Entry_values():
       
        ##r-roomno
        sql = "SELECT roomno, name, phno, ano, check_in_date, current_date FROM guest WHERE roomno = %s;"
        cr.execute(sql, (ro,))
        data = cr.fetchall()       
        #to get stay duration
        sql='SELECT current_date-check_in_date from guest where roomno=%s;'
        cr.execute(sql,(ro,))
        sd=cr.fetchone()
        #to get roomtype
        sql='select room_type_id from guest where roomno=%s;'
        cr.execute(sql,(ro,))
        rt=cr.fetchone()
        #to get price
        sql='select price from room_type where roomtypeid=%s;'
        cr.execute(sql,rt)
        price=cr.fetchone()
        #calc amt
        total=sd[0]*price[0]
        return data[0],sd[0],total

    def billing():
        try:
            data = Entry_values()
            rono, name, phno, ano, check_in, check_out = data[0]
            sd,total = data[1],data[2]
            bill_text = f"""\
            \t\t\t\tSTAY INN
            \t---------------------------------------------------------------------------------------
            \tRoom_Number\t\t\t   {rono}
            \t---------------------------------------------------------------------------------------
            \tCustomer Name\t\t\t{name}
            \tPhone Number\t\t\t{phno}
            \tAadhar Number\t\t\t{ano}
            \tCheck in date\t\t\t{check_in}
            \tCheck out date\t\t\t{check_out}
            \tStay duration\t\t\t{sd}
            \t---------------------------------------------------------------------------------------
            \tTotal amount\t\t\t{total}
            \t---------------------------------------------------------------------------------------"""           
            an = Label(checkoutpg,
                text=bill_text,
                font=('Times New Roman Greek', 13, 'bold'),
                fg='white',
                bg='#09094a',
                padx=20,
                pady=20,
                justify='left',
                anchor='nw')
            an.place(x=0, y=20)

            def coutguest():
                sql='delete from guest where roomno=%s;'
                cr.execute(sql,(ro,))
                sql='update rooms set availability="vacant" where roomno=%s;'
                cr.execute(sql,(ro,))
                mc.commit()
                checkoutpg.destroy()
                messagebox.showinfo('Success','Checked out succesfully')   

            #final check out
            out = Button(checkoutpg,
                     text="Check out",
                     font=("Times New Roman Greek", 15, "bold"),
                     fg="white",
                     bg="#453e59",
                     command=coutguest)
            out.place(x=490, y=370)
            cd.place_forget()
            bill.place_forget()
        except:
            messagebox.showerror('ERROR',"Bill can't be generated")
            checkoutpg.destroy()
        
    bill = Button(checkoutpg,
                 text="Show bill",
                 font=("Times New Roman Greek", 15, "bold"),
                 fg="white",
                 bg="#453e59",
                 command=billing)
    bill.place(x=490, y=370)
#-----------------------------------------------------------------------------
#to destroy chkout window 
def destroy(chkpg,ro,n,ph,an,ci):
    chkpg.destroy()
    checkout(ro,n,ph,an,ci)
#------------------------------------------------------------------------------
def chkout():
    global rno,ro,n,ph,an,ci#declaring the variable as global
    chkpg=Tk()
    chkpg.geometry('500x400+800+150')
    chkpg.title("CHECK_OUT PAGE")
    chkpg.configure(background='#09094a')
    def values(r):
        r=var.get()
        sql=('Select roomno, name, phno, ano, check_in_date FROM guest WHERE roomno = %s;')
        cr.execute(sql, (r,))
        data = cr.fetchone()
        ro,n,ph,an,ci=data
        return ro,n,ph,an,ci
#------------------------------------------------------------
    #label for headings
    #label for roomno
    th=Label(chkpg,
        text="""---------------------------------------------------
Stay Inn
---------------------------------------------------
                    """,
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    th.place(x=0,y=0)
    
    #label for roomno
    rn=Label(chkpg,
        text="Room Number  ",
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    rn.place(x=10,y=230)
    var=StringVar()
    options=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]
    rno=OptionMenu(chkpg,var,*options,command=values)
    var.set(101)
    rno.place(x=260,y=250)
    #label for name
    n=Label(chkpg,
        text="Name ",
        font=('Times New Roman Greek',20,'bold'),
        fg='white',
        bg='#09094a',
        padx=20,
        pady=20)
    n.place(x=10,y=150)
     #entry name
    name=Entry(chkpg,
               font=('arial',20),
               fg='black',
               bg='white')
    name.place(x=140,y=170)
    vd= Button(chkpg,
                 text="Show Details",
                 font=("Times New Roman Greek", 15, "bold"),
                 fg="white",
                 bg="#453e59",
                 command=lambda: destroy(chkpg,*values(var.get())))
    vd.place(x=300, y=330)





