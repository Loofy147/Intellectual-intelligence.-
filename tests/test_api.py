import unittest
import json
# from server.app import create_app, db
# from server.models import User, Team, TeamMembership
# from werkzeug.security import generate_password_hash
# from flask_jwt_extended import create_access_token

class ApiTestCase(unittest.TestCase):
    pass
    # def setUp(self):
    #     self.app = create_app('testing')
    #     self.app_context = self.app.app_context()
    #     self.app_context.push()
    #     db.create_all()
    #
    #     # Create a test user
    #     password_hash = generate_password_hash('password')
    #     user = User(email='test@example.com', password_hash=password_hash)
    #     db.session.add(user)
    #     db.session.commit()
    #     self.user_id = user.id
    #
    #     with self.app.test_request_context():
    #          self.access_token = create_access_token(identity=self.user_id)
    #     self.headers = {'Authorization': f'Bearer {self.access_token}'}
    #     self.client = self.app.test_client()
    #
    #
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #     self.app_context.pop()
    #
    # def test_create_team(self):
    #     """Test creating a new team."""
    #     response = self.client.post('/api/teams',
    #                              headers=self.headers,
    #                              data=json.dumps(dict(team_name='Test Team')),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Team.query.count(), 1)
    #
    # def test_get_teams(self):
    #     """Test getting teams for the current user."""
    #     self.client.post('/api/teams', headers=self.headers, data=json.dumps(dict(team_name='Test Team')), content_type='application/json')
    #     response = self.client.get('/api/teams', headers=self.headers)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.get_json()), 1)
    #
    # def test_create_compass(self):
    #     """Test creating a compass for a team."""
    #     team_res = self.client.post('/api/teams', headers=self.headers, data=json.dumps(dict(team_name='Test Team')), content_type='application/json')
    #     team_id = team_res.get_json()['team_id']
    #     response = self.client.post(f'/api/teams/{team_id}/compasses', headers=self.headers, data=json.dumps(dict(title='My Compass')), content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Team.query.get(team_id).compasses.count(), 1)

if __name__ == '__main__':
    unittest.main()
