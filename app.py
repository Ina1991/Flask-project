#Connect via Flask_SQLAlchemy

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__, static_url_path='', static_folder='static')
db_URI = "mssql+pyodbc://sa:123@vulkan"
app.config['SQLALCHEMY_DATABASE_URI'] =db_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

# 声明模型类
class Role(db.Model):
    __tablename__ = "my_table3"    #设置表名
    id = db.Column(db.INTEGER,primary_key=True)    #设置字段，以及属性
    name = db.Column(db.String(10),nullable=False)

@app.route("/")
def index():
    return "hello"

#from app import db
db.create_all()
