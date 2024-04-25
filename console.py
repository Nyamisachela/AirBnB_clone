#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it to the file and prints the id"""
        if not line:
            print("** class name missing **")
            return
        try:
            obj = eval(f"{line}()")
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return
        class_name, id = args[0], args[1]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{id}"
        all_objects = storage.all()
        if instance_key in all_objects:
            print(all_objects[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) < 2:
            print("** class name missing **" if len(args) == 0 else "** instance id missing **")
            return
        class_name, id = args[0], args[1]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        instance_key = f"{class_name}.{id}"
        all_objects = storage.all()
        if instance_key in all_objects:
            del all_objects[instance_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Shows all instances of a class, or if no class name is provided, all instances in storage"""
        class_name = line.strip()
        if class_name and class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        all_objects = storage.all()
        print([str(obj) for obj_id, obj in all_objects.items() if class_name == "" or obj_id.startswith(class_name + ".")])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj_id = f"{args[0]}.{args[1]}"
        if obj_id in storage.all():
            obj = storage.all()[obj_id]
            if len(args) == 4:
                setattr(obj, args[2], args[3].strip('"'))
                obj.save()
            else:  # Handling dictionary updates
                for i in range(2, len(args), 2):
                    setattr(obj, args[i], args[i+1].strip('"'))
                obj.save()
        else:
            print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

