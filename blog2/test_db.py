import pyodbc

server = ""
database = ""
username = ""
password = ""

print("DB CONNECT ATTEMPT")
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0]) 
        row = cursor.fetchone()
    print("SUCCESS")
except Exception as e:
    print ("Error: " + str(e))