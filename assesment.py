import pyodbc as pyodbc  #Importing module
#ms_drivers=[x for x in pyodbc.drivers() if 'ACCESS' in x.upper()]
#print(f'MS-Access Drivers:{ms_drivers}')
#setting the driver string
drive='{Microsoft Access Driver (*.mdb, *.accdb)}'  
#setting the path of the databse in ms access
path=(r'C:\Users\azba\OneDrive\Desktop\Azba\Incubyte\incubyte\Records.accdb')

#connecting into the database
connect= pyodbc.connect(driver=drive, DBQ=path , autocommit=True)
cursor=connect.cursor()

""" c_name=input("Enter the name of the customer:")
c_id=input("Enter the customer id")
c_opendate=input("Enter the Customer open date:")
lastconsult=input("Enter the Last consult date:")
vax=input("Enter the Customer vaccine:")
doc=input("Enter the doctor cunsulted:")
state=input("Enter the Customer State:")
country=input("Enter the Customer Country:")
pin=input("Enter the pincode:")
dob=input("Enter the date of birth:")
active=input("Enter whether the Customer is active or not:")
val=(c_name,c_id,c_opendate,lastconsult,vax,doc,state,country,pin,dob,active)
cursor.execute("INSERT INTO Records_main VALUES (?,?,?,?,?,?,?,?,?,?,?)",val)
cursor.commit() """
cursor.execute('select * from Records_main')
for row in cursor.fetchall():
    for x in row:
        print(x,"\t|",end="")
    print()
