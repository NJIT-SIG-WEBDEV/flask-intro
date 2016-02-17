from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

import keys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = keys.get_mysql_uri()

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('sig_ls', MigrateCommand)

class Links(db.Model):

	__tablename__ = "links"

	id = db.Column(db.Integer, primary_key=True)
	original = db.Column(db.String(255))

	def __init__(self, original):
		self.original = original

if __name__ == "__main__":
	manager.run()
