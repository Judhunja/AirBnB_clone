#!/usr/bin/python3
""" This module contains a class HBNBCommand """
import cmd


class HBNBCommand(cmd.Cmd):
    """ This initializes a class HBNBCommand """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quits if the user types in quit or crtl+D(EOF)\n """
        return True

    def do_EOF(self, line):
        """ Quits the program\n """
        return True

    def emptyline(self):
        """ Does nothing when Enter is pressed on emptyline """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
