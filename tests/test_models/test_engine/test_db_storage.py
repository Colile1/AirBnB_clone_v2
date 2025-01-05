#!/usr/bin/python3
"""Test Database storage"""
import unittest
import models
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'Skip if not using db')
class TestDBStorage(unittest.TestCase):
    """Test the database storage class"""
    
    def setUp(self):
        """Set up test environment"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            self.storage = DBStorage()
            self.storage.reload()
    
    def test_all_returns_dict(self):
        """Test that all returns a dictionary"""
        self.assertEqual(dict, type(self.storage.all()))
    
    def test_new(self):
        """Test that new adds an object to the database"""
        state = State(name="California")
        self.storage.new(state)
        self.storage.save()
        key = f"{state.__class__.__name__}.{state.id}"
        self.assertIn(key, self.storage.all())
