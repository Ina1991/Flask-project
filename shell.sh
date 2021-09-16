# 在数据库中生成所有声明类的表
# 打开 Python Shell 使用的是 flask shell命令，而不是 python。使用这个命令启动的 Python Shell 激活了“程序上下文”，它包含一些特殊变量，这对于某些操作是必须的（比如上面的 db.create_all()调用）。请记住，后续的 Python Shell 都会使用这个命令打开。
from app import db
db.create_all()

#使用flask-sqlacodegen自动生成model
flask-sqlacodegen "mssql+pyodbc://sa:123@vulkan" --tables slaveData --outfile "data.py"  --flask