from OrangeDB import Orange
from unittest import TestCase
import unittest


class TestOrange(TestCase):

    def create_db(self):
        """ create a new database """
        db = Orange('tests.orng', auto_dump=False)
        db.clear()
        return db

    def test_set_get(self):
        """ Test get and set """
        db = self.create_db()
        db.set('name', 'shayan')
        db.set('user', 'username')
        db.setnx('user', 'new_user')

        self.assertEqual(db.get('name'), 'shayan')
        self.assertEqual(db['name'], 'shayan')
        self.assertEqual(db.get('username', 'not_set'), 'not_set')
        self.assertNotEqual(db.get('user'), 'new_user')

    def test_delete_has(self):
        """ Test delete methods """
        db = self.create_db()
        db.set('name', 'Foo')
        db.set('user', 'Fee')

        self.assertTrue(db.has('name'))
        self.assertTrue(db.has('user'))

        db.delete('name')
        del db['user']

        self.assertIsNone(db.get('name'))
        self.assertIsNone(db.get('user'))

    def test_clear(self):
        """ Test the clear function """
        db = self.create_db()
        db.set('numbers', {1: 'one', 2: 'two'})
        db.set('values', [1, 2, 3, 4])
        db.set('name', 'foo')

        db.clear()
        self.assertEqual(db.copy(), dict())

    def test_incrby_pop(self):
        """ Test incrby function and pop """
        db = self.create_db()
        db.set('age', 1)
        db.incrby('age', 5)

        self.assertTrue(db.has('age'))
        self.assertEqual(db['age'], 6)

        age = db.pop('age')
        self.assertEqual(age, 6)
        self.assertFalse(db.has('age'))

    def test_getm(self):
        """ Test the getm method """
        db = self.create_db()
        db.set(1, 'one')
        db.set(3, 'three')
        db.set(4, 'four')

        result = db.getm(1, 2, 3, 4, default='None')
        exp = ['one', 'None', 'three', 'four']
        self.assertEqual(result, exp)

        result = db.getm(1, 2, 3, 4)
        exp = ['one', None, 'three', 'four']
        self.assertEqual(result, exp)

    def test_keys_values_items(self):
        """ Test keys, values, items methods """
        db = self.create_db()
        db.set('first', 'John')
        db.set('last', 'Doe')

        keys = sorted(list(db.keys()))
        keys_exp = sorted(['first', 'last'])

        values = sorted(list(db.values()))
        values_exp = sorted(['John', 'Doe'])

        self.assertEqual(keys, keys_exp)
        self.assertEqual(values, values_exp)

        items = db.items()
        items_exp = [('first', 'John'), ('last', 'Doe')]

        for item in db.items():
            self.assertTrue(item in items_exp)

    def test_len_contain(self):
        """ Test __len__ and __contains__ """
        db = self.create_db()
        db.set('name', 'Steve')
        db.set('email', 'Steve@apple.com')

        self.assertEqual(len(db), 2)
        self.assertTrue('name' in db)


if __name__ == "__main__":
    unittest.main()
