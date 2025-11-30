import unittest
import json
from server.app import create_app, db
from server.models import User
from werkzeug.security import generate_password_hash

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register(self):
        response = self.client.post(
            '/api/auth/register',
            data=json.dumps({
                "username": "testuser",
                "email": "test@example.com",
                "password": "password"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        with self.app.app_context():
            hashed_password = generate_password_hash("password", method='pbkdf2:sha256')
            user = User(username="testuser", email="test@example.com", password_hash=hashed_password)
            db.session.add(user)
            db.session.commit()

        response = self.client.post(
            '/api/auth/login',
            data=json.dumps({
                "username": "testuser",
                "password": "password"
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

if __name__ == '__main__':
    unittest.main()
