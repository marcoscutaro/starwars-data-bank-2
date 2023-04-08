connectionCharacPlanets = db.Table('connectionCharacPlanets',
    db.Column('characters_id', db.Integer, db.ForeignKey('characters.id'), primary_key=True),
    db.Column('planets_id', db.Integer, db.ForeignKey('planets.id'), primary_key=True),
)



class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)


connectionCharacPlanets = db.relationship('Connection', secondary=connectionCharacPlanets, lazy='subquery', backref=db.backref('characters', lazy=True))

connectionCharacPlanets = db.relationship('Connection', secondary=connectionCharacPlanets, lazy='subquery', backref=db.backref('planets', lazy=True))


class Favourites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(120), db.ForeignKey('characters.id'),unique=True, nullable=False)
    planets = db.Column(db.String(80), db.ForeignKey('planets.id'), unique=False, nullable=False)
    user_id = db.Column(db.Boolean(), db.ForeignKey('user.id'), unique=False, nullable=False)
    connectionCharacPlanetsFavourites = db.relationship('Connection', secondary=connectionCharacPlanetsFavourites, lazy='subquery', backref=db.backref('favourites', lazy=True))

    def __repr__(self):
        return '<Favourites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "characters": self.characters,
            "planets": self.planets,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }