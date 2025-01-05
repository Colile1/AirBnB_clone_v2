#!/usr/bin/python3
"""Unit tests for console.py"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))0  
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Test cases for HBNB console"""

    def setUp(self):
        """Set up test cases"""
        self.console = HBNBCommand()
        
    def tearDown(self):
        """Clean up after tests"""
        storage._FileStorage__objects = {}
        
    def test_create_valid(self):
        """Test create command with valid class"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) == 36)

    def test_create_missing_class(self):
        """Test create with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_create_invalid_class(self):
        """Test create with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_show_valid(self):
        """Test show command with valid input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {obj_id}")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_show_missing_class(self):
        """Test show with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_destroy_valid(self):
        """Test destroy command with valid input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy BaseModel {obj_id}")
            self.assertEqual(f.getvalue().strip(), "")

    def test_all_valid(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("all BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_update_valid(self):
        """Test update command with valid input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            obj_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            cmd = f'update BaseModel {obj_id} name "test_name"'
            self.console.onecmd(cmd)
            self.assertEqual(f.getvalue().strip(), "")

    def test_dot_notation_all(self):
        """Test dot notation for all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.all()")
            self.assertTrue(isinstance(eval(f.getvalue()), list))

    def test_dot_notation_count(self):
        """Test dot notation for count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel.count()")
            self.assertTrue(f.getvalue().strip().isdigit())

    def test_quit_command(self):
        """Test quit command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_EOF_command(self):
        """Test EOF command"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")


if __name__ == '__main__':
    unittest.main()
