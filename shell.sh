#在数据库中生成所有声明类的表
from app import db
db.create_all()

#
flask-sqlacodegen "mssql+pyodbc://sa:123@vulkan" --tables slaveData --outfile "data.py"  --flask