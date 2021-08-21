import pyodbc #Importing module
import getpass
"""ms_drivers=[x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
print(f'MS-Access Drivers:{ms_drivers}')"""

#setting the driver string

drive='{Microsoft Access Driver (*.mdb, *.accdb)}'  
#setting the path of the databse in ms access

path=(r'C:\Users\azba\OneDrive\Desktop\Azba\Incubyte\incubyte\Records.accdb')
#connecting into the database

connect= pyodbc.connect(driver=drive, DBQ=path , autocommit=True)
cursor=connect.cursor()

#specifying option about add display the data
print("\t========================================================")
print("\t\t\t WELCOME TO THE HOSPITAL DATABASE!\n")
session=1
name=input("\tEnter username:")
pas=getpass.getpass("\tEnter yout password:")
if name=="Admin" and pas=="reveal":
    while session==1:
        print("\tWhat Operations would you like to perform?\t\t\n")
        print("\t1)Add record\n\t2)Edit records\n\t3)Display records")
        choice=int(input("\n\tEnter your choice:"))
        print("\t========================================================")
        if choice==1:
                #getting the input for the tables
                c_name=input("\tEnter the name of the customer:")
                #c_id=input("Enter the customer id:")
                c_opendate=input("\tEnter the Customer open date:")
                lastconsult=input("\tEnter the Last consult date:")
                vax=input("\tEnter the Customer vaccine:")
                doc=input("\tEnter the doctor cunsulted:")
                state=input("\tEnter the Customer State:")
                country=input("\tEnter the Customer Country:")
                pin=input("\tEnter the pincode:")
                dob=input("\tEnter the date of birth:")
                active=input("\tEnter whether the Customer is active or not:");
                #val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
                #bifergating data according to the country it belongs
                if  country=="USA" or country=="usa":
                    cursor.execute("select * from USA_db")
                    id=0
                    for row in cursor.fetchall():
                        id=id+1
                    c_id=id+1
                    val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
                    cursor.execute("INSERT INTO USA_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
                    cursor.commit()
                    print("\t\tRecord inserted succesfully!")
                elif country=="in" or country=="IN":
                    cursor.execute("select * from IN_db")
                    id=0
                    for row in cursor.fetchall():
                        id=id+1
                    c_id=id+1
                    val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
                    cursor.execute("INSERT INTO IN_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
                    cursor.commit()
                    print("\t\tRecord inserted succesfully!")
                        
                else:
                    print("\t\tSorry NO branches in",country)
                print("\t========================================================") 
        elif choice==2:
            name=input("\tEnter the name of the customer you wish to update the record of:")
            id=input("\tEnter the customer's ID:")
            cou=input("\tEnter the country of the customer:")
            date=input("\tEnter the last consulted date of the customer:")
            doc=input("\tEnter the last consulted Doctor:")
            if cou=="in" or cou=="IN":
                cursor.execute("UPDATE IN_db SET last_consulted_date=? WHERE customer_name=? AND customer_id=?",date,name,id)
                cursor.execute("UPDATE IN_db SET doctor_consulted= ? WHERE customer_name=? AND customer_id=?",doc,name,id)
                cursor.commit()
                print("\t\tRecord updated!")
            elif cou=="USA" or cou=="usa":
                cursor.execute("UPDATE USA_db SET last_consulted_date=? WHERE customer_name=? AND customer_id=?",date,name,id)
                cursor.execute("UPDATE USA_db SET doctor_consulted= ? WHERE customer_name=? AND customer_id=?",doc,name,id)
                cursor.commit()
                print("\t\tRecord updated!")
        elif choice==3:
            #options about the data display acc to country
            print("\tSelect the country you wish to see the data of?\n")
            print("\t1)USA")
            print("\t2)India")
            ch=int(input("\n\tEnter your choice:"))
            if ch==1:
                cursor.execute('select * from USA_db')
                print("\t========================================================") 
                print("\t|H|Customer_Records|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t========================================================")
            elif ch==2:
                cursor.execute('select * from IN_db')
                print("\t========================================================") 
                print("\t|H|Customer_Records|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t========================================================")    
            else:
                print("\tInvalid input!")
                print("========================================================")
                    
        else:
            print("\tWe dont provide sevices in",country)
        session=int(input("\n\tDo you want to end the session?[0/1]"))
    #ending the session
    print("\t========================================================")
    print("\t---------------------Session over----------------------")
else:
    print("\tIncorrect username or password!")
    print("\t---------------------Session Aborted----------------------")
    exit()

