# %%

# Connect SQLAlchemy to MS SQL Server Database
from sqlalchemy import create_engine
import pandas as pd

Server='DESKTOP-IK1B8NM/WERMAWIN'
Database='WERMAWIN'
Driver='ODBC Driver 11 for SQL Server'
# Database_Con='mssql+pyodbc://DESKTOP-IK1B8NM/WERMAWIN\\SQLEXPRESS/WERMAWIN?trusted_connection=yes&driver=SQL+Server+Native+Client+11.0'

HOSTNAME = '127.0.0.1'
PORT = '1433'
DATABASE = 'WERMAWIN'
USERNAME = 'ina'
PASSWORD = '123'
# dialect+driver://username:password@host:port/database
Dcon = "mssql+pyodbc://{username}:{password}@{host}:{port}/{db}?driver=SQL+Server+Native+Client+11.0&charset=utf8".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)
# Dcon='mssql+pyodbc://scott:tiger@myhost:port/WERMAWIN?driver=SQL+Server+Native+Client+11.0'
engine=create_engine(Dcon)
con=engine.connect()


df=pd.read_sql_query("Select * from [dbo].[slaveData]", con)
print(df)
#%%
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://' + 'DESKTOP-IK1B8NM/WERMAWIN' + '/' + 'WERMAWIN' + '?driver=SQL+Server'
db = SQLAlchemy(app)

class Country(db.Model):
    __tablename__ = 'example'
    id = db.Column('Country_ID', db.Integer, primary_key=True)
    code = db.Column('Country_Code', db.String)

@app.route('/test')
def test():
    allCountries = Country.query.all()
    return jsonify(allCountries)
    
'''
