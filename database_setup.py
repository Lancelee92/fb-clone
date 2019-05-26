import os
import sysconfig
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name
        }

engine = create_engine('postgresql://fb:password@localhost/facebook')
Base.metadata.create_all(engine)