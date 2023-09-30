import mysql.connector
import login
g=mysql.connector.connect(host="localhost", user="root", passwd="7291001232",database="timetable")


def signup():
    name=input("==========((Enter Your Username))==========")
    passw=input("==========((Enter Your Password))==========")
    post=int(input("==========((Enter Your Post  [[Press 1. For Admin,Press 2. For Teacher]]========== "))
    if post==1:
        ask=input("==========((Enter Admin Pass Key))==========")
        if ask=="revelationrush":
            print("==========((Welcome Administrator))==========")
            con1=g.cursor()
            c="insert into login values('{}','{}','{}')".format(name,passw,post)
            con1.execute(c)
            g.commit()
            print("==========((Going To Login Option Now))==========")
            login.login()
        else:
            print("==========((Do Not Try To Steal Info))==========")
    else:
        con1=g.cursor()
        c="insert into login values('{}','{}','{}')".format(name,passw,post)
        con1.execute(c)
        g.commit()
        print("==========((Going To Login Option Now))==========")
        login.login()
