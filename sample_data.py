import mysql.connector as s

#connection to sql
mc=s.connect(host='localhost',user='root',passwd='Kss#140206',database='hotel_manage')
cr=mc.cursor()
cr.execute("Insert into guest values('Ram',9942134679,100234567123,118,'2024-01-20','d')")
cr.execute("Insert into guest values('Jenny',9924316498,100234987231,105,'2024-01-20','a')")
cr.execute("Insert into guest values('Shristi',9432164679,1045345679123,119,'2024-01-18','d')")
cr.execute("Insert into guest values('Karthi',9942134567,100434787123,113,'2024-01-19','c')")
cr.execute("Insert into guest values('krithi',832134699,100734677123,112,'2024-01-18','c')")
cr.execute("Insert into guest values('nikitha',9942134679,100234563463,109,'2024-01-23','b')")
mc.commit()

#--------------------
cr.execute("Update rooms set availability='occupied' where roomno=118;")
cr.execute("Update rooms set availability='occupied' where roomno=105;")
cr.execute("Update rooms set availability='occupied' where roomno=119;")
cr.execute("Update rooms set availability='occupied' where roomno=113;")
cr.execute("Update rooms set availability='occupied' where roomno=112;")
cr.execute("Update rooms set availability='occupied' where roomno=109;")
mc.commit()

cr.close()
mc.close()
