#coding=utf-8
#Connect via pymssql

# import pymssql
# conn = pymssql.connect(host='127.0.0.1',user='sa',
#                        password='123',database='WERMAWIN',
#                       charset="utf8")
# #查看连接是否成功
# print (conn)
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM [WERMAWIN].[dbo].[slaveData]')
# print( cursor.fetchall() ) 

#Connect via pyodbc 
# import pyodbc 
# conn = pyodbc.connect(r'DRIVER={SQL Server Native Client 11.0};SERVER=127.0.0.1,1433;DATABASE=WERMAWIN;UID=sa;PWD=123')

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM [WERMAWIN].[dbo].[slaveData]')

# for row in cursor:
#     print(row)










