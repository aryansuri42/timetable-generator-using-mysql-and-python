import mysql.connector
g=mysql.connector.connect(host="localhost", user="root", passwd="7291001232",database="timetable")

def choices1():
    w=input("==========((Enter Your Username))==========")
    print("==========((Welcome))==========", w)
    con1=g.cursor()
    query='select * from tableclass where username=%s'
    con1.execute(query,(w, ))
    files=con1.fetchall()
    for i in files:
        print(i)
    print("Options Loading....")
    print("==========((Enter 1. To View Timetable))==========")
    print("==========((Enter 2. To Quit))==========")
    ch=int(input("==========((Enter Your Option))=========="))
    if ch==1:
        name_table=input("ENTER NAME OF TABLE....")
        QUERY='select * from '+name_table
        conb=g.cursor()
        conb.execute(QUERY)
        resut_table=conb.fetchall()
        l2=[]
        x = PrettyTable(["Day", "Period No.", "Time", "Subject Name","Teacher"])
        x.align["Day"] = "l"
         
                    
        for i in resut_table:
            for j in i:
                f=l2.append(j)    
                if len(l2)==5:
                    rep1=l2[2]
                    rep2=rep1.replace(" ",":",3)
                    rep3=""
                    count=0
                    for i in rep2:
                        if i==":":
                            count+=1
                            if count==2:
                                rep3=rep3+"-"
                            else:
                                rep3=rep3+i
                        else:
                            rep3=rep3+i   
                    l2[2]=rep3
                    x.add_row(l2)
                    l2=[]
        print(x)
    
        print("TO GO BACK PRESS.  1")
        print("TO QUIT PRESS ANYTHING")
        ch=input("")
        if ch=="1":
            choices1()
        else:
            print("Thanks")
            
        
