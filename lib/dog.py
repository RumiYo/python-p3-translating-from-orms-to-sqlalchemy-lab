from models import Dog
from sqlalchemy import (create_engine, engine)
from sqlalchemy.orm import sessionmaker

def create_table(base, engine):
    
    db_file = '/Users/rumiyokoyama/Development/code/phase-3/python-p3-translating-from-orms-to-sqlalchemy-lab/lib/dogs.db'

    engine = create_engine(f'sqlite:///{db_file}')
    base.metadata.create_all(engine)


def save(session, dog):
   session.add(dog)
   session.commit() 

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name.like(name)).all()
    for record in query:
         return record

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).all()
    for record in query:
        return record

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name.like(name), Dog.breed == breed).all()
    for record in query:
        return record

def update_breed(session, dog, breed):
    dog.breed = breed
    session.commit()