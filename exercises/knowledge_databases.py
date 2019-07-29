from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(name, topic, rating):
	article_object = Knowledge(
	name=name,
	topic=topic,
	rating=rating)
	session.add(article_object)
	session.commit()
add_article("Demon Cat","IDK",9)


def query_all_articles():
	article= session.query( Knowledge).all()
	return article

print(query_all_articles())

def query_article_by_topic(their_topic):
	article= session.query(Knowledge).filter_by(
		topic = their_topic).first()
	return article
#print(query_article_by_topic("IDK"))
	

def delete_article_by_topic(topic):
	session.query(Knowledge).filter_by(
		topic=topic).delete()
	session.commit()
#delete_article_by_topic("IDK")

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()
#delete_all_articles()

def edit_article_rating(topic,uprating):
	article_object = session.query(
		Knowledge).filter_by(
		 topic=topic).first()
	article_object.rating = uprating
	session.commit()

edit_article_rating("IDK",5)


