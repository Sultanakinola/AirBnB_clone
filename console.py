#!/usr/bin/python3
"""
The `console` implements the HBNB command
line interface which will be used for our
`BaseModels call`.
"""


import cmd
import models
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Implements CLI for our class.
    """
    prompt = "(hbnb) "
    cls = {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}

    def emptyline(self):
        """Implements emptyline"""
        pass

    def help_EOF(self):
        """Displays help info for EOF command"""
        print("\nQuits the program on EOF character\n")

    def help_quit(self):
        """Dispays help info for quit command"""
        print("\nQuits the program\n")

    def help_help(self):
        """Displays help info of a command"""
        print("\nDisplays help info of a command\n")

    def do_quit(self, line):
        """Quits the CLI on quit"""
        return True

    def do_EOF(self, line):
        """exits the CLI on EOF"""
        return True

    def do_help(self, arg):
        """Handler for help methods"""
        if not arg:
            print("\nDocumented commands (type help <topic>")
            print("======================================")
            print("EOF  help  quit\n")

        else:
            try:
                func = getattr(self, "help_" + arg)
            except AttributeError:
                print("No help available for", arg)
            else:
                func()

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.

        Ex: $ create BaseModel

        Args:
            line - The CLI argument string
        """
        cls_name = self.parseline(line)[0]
        if not cls_name:
            print("** class name missing **")
        else:
            if cls_name in HBNBCommand.cls:
                obj = eval(cls_name)()
                obj.save()
                print(obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance based
        on the class name and id.

        Ex: $ show BaseModel 1234-1234-1234

        Args:
            line - The CLI argument string
        """
        cls_name = self.parseline(line)[0]
        arg_id = self.parseline(line)[1]
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif not arg_id:
            print("** instance id missing **")
        else:
            key = cls_name + "." + arg_id
            objs = storage.all().get(key)
            if not objs:
                print("** no instance found **")
            else:
                print(objs)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.

        Args:
            line - The CLI argument string
        """
        cls_name = self.parseline(line)[0]
        arg_id = self.parseline(line)[1]
        if not cls_name:
            print("** class name missing **")
        elif cls_name not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif not arg_id:
            print("** instance id missing **")
        else:
            key = cls_name + "." + arg_id
            objs = storage.all().get(key)
            if not objs:
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances/objects based or
        not on the class name.

        Ex: $ all BaseModel
        Ex: $ all

        Args:
            line - The CLI argument string
        """
        cls_name = self.parseline(line)[0]
        objs = storage.all()

        if not cls_name:
            print([str(objs[obj]) for obj in objs])
        elif cls_name in HBNBCommand.cls:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(cls_name)])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance/object based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file).

        Args:
            line - The CLI argument string
        """
        args = line.split()
        if len(args) >= 4:
            key = args[0] + "." + args[1]
            arg_type = type(eval(args[3]))
            arg3 = args[3]
            arg3 = arg3.strip("'")
            arg3 = arg3.strip('"')
            obj = storage.all()[key]
            setattr(obj, args[2], arg_type(arg3))
            obj.save()
        elif len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif ("{}.{}".format(args[0], args[1])) not in storage.all().keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        else:
            print("** value missing **")

    def get_obj(self, instance=""):
        """Gets the instance of a class"""
        objs = storage.all()

        if instance:
            key = objs.keys()
            return([str(v) for k, v in objs.items() if k.startswith(instance)])
        return([str(v) for k, v in objs.items()])

    def default(self, line):
        """Executes methods that are not defined"""
        if "." in line:
            parts = re.split(r"\.|\(|\)", line)
            cls_name = parts[0]
            command = parts[1]
            
            if cls_name in HBNBCommand.cls:
                if command == "all":
                    print(self.get_obj(cls_name))
                elif command == "count":
                    print(len(self.get_obj(cls_name)))




if __name__ == "__main__":
    HBNBCommand().cmdloop()
