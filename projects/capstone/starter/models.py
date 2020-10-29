from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer, DateTime
from flask import json, jsonify


db = SQLAlchemy()

class Movie(db.Model):
  __tablename__ = 'Movie'
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String)
  release_date = db.Column(db.DateTime)
  actor_id = db.Column(db.ForeignKey('Actor.id'))

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

class Actor(db.Model):
  __tablename__ = 'Actor'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String)
  age = db.Column(db.Integer)
  gender = db.Column(db.String)
  movies = db.relationship('Movie', backref='actor')

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender



