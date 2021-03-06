import os
import sys
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey,ForeignKeyConstraint, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, MetaData


Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250), nullable=True)

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)

    @property
    def serialize(self):
    	"""Return object data in easily serializeable format"""
    	return {
    		'name': self.name,
    		'id': self.id,
    	}

class Book(Base):
	__tablename__ = 'book'

	id = Column(Integer, primary_key=True)
	title = Column(String(250), nullable=False)
	author = Column(String(250), nullable=False)
	description = Column(String(2000), nullable=False)
	category_name = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)
	#__table_args__ = (ForeignKeyConstraint([category_name],[Category.name]), {})

	@property
	def serialize(self):
		"""Return object data in easliy serializeable format"""
		return {
			'title': self.title,
			'author': self.author,
			'description': self.description,
			'category_name': self.category_name,
			'id': self.id,
		}

engine = create_engine('postgresql://catalog:catalog123@localhost/catalog')


Base.metadata.create_all(engine)
