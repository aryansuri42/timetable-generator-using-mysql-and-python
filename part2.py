if CHOICE==6:
    FOODNO=int(input("Enter Grocery No."))
    query="delete from grocery where GROCERYNO={}".format(GROCERYNO)
    mycur.execute(query)
    mydb.commit()
    if mycur.rowcount>0:
        print("DATA DELETED SUCCESFULLY..")
    else:
        print("NO DATA FOUND")

if CHOICE==7:
    query="select * from grocery"
    mycur.execute(query)
    x=mycur.fetchall()
    print(x)
    
if CHOICE==8:
    b=input("DO YOU WANT TO TIP?" 'Y/N--')
    if b=="Y":
        print("TIP")
        print("9-INSERT VALUES")
        print("10-DELETE DATA")
        print("11-DISPLAY ALL ITEMS")
        print("12-EXIT")
        CHOICE=int(input("ENTER YOUR CHOICE: "))
        if CHOICE==9:
            SERIALNO==int(input("ENTER SERIAL NO"))
            CUSTOMERNAME=input("ENTER NAME")
            CUSTOMERPHONENO=int(input("ENTER NUMBER"))
            TIPAMOUNT=int(input("ENTER TIP AMOUNT"))
            query="insert into TIP values ({},'{}',{},{})".format(SERIALNO, CUSTOMERNAME, CUSTOMERPHONENO, TIPAMOUNT)
            mycur.execute(query)
            mydb.commit()
            print("DATA INSERTED SUCCESFULLY")
        if CHOICE==10:
            SERIALNO = int(input("ENTER SERIALNO:"))
            query="delete from TIP where SERIALNO={}".format(SERIALNO)
            mycur.execute(query)
            mydb.commit()
            if mycur.rowcount>0:
                print("DATA DELETED SUCCESFULLY..")
            else:
                print("NO DATA FOUND")
                
        if CHOICE==11:
            query="select * from TIP"
            mycur.execute(query)
            x=mycur.fetchall()
            print(x)