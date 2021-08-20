import pyodbc #Importing module
#ms_drivers=[x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
#print(f'MS-Access Drivers:{ms_drivers}')
#setting the driver string
drive='{Microsoft Access Driver (*.mdb, *.accdb)}'  
#setting the path of the databse in ms access
path=(r'C:\Users\azba\OneDrive\Desktop\Azba\Incubyte\incubyte\Records.accdb')

#connecting into the database
connect= pyodbc.connect(driver=drive, DBQ=path , autocommit=True)
cursor=connect.cursor()
print("========================================================")
print("Enter the your choice:")
print("1)Add record\n2)Display records")
choice=int(input())
print("========================================================")
if choice==1:
        #getting the input for the tables
        c_name=input("Enter the name of the customer:")
        c_id=input("Enter the customer id:")
        c_opendate=input("Enter the Customer open date:")
        lastconsult=input("Enter the Last consult date:")
        vax=input("Enter the Customer vaccine:")
        doc=input("Enter the doctor cunsulted:")
        state=input("Enter the Customer State:")
        country=input("Enter the Customer Country:")
        pin=input("Enter the pincode:")
        dob=input("Enter the date of birth:")
        active=input("Enter whether the Customer is active or not:");
        val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
        if  country=="USA" or country=="usa":
            cursor.execute("INSERT INTO USA_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
            cursor.commit()
            print("Record inserted succesfully!")
        elif country=="in" or country=="IN":
            cursor.execute("INSERT INTO IN_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
            cursor.commit()
            print("Record inserted succesfully!")
                
        else:
            print("Sorry NO branches in",country)
            
elif choice==2:
    print("Which county records you want to display?")
    print("1)USA")
    print("2)India")
    ch=int(input())
    if ch==1:
        cursor.execute('select * from USA_db')
        for row in cursor.fetchall():
            for x in row:
                print(x,"\t|",end="")
            print()
    elif ch==2:
        cursor.execute('select * from IN_db')
        for row in cursor.fetchall():
            for x in row:
                print(x,"\t|",end="")
            print()
            
    else:
        print("Invalid input!")
            
else:
    print("We dont provide sevices in",country)
    


"""
cursor.execute('select * from USA_db')
for row in cursor.fetchall():
    for x in row:
        print(x,"\t |",end="")
    print()
"""
