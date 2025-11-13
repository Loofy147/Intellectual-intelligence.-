from flask_sqlalchemy import SQLAlchemy
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(120), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    teams = db.relationship('Team', secondary='team_memberships', back_populates='members')

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_name = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    members = db.relationship('User', secondary='team_memberships', back_populates='teams')
    compasses = db.relationship('Compass', backref='team', lazy=True)

class TeamMembership(db.Model):
    __tablename__ = 'team_memberships'
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), primary_key=True)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey('teams.id'), primary_key=True)
    role = db.Column(db.String(50), nullable=False, default='member') # e.g., 'owner', 'member'

class Compass(db.Model):
    __tablename__ = 'compasses'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    team_id = db.Column(UUID(as_uuid=True), db.ForeignKey('teams.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False, default='Untitled Compass')
    data = db.Column(JSONB, nullable=False, default=lambda: {})
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
