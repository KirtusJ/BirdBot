from util import database as db_config

import sys, os

import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class Database():
	def __init__(self):
		pass
	def __initdb__(self, env):
		try:
			print("Initializing Database in {env} mode\n".format(env=env['mode']))
			db = db_config(env)
			self.engine = create_engine(db["link"])
			self.Base = declarative_base()
			self.Session = sessionmaker()
			self.Session.configure(bind=self.engine)
			self.session = self.Session()
			self.base = self.Base()
		except Exception as e:
			print(e)


database = Database()

