from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(80), unique=True, nullable=False)
    characters = db.relationship('Characters', backref='user')    
    planets = db.relationship('Planets', backref='user')    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }




class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.Boolean(120), unique=False, nullable=False)
    hair_color = db.Column(db.Boolean(120), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    birth_year = db.Column(db.String(120), unique=False, nullable=False)
    gender = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.status,
            "mass": self.species,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.Boolean(120), unique=False, nullable=False)
    diameter = db.Column(db.Boolean(120), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)
    population = db.Column(db.String(120), unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
        }


class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(120), db.ForeignKey('characters.id'),unique=True, nullable=False)
    planets = db.Column(db.String(80), db.ForeignKey('planets.id'), unique=False, nullable=False)
    user_id = db.Column(db.Boolean(), db.ForeignKey('user.id'), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "characters": self.characters,
            "planets": self.planets,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }