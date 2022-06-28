#!/usr/bin/python3
"""
    Console Module
"""
from cmd import Cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(Cmd):
    """class HBNB Command"""

    Cmd.prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when Enter"""
        pass

    def do_quit(self, s):
        """Quit the console"""
        exit()

    def help_quit(self):
        """Informations about quit"""
        print('Quit command to exit the program\n')

    def do_EOF(self, s):
        """Quit the console"""
        print()
        exit()

    def help_EOF(self):
        """Informations about EOF"""
        print('Ctrl + D to exit the program\n')

    def do_create(self, s):
        """Create a BaseModel instance, print its id and save it"""
        list = s.split()
        if len(list) < 1:
            print('** class name missing **')
        elif list[0] == 'BaseModel':
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        else:
            print("** class doesn't exist **")

    def help_create(self):
        """Informations about create"""
        print('Create a BaseModel instance, print its id and save it\n')

    def do_show(self, s):
        """Show string representation of an instance"""
        my_list = s.split()
        my_dict = storage.all()
        check = 0
        if len(my_list) == 0:
            print("** class name missing **")
        elif len(my_list) == 1 and my_list[0] == "BaseModel":
            print("** instance id missing **")
        elif my_list[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for key, value in my_dict.copy().items():
                if key == f"BaseModel.{my_list[1]}":
                    print(value)
                    check = 1
            if check == 0:
                print('** no instance found **')

    def help_show(self):
        """Informations about show"""
        print('Show string representation of an instance\n')

    def do_destroy(self, s):
        """Destroy an instance with its id"""
        list = s.split()
        dict = storage.all()
        check = 0
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(list) == 1:
            print("** instance id missing **")
        else:
            for key, value in dict.copy().items():
                if key == f"BaseModel.{list[1]}":
                    dict.pop(key)
                    storage.save()
                    check = 1
            if check == 0:
                print("** no instance found **")

    def help_destroy(self):
        """Informations about destroy"""
        print('Destroy an instance with its id\n')

    def do_all(self, s):
        """Print the string representation of all instances"""
        my_list = s.split()
        my_dict = storage.all()
        if len(my_list) == 1 and my_list[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            for value in my_dict.copy().values():
                print(value)

    def help_all(self):
        """Informations about all"""
        print("Print the string representation of all instances\n")

    def do_update(self, s):
        """Adding or updating attribute of an instance"""
        list = shlex.split(s, posix=False)
        dict = storage.all()
        my_obj = None
        if len(list) == 0:
            print("** class name missing **")
        elif list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(list) == 1:
            print("** instance id missing **")
        else:
            for key, value in dict.copy().items():
                if key == f"BaseModel.{list[1]}":
                    my_obj = value
            if my_obj is None:
                print("** no instance found **")
            elif len(list) == 2:
                print("** attribute name missing **")
            elif len(list) == 3:
                print("** value missing **")
            else:
                if list[3][0] == '"':
                    setattr(my_obj, list[2], list[3][1:-1])
                elif '.' in list[3]:
                    setattr(my_obj, list[2], float(list[3]))
                else:
                    setattr(my_obj, list[2], int(list[3]))
            storage.save()

    def help_update(self):
        """Informations about update"""
        print("Adding or updating attribute of an instance\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()