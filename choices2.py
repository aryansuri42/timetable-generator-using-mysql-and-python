import mysql.connector
from prettytable import PrettyTable
g=mysql.connector.connect(host="localhost", user="root", passwd="7291001232",database="classtable")
def choices2():
    choices2.w=input("==========((Enter Teacher's Username))==========")
    print("==========((Welcome))==========", choices2.w)
    choicetab()
def choicetab():
    con1=g.cursor()
    query='select Table_Name from tableclass where username=%s'
    con1.execute(query,(choices2.w, ))
    files=con1.fetchall()
    print("TABLES CREATED ARE AS FOLLOWS:-")
    for i in files:
        print(i)
    print("Options Loading....")
    print("==========((Press 1. For New Timetable))==========")
    print("==========((Enter 2. To View Timetable))==========")
    print("==========((Enter 3. To Delete))==========")
    print("==========((Enter 4. To Quit))==========")
    ch=int(input("==========((Enter Your Option))=========="))
    if ch==1:
        conv=g.cursor()
        choicetab.name_table=input('==========((Enter Name Of Timetable e.g XIIA29/3/21  ))==========...')
        conv.execute("insert into tableclass values('{}','{}')".format(choices2.w,choicetab.name_table))
        g.commit()
        query="create table "
        query1=query+choicetab.name_table
        query2=query1+" (DAY varchar(10) ,Period_No int(1), Time varchar(12), Subject_Name varchar(15), Teacher_Name varchar(15))"
        con2=g.cursor()
        con2.execute(query2)
        print("Table Created Now Loading...")
        print("==========((Add Values))==========")
        days=int(input('ENTER THE NUMBER OF DAYS....'))
        periodno=int(input('ENTER NUMBER OF PERIODS....'))
        for i in range(0,periodno*days):
            go()
        print("TO GO BACK PRESS.  1")
        print("TO CHANGE TEACHER'S NAME PRESS. 2 ")
        print("TO QUIT PRESS ANYTHING")
        ch=input("")
        if ch=="1":
            choicetab()
        elif ch=="2":
            choices2()
        else:
            print("Thanks")
    elif ch==2:
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
        print("TO CHANGE TEACHER'S NAME PRESS. 2 ")
        print("TO QUIT PRESS ANYTHING")
        ch=input("")
        if ch=="1":
            choicetab()
        elif ch=="2":
            choices2()
        else:
            print("Thanks")    
    elif ch==3:
        name_table=input("NAME OF THE TABLE TO BE DELETED....")
        condel=g.cursor()
        condel1=g.cursor()
        queryt="Delete From tableclass where Table_Name=%s"
        querytab="Drop table "+name_table
        condel.execute(queryt,(name_table,))
        condel1.execute(querytab)
        print("Table Deleted")
        print("TO GO BACK PRESS.  1")
        print("TO QUIT PRESS ANYTHING")
        print("TO GO BACK PRESS.  1")
        print("TO CHANGE TEACHER'S NAME PRESS. 2 ")
        print("TO QUIT PRESS ANYTHING")
        ch=input("")
        if ch=="1":
            choicetab()
        elif ch=="2":
            choices2()
        else:
            print("Thanks")
def go():
    day=input('ENTER THE DAY OF WEEK....')
    period=int(input("ENTER THE PERIOD NUMBER...."))
    timeface=input("ENTER TIME e.g 8:30-9:30....")
    time=""
    for i in timeface:
        if i==":" or i=="-":
            time=time+" "
        else:
            time=time+i
    sub=input("ENTER SUBJECT NAME....")
    teach_name=input("ENTER TEACHER NAME....")
    print("TO WATCH THE NAME OF TABLES WHERE PERIOD IS CLASHING PRESS.1")
    print("TO CONTINUE WITHOUT CLASHING WITH ANY OTHER TABLE PRESS ENTER")
    cfa=input("")
    if cfa=="1":
        query='select Table_Name from tableclass where username=%s'
        con1=g.cursor()
        con1.execute(query,(choices2.w, ))
        files=con1.fetchall()
        l3=[]
        for i  in files:
            for j in i:
                l3.append(j)
        for u in l3:
            con5=g.cursor()
            query9="select * from "+u+" where Period_No=%s and Teacher_Name=%s and Day=%s"
            con5.execute(query9, (period,teach_name,day ))
            res_search=con5.fetchall()
            for i in res_search:
                print(i)
        if teach_name in i:
            print(u)
            print("Period are clashing make ammends")
            go()
                    
        else:
            conv=g.cursor()
            conv.execute("insert into "+choicetab.name_table+" values('{}',{},'{}','{}','{}')".format(day,period,time,sub,teach_name))
            g.commit()
                    
                        
    else:
        conv=g.cursor()
        conv.execute("insert into "+choicetab.name_table+" values('{}',{},'{}','{}','{}')".format(day,period,time,sub,teach_name))
        g.commit()


                  


        

        




