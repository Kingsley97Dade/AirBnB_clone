#!/usr/bin/python3

"""Unnitest for console
"""

import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.console.preloop()

    def tearDown(self):
        self.console.postloop()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, command):
        self.console.onecmd(command)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_show_destroy_all_update_commands(self):
        storage.reset()

        # Create
        expected_output = "f1r57-1n574nc3\n"
        self.assert_stdout(expected_output, "create BaseModel")
        obj = storage.all()['BaseModel.f1r57-1n574nc3']

        # Show
        expected_output = str(obj) + '\n'
        self.assert_stdout(expected_output, "show BaseModel {}".format(obj.id))

        # Destroy
        self.assert_stdout("", "destroy BaseModel {}".format(obj.id))
        self.assertNotIn(obj, storage.all().values())

        # All
        obj1 = BaseModel()
        obj2 = BaseModel()
        expected_output = "[{}, {}]\n".format(str(obj1), str(obj2))
        self.assert_stdout(expected_output, "all BaseModel")

        # Update
        self.assert_stdout(
            "",
            'update BaseModel {} name "New Name"'.format(obj1.id)
        )
        updated_obj = storage.all()['BaseModel.' + obj1.id]
        self.assertEqual(updated_obj.name, "New Name")

    def test_invalid_commands(self):
        storage.reset()

        # Invalid create command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "create InvalidClass")

        # Invalid show command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "show InvalidClass")

        # Invalid destroy command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "destroy InvalidClass")

        # Invalid all command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "all InvalidClass")

        # Invalid update command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "update InvalidClass")

    def test_empty_line_quit_commands(self):
        # Empty line
        expected_output = ""
        self.assert_stdout(expected_output, "")

        # Quit command
        self.assertTrue(self.console.onecmd("quit"))

    def test_help_commands(self):
        expected_output = "Quit command to exit the program\n"
        self.assert_stdout(expected_output, "help quit")


if __name__ == '__main__':
    unittest.main()
