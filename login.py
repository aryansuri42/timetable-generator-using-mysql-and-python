import mysql.connector
import choices1
import choices2
import signup


con=mysql.connector.connect(host="localhost", user="root", passwd="7291001232",database="timetable")
def login():
    a=input("==========((Enter Your Username))==========")
    b=input("==========((Enter Your Password))==========")
    con1=con.cursor()
    query="SELECT * FROM login WHERE username=%s"
    con1.execute(query, (a, ))
    result=con1.fetchall()
    for i in result:
        if a in i and b in i :
            print("==========((Acess Granted))==========")
            print("==========((Select Your Post 1.Admin , 2.Teacher))==========")
            ch=int(input(""))
            if ch==1:
                key="revelationrush"
                key1=input("==========((Enter The Pass Key))==========")
                if key==key1:
                    print("==========((Welcome Admin))==========")
                    choices2.choices2()
                else:
                    print("==========((Wrong Key Please Retry))==========")
                    login()
            elif ch==2:
                choices1.choices1()
            else:
                print("==========((Wrong Choice Retry))==========")
                login()
        else:
            print("==========((If Want To Retry Press 1.))==========")
            print("==========((If Want To Signup Press 2.))==========")
            ch1=int(input(""))
            if ch1==1:
                login()
            else:
                signup.signup()

                
            
        
