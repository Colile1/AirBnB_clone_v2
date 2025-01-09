import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommandParamsCreate(unittest.TestCase):

    def setUp(self):
        self.cmd = HBNBCommand()
        self.cmd.prompt = ''

    def test_create_state_with_params(self):
        """Test creating a valid State object with parameters."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('State name="California"')
            output = fake_out.getvalue().strip()
            self.assertTrue(output)  # Check that an ID is printed

    def test_create_place_with_params(self):
        """Test creating a valid Place object with parameters."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('Place city_id="0001" user_id="0001" name="My_little_house" '
                              'number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 '
                              'latitude=37.773972 longitude=-122.431297')
            output = fake_out.getvalue().strip()
            self.assertTrue(output)  # Check that an ID is printed

    def test_create_invalid_class(self):
        """Test creating an object with an invalid class name."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('InvalidClass name="Test"')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_missing_class(self):
        """Test creating an object without a class name."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('')
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_parameter(self):
        """Test creating an object with an invalid parameter."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('State invalid_param')
            output = fake_out.getvalue().strip()
            self.assertIn("** invalid parameter:", output)


if __name__ == '__main__':
    unittest.main()
