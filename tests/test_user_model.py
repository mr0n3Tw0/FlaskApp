import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(password='test')
        self.assertTrue(u.password_hash is not None)

    def test_no_pasword_getter(self):
        u = User(password='test')
        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(password='test')
        self.assertTrue(u.verify_password('test'))
        self.assertFalse(u.verify_password('random str'))

    def test_password_salts_are_random(self):
        u = User(password='test')
        u2 = User(password='test')
        self.assertTrue(u.password_hash != u2.password_hash)