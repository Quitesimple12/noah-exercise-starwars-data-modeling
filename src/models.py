import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    userid = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = relationship("Favorites", back_populates="user")

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favoriteid = Column(Boolean, primary_key=True)
    userid = Column(Integer, ForeignKey('User.userid'))
    user = relationship("User", back_populates="favorites")
    planet_id = Column(Integer, ForeignKey('Planets.planetid'))
    planet = relationship("Planets")
    vehicle_id = Column(Integer, ForeignKey('Vehicles.vehicleid'))
    vehicle = relationship("Vehicles")
    character_id = Column(Integer, ForeignKey('Characters.characterid'))
    character = relationship("Characters")
                                              
class Planets(Base):
    __tablename__ = 'Planets'
    planetid = Column(Integer, primary_key=True)
    planetname = Column(String(250), nullable=False)
    planetdesc = Column(String(1000), nullable=False)
    planetsize = Column(Integer, primary_key=True)
    planettemp = Column(Integer, primary_key=True)
    favoriteid = Column(Boolean, default=False)

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    vehicleid = Column(Integer, primary_key=True)
    vehiclename = Column(String(250), nullable=False)
    vehicledesc = Column(String(1000), nullable=False)
    vehiclesize = Column(Integer, primary_key=True)
    vehiclespeed = Column(Integer, primary_key=True)
    favoriteid = Column(Boolean, default=False)

class Characters(Base):
    __tablename__ = 'Characters'
    characterid = Column(Integer, primary_key=True)
    charactername = Column(String(250), nullable=False)
    characterdesc = Column(String(1000), nullable=False)
    characterheight = Column(Integer, primary_key=True)
    characterweight = Column(Integer, primary_key=True)
    favoriteid = Column(Boolean, default=False)





## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
