import unittest
import json
# from server.app import create_app, db
# from server.models import User
# from werkzeug.security import generate_password_hash

class AuthTestCase(unittest.TestCase):
    pass
    # def setUp(self):
    #     self.app = create_app('testing')
    #     self.app_context = self.app.app_context()
    #     self.app_context.push()
    #     db.create_all()
    #     self.client = self.app.test_client()
    #
    # def tearDown(self):
    #     db.session.remove()
    #     db.drop_all()
    #     self.app_context.pop()
    #
    # def test_registration(self):
    #     """Test user registration."""
    #     response = self.client.post('/api/auth/register',
    #                              data=json.dumps(dict(email='test@example.com', password='password')),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 201)
    #
    # def test_login(self):
    #     """Test user login."""
    #     password_hash = generate_password_hash('password')
    #     user = User(email='test@example.com', password_hash=password_hash)
    #     db.session.add(user)
    #     db.session.commit()
    #
    #     response = self.client.post('/api/auth/login',
    #                              data=json.dumps(dict(email='test@example.com', password='password')),
    #                              content_type='application/json')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('access_token', response.get_json())

if __name__ == '__main__':
    unittest.main()
