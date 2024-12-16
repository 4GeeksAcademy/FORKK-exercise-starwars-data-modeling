import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Tabla intermedia para la relación muchos-a-muchos entre Usuario y Favoritos
# Favoritos puede ser tanto planetas como personajes
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)

    # Relación con la tabla Usuario
    usuario = relationship('Usuario', back_populates='favoritos')
    # Relación con la tabla Planeta
    planeta = relationship('Planeta', back_populates='favoritos')
    # Relación con la tabla Personaje
    personaje = relationship('Personaje', back_populates='favoritos')

# Tabla Usuario
class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    fecha_subscripcion = Column(DateTime, nullable=False, default=func.now()) #Default para DateTime
    # Relación con la tabla Favorito
    favoritos = relationship('Favorito', back_populates='usuario')

# Tabla Planeta
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    clima = Column(String(250), nullable=False)
    terreno = Column(String(250), nullable=False)

    # Relación inversa con la tabla Favorito
    favoritos = relationship('Favorito', back_populates='planeta')

# Tabla Personaje
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    genero = Column(String(250), nullable=False)
    altura = Column(String(50), nullable=True)
    peso = Column(String(50), nullable=True)

    # Relación inversa con la tabla Favorito
    favoritos = relationship('Favorito', back_populates='personaje')


# Render del diagrama
render_er(Base, 'diagram.png')
