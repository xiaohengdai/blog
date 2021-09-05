#coding: utf-8
from app.config_default import Config as DefaultConfig

class Config(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ks123456@localhost:3306/gifshow?charset=utf8'

