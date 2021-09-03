import pyodbc

cnxn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=IP ADDRESS;'
    'UID=sa;'
    'PWD=PASSWORD;'
    'DATABASE=DBNAME;'
)

cursor = cnxn.cursor()
cursor.execute('SELECT * FROM Agent_Targeting_Rule')
for row in cursor:
    print(row)
print()
for row in cursor.columns(table='Agent_Targeting_Rule'):
    print (row.column_name)
    #print(row)



#print (row.column_name)

#column_data = cursor.columns(table=Agent_Targeting_Rule, catalog=pod_awdb, schema='dbo').fetchall()
#print(column_data)

print()
#print the total number of rows returned
#might be print up the row itself
print(len(row))
#thought this was number of row but it is always 1
print(cursor.arraysize)
#always -1
print(cursor.rowcount)

tepvar = cursor.fetchall()
rowcount = len(tepvar)
print(rowcount)


cnxn.close()