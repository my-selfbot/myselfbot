import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'


	id = Column(Integer, primary_key=True)
	username = Column(String, nullable=False)
	password = Column(String)
	full_name = Column(String, nullable=False)
	is_verified = Column(Boolean)

class Friendship(Base):
	__tablename__ = 'friendships'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	user = relationship(User)
	profile_id = Column(Integer, ForeignKey('users.id'))
	profile = relationship(User)
	started_at = Column(Date)
	invited_at = Column(Date)
	followed_at = Column(Date)
	unfollowed_at = Column(Date)
	following_at = Column(Date)
	unfollwing_at = Column(Date)
	first_interaction = Column(Date)
	last_interaction = Column(Date)
	n_likes = Column(Integer)
	n_comments = Column(Integer)
	n_replay = Column(Integer)

def create_db():
	# Create an engine that stores data in the local directory's
	# sqlalchemy_example.db file.
	engine = create_engine('sqlite:///aloha.db')
	 
	# Create all tables in the engine. This is equivalent to "Create Table"
	# statements in raw SQL.
	Base.metadata.create_all(engine)