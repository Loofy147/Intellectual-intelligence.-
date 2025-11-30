from .app import db
import uuid

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.username}>'

class Team(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    team_name = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(100))

    def __repr__(self):
        return f'<Team {self.team_name}>'

class TeamMembership(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    team_id = db.Column(db.String(36), db.ForeignKey('team.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('teams', lazy=True))
    team = db.relationship('Team', backref=db.backref('users', lazy=True))

class Compass(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    team_id = db.Column(db.String(36), db.ForeignKey('team.id'), nullable=False)
    team = db.relationship('Team', backref=db.backref('compasses', lazy=True))
    # The Pragmatic Compass fields
    q1 = db.Column(db.Text)
    q2 = db.Column(db.Text)
    q3 = db.Column(db.Text)
    ac1 = db.Column(db.Text)
    ac2 = db.Column(db.Text)
    le1 = db.Column(db.Text)
    le2 = db.Column(db.Text)
    le3 = db.Column(db.Text)
