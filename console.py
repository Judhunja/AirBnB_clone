#!/usr/bin/python3
""" This module contains a class HBNBCommand """
import cmd
from engine.file_storage import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This initializes a class HBNBCommand"""

    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quits if the user types in quit or crtl+D(EOF)\n"""
        return True

    def do_EOF(self, line):
        """Quits the program\n"""
        return True

    def emptyline(self):
        """Does nothing when Enter is pressed on emptyline"""
        pass

    def do_create(self, name):
        """Creates a new instance of BaseModel, saves it to a JSON file
        and prints the id
        """
        if name is None:
            print("** class name missing **")
        if not name:
            print("** class doesn't exist **")
        name = BaseModel()
        storage.save(name)
        print(name.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
