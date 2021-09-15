#coding=utf-8
import pymssql
conn = pymssql.connect(host='127.0.0.1',user='sa',
                       password='123',database='WERMAWIN',
                      charset="utf8")
#查看连接是否成功
print (conn)
cursor = conn.cursor()
cursor.execute('SELECT * FROM [WERMAWIN].[dbo].[slaveData]')
print( cursor.fetchall() ) 