#hotel management tables
import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='Kss#140206')
cr=mc.cursor()
from tkinter import *

#create database
def db_hot():
    cr.execute('create database if not exists hotel_manage;')
    cr.execute('use hotel_manage;')

#create table-roomtype
def room_type():
    sql='''create table if not exists room_type(
    roomtypeid varchar(1) primary key,
    type_description varchar(40),
    price int not null,
    no_of_rooms int not null);'''
    cr.execute(sql)
    mc.commit()

#data insertion into roomtype
def room_type_data():
    cr.execute("insert into room_type values('a','Standard non AC',1250,5);")
    cr.execute("insert into room_type values('b','Standard AC',1500,5);")
    cr.execute("insert into room_type values('c','Double bed AC',1650,5);")
    cr.execute("insert into room_type values('d','Triple bed AC',1750,5);")
    mc.commit()

#create table - rooms
def roomtable():
    sql='''create table if not exists rooms(
    roomno int primary key,
    roomtypeid varchar(1) not null,
    availability enum('occupied','vacant') default 'vacant');'''
    #o - occupied , v - vacant
    cr.execute(sql)

#insert data into rooms
def rooms_data():
    #type a
    for i in range(101,106):
        sql="insert into rooms(roomno,roomtypeid)values(%s,%s);"
        values=(i,'a')
        cr.execute(sql,values)
    #type b
    for i in range(106,111):
        sql="insert into rooms(roomno,roomtypeid)values(%s,%s);"
        values=(i,'b')
        cr.execute(sql,values)
    #type c
    for i in range(111,116):
        sql="insert into rooms(roomno,roomtypeid)values(%s,%s);"
        values=(i,'c')
        cr.execute(sql,values)
    #type d
    for i in range(116,121):
        sql="insert into rooms(roomno,roomtypeid)values(%s,%s);"
        values=(i,'d')
        cr.execute(sql,values)
    mc.commit()

    

#create table - guest
def guesttable():
    sql='''create table if not exists guest(
    name varchar(30),
    phno bigint not null,
    ano bigint primary key,
    roomno int unique,
    check_in_date date,
    room_type_id varchar(1) references room_type(roomtypeid));'''
    cr.execute(sql)
   


db_hot()
guesttable()
roomtable()
room_type()
rooms_data()
room_type_data()




    

