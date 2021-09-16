# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class SlaveDatum(db.Model):
    __tablename__ = 'slaveData'
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
