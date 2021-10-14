# -*- coding: utf-8 -*-
#Connect via Flask_SQLAlchemy

from flask import Flask, jsonify, request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__, static_url_path='', static_folder='static')
db_URI = "mssql+pyodbc://sa:123@vulkan"
app.config['SQLALCHEMY_DATABASE_URI'] =db_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=True

# 初始化扩展，传入程序实例 app
db = SQLAlchemy(app)

# 声明模型类 建立与slaveData 表结构一致的数据表
class DataCopy(db.Model):
    __tablename__ = 'datacopy'
    __table_args__ = (
        db.Index('slaveDataSlaveId', 'slaveId', 'datEnd'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    slaveId = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    datStart = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    datEnd = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    channel1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    error = db.Column(db.Boolean, nullable=False, server_default=db.FetchedValue())
    
    # def __repr__(self):
    #     return '<Datacopy %r>' % self.username

class AndonData(db.Model):
    __tablename__ = 'andonData'
    __table_args__ = (
        db.Index('slaveDataSlaveId', 'slaveId', 'datEnd'),
    )

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    slaveId = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    datStart = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    datEnd = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    duration = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    channel1 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel2 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel3 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    channel4 = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    error = db.Column(db.Boolean, nullable=False, server_default=db.FetchedValue())

# @app.route("/")
# def index():
#     return "hello"

@app.route('/setplandata', methods=['POST'])
def setplandata():
    return render_template('setplandata.html')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/status_input', methods=['GET','POST'])
def status_input():
    return render_template('status_input.html')
# from app import AndonData, DataCopy
# dat1='2021-09-08 10：59：49'
# dat2='2021-09-08 11：20：00'

# sq1='''
#     INSERT INTO [WERMAWIN].[dbo].[Datacopy]
#     SELECT *
#     FROM [WERMAWIN].[dbo].[AndonData]
#     WHERE datEnd between '2021-09-08 10：59：49' and '2021-09-08 11：20：00'
#     '''

# result=db.engine.execute(sq1)

historys = .query.filter(History.date.between(firstDay, lastDay)).all()












