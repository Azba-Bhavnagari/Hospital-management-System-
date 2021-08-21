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
print("\t=======================================================================================")
print("\t\t\t\t\t HOSPITAL DATABASE!")
print("\t=======================================================================================\n")
session=1

#checking for the authorised user
name=input("\tEnter username:")
pas=getpass.getpass("\tEnter yout password:")
if name=="Admin" and pas=="reveal":
    print("\t=======================================================================================")
    name=name.upper()
    print("\t\t\t\t WELCOME TO THE HOSPITAL DATABASE",name,"!")
    print("\t=======================================================================================\n")
    while session==1:
        #checking for the operations the user wants to perform
        print("\t=======================================================================================\n")
        print("\tWhat Operations would you like to perform?\t\t\n")
        print("\t1)Fetch Records\n\t2)Add record\n\t3)Edit records\n\t4)Display Country Wise Records\n\t5)Log out")
        choice=int(input("\n\tEnter your choice:"))
        print("\t=======================================================================================")
        if choice==1:    #for fetching the single customer record
            name=input("\tEnter the customer name you wish to search:")
            id=input("\tEnter customer id:")
            con=input("\tEnter the country costomer belong to:")
            if con=="in" or con=="IN":
                cursor.execute("SELECT * FROM IN_db WHERE customer_name=? AND customer_id=?",name,id)
                print("\t========================================================") 
                print("\t|H|Customer_Records|Country-INDIA|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t========================================================")
            elif con=="usa" or "USA":
                cursor.execute("SELECT * FROM USA_db WHERE customer_name=? AND customer_id=?",name,id)
                print("\t========================================================") 
                print("\t|H|Customer_Records|Country-USA|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t========================================================")
            elif con=="CAN" or "can":
                cursor.execute("SELECT * FROM CAN_db WHERE customer_name=? AND customer_id=?",name,id)
                print("\t========================================================") 
                print("\t|H|Customer_Records|Country-Canada|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t========================================================")
            elif con=="UK" or "uk":
                cursor.execute("SELECT * FROM UK_db WHERE customer_name=? AND customer_id=?",name,id)
                print("\t========================================================") 
                print("\t|H|Customer_Records|Country-UK|")
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
                print("\tThere is no customer with name ",name," and id",id,"in ",con)    
        elif choice==2:  #for introducing new costomer to the family
                #getting the input for the tables
                c_name=input("\tEnter the name of the customer:")
                #c_id=input("Enter the customer id:")
                c_opendate=input("\tEnter the Customer open date:[yyyy-mm-dd]")
                lastconsult=input("\tEnter the Last consult date:[yyyy-mm-dd]")
                vax=input("\tEnter the Customer vaccine:")
                doc=input("\tEnter the doctor cunsulted:")
                state=input("\tEnter the Customer State:")
                country=input("\tEnter the Customer Country:")
                pin=input("\tEnter the pincode:")
                dob=input("\tEnter the date of birth:[yyyy-mm-dd]")
                active=input("\tEnter whether the Customer is active or not:[y,n]")
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
                elif country=="uk" or country=="UK":
                    cursor.execute("select * from UK_db")
                    id=0
                    for row in cursor.fetchall():
                        id=id+1
                    c_id=id+1
                    val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
                    cursor.execute("INSERT INTO UK_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
                    cursor.commit()
                    print("\t\tRecord inserted succesfully!")  
                elif country=="can" or country=="CAN":
                    cursor.execute("select * from CAn_db")
                    id=0
                    for row in cursor.fetchall():
                        id=id+1
                    c_id=id+1
                    val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
                    cursor.execute("INSERT INTO GER_db VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
                    cursor.commit()
                    print("\t\tRecord inserted succesfully!")   
                else:
                    print("\t\tSorry NO branches in",country)
                print("\t=======================================================================================")
        elif choice==3:  #updating the database 
            name=input("\tEnter the name of the customer you wish to update the record of:")
            id=input("\tEnter the customer's ID:")
            cou=input("\tEnter the country of the customer:")
            date=input("\tEnter the last consulted date of the customer:[yyyy-mm-dd]")
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
            elif cou=="UK" or cou=="uk":
                cursor.execute("UPDATE UK_db SET last_consulted_date=? WHERE customer_name=? AND customer_id=?",date,name,id)
                cursor.execute("UPDATE UK_db SET doctor_consulted= ? WHERE customer_name=? AND customer_id=?",doc,name,id)
                cursor.commit()
                print("\t\tRecord updated!")
            elif cou=="can" or cou=="CAN":
                cursor.execute("UPDATE CAN_db SET last_consulted_date=? WHERE customer_name=? AND customer_id=?",date,name,id)
                cursor.execute("UPDATE CAN_db SET doctor_consulted= ? WHERE customer_name=? AND customer_id=?",doc,name,id)
                cursor.commit()
                print("\t\tRecord updated!")    
        elif choice==4:  #options about the data display acc to country
            print("\tSelect the country you wish to see the data of?\n")
            print("\t1)USA")
            print("\t2)India")
            print("\t3)UK")
            print("\t4)Canada")    
            ch=int(input("\n\tEnter your choice:"))
            if ch==1:
                cursor.execute('select * from USA_db')
                print("\t=======================================================================================")
                print("\t|H|Customer_Records|Country-USA|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t=======================================================================================")
            elif ch==2:
                cursor.execute('select * from IN_db')
                print("\t=======================================================================================")
                print("\t|H|Customer_Records|Country-INDIA|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t=======================================================================================")
            elif ch==3:
                cursor.execute('select * from UK_db')
                print("\t=======================================================================================")
                print("\t|H|Customer_Records|Country-UK|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t=======================================================================================")
            elif ch==4:
                cursor.execute('select * from CAN_db')
                print("\t=======================================================================================")
                print("\t|H|Customer_Records|Country-Canada|")
                count=0
                for row in cursor.fetchall():
                    print("\t|D|",end="")
                    for x in row:
                        print(x,"\t|",end="")
                    print()
                    count=count+1
                print("\t|T|",count,"|")
                print("\t=======================================================================================")
            else:
                print("\tInvalid input!")
                print("\t=======================================================================================")
        elif choice==5:
            ask=input("\n\tAre you sure you want to log out?")
            if ask=="Y" or ask=="y":
                print("\tLogged out!")
                print("\t--------------------------------Session Ended------------------------------------------")
                print("\t=======================================================================================")
                exit()
            else:
                print()
                continue
        else:
            print("\tInvalid input!")
            print("\t=======================================================================================")
        #if the user wants to end the session 
        session=int(input("\n\tDo you want to end the session?[0/1]"))
    #ending the session
    print("\t=======================================================================================")
    print("\t------------------------------Session Terminated---------------------------------------")
else: #terminating the session as the password of user name entered is wrong
    print("\tIncorrect username or password!")
    print("\t------------------------------Session Aborted------------------------------------------")
    print("\t=======================================================================================")
    exit()

