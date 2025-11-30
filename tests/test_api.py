import unittest
import json
from server.app import create_app, db
from server.models import User, Team, TeamMembership, Compass
from werkzeug.security import generate_password_hash

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create a test user
            hashed_password = generate_password_hash("password", method='pbkdf2:sha256')
            self.user = User(username="testuser", email="test@example.com", password_hash=hashed_password)
            db.session.add(self.user)
            db.session.commit()

            # Get an auth token
            response = self.client.post(
                '/api/auth/login',
                data=json.dumps({"username": "testuser", "password": "password"}),
                content_type='application/json'
            )
            self.token = response.get_json()['access_token']
            self.headers = {'Authorization': f'Bearer {self.token}'}

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_team(self):
        response = self.client.post(
            '/api/teams',
            headers=self.headers,
            data=json.dumps({"team_name": "Test Team", "company_name": "Test Co"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_get_teams(self):
        with self.app.app_context():
            team = Team(team_name="Test Team")
            db.session.add(team)
            membership = TeamMembership(user=self.user, team=team)
            db.session.add(membership)
            db.session.commit()

        response = self.client.get('/api/teams', headers=self.headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)

    def test_create_compass(self):
        with self.app.app_context():
            team = Team(team_name="Test Team")
            db.session.add(team)
            membership = TeamMembership(user=self.user, team=team)
            db.session.add(membership)
            db.session.commit()
            self.team_id = team.id

        response = self.client.post(
            f'/api/teams/{self.team_id}/compasses',
            headers=self.headers,
            data=json.dumps({"q1": "Test"}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
