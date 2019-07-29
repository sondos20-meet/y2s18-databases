from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__="article"
	article_id = Column(Integer, primary_key =True)
	name = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.
	def __repr__(self):
		return("article name: {}\n"
			"article topic: {}\n "
			"article rating: {}\n").format(

			self.name, self.topic, self.rating)
print(repr(Knowledge.__tablename__))
x = Knowledge(name =" michael jaxon is alive", topic= "trues")
print(x)