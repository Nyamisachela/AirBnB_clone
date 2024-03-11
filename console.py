#!/usr/bin/env python

import cmd

class HBNBCommand(cmd.Cmd):
    """Console for ALX Airbnb Clone project"""
    prompt = "Mina> "

    def do_EOF(self, line):
        """Quit the program"""
        return True

    def do_quit(self, line):
        """Quit the program"""
        return True

    def help_quit(self):
        """Print help for quit command"""
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

