import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    name = Column( String(50))
    rotation_period = Column( Integer , nullable=False)
    orbital_period = Column( Integer, nullable=False)
    diameter = Column( Integer, nullable=False)
    climate = Column( String(200), nullable=False)
    gravity = Column( String(200), nullable=False)
    terrain = Column( String(200), nullable=False)
    surface_water = Column( Integer, nullable=False)
    population = Column( Integer, nullable=False)
    url = Column( String(200), nullable=False)

class People(Base):
    __tablename__ = 'People'
    id = Column( Integer, primary_key=True)
    name = Column( String(50), nullable=True)
    height = Column( Integer, nullable=False)
    mass = Column( Integer, nullable=False)
    hair_color = Column( String(200), nullable=False)
    skin_color = Column( String(200), nullable=False)
    eye_color = Column( String(200), nullable=False)
    birth_year = Column( String(200), nullable=False)
    gender = Column( String(200), nullable=False)
    homeworld = Column( String(200), nullable=False)
    url = Column( String(200), nullable=False)


class Starships(Base):
    __tablename__ = 'Starships'
    id = Column( Integer, primary_key=True)
    name = Column( String(50), nullable=True)
    model = Column( String(200), nullable=False)
    manufacturer = Column( String(200), nullable=False)
    cost_in_credits = Column( Float, nullable=False)
    length = Column( Float, nullable=False)
    max_atmosphering_speed = Column( String(200), nullable=False)
    crew = Column( Float, nullable=False)
    passengers = Column( Integer, nullable=False)
    cargo_capacity = Column( Float, nullable=False)
    consumables = Column( String(200), nullable=False)
    hyperdrive_rating = Column( Float, nullable=False)
    MGLT = Column( Integer, nullable=False)
    url = Column( String(200), nullable=False)


class Species(Base):
    __tablename__ = 'Species'
    id = Column( Integer, primary_key=True)
    name = Column( String(50), nullable=True)
    classification = Column( String(200), nullable=False)
    designation = Column( String(200), nullable=False)
    average_height = Column( Integer, nullable=False)
    skin_colors = Column( String(200), nullable=False)
    hair_colors = Column( String(200), nullable=False)
    eye_colors = Column( String(200), nullable=False)
    average_lifespan = Column( Integer, nullable=False)
    homeworld = Column( String(200), nullable=False)
    language = Column( String(200), nullable=False)
    url = Column( String(200), nullable=False)


class Users(Base):
    __tablename__ = 'Users'
    id = Column( Integer, primary_key=True)
    name = Column( String(200), nullable=False)
    password = Column( String(22), nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    favoriteid = Column( Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('Users.id'))
    type = Column( String(15), nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')