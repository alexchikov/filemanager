import os
import re
import exc
import traceback
import shutil

system = os.name
banned_filenames = ['CON', 'PRN', 'AUX', 'NUL',
                    'COM0', 'COM1', 'COM2', 'COM3',
                    'COM4', 'COM5', 'COM6', 'COM7',
                    'COM8', 'COM9', 'LPT0', 'LPT1',
                    'LPT2', 'LPT3', 'LPT4', 'LPT5',
                    'LPT6', 'LPT7', 'LPT8', 'LPT9']
dirname_regexp = re.compile(r'[^<>:«|?*.«:;|=,]+')
filename_regexp = re.compile(r'[-a-zA-Z0-9()!@$%^*_.]+')

"""
Commands:
    > mkd - using for creating dirs;
    > dld - using for drop dirs;
    > chd - using for changing dirs;
    > mkf - using for creating files;
    > wrt - for write text in files;
    > dlf - for deleting files;
    > view - for viewing files;
    > copy - for copying files;
    > move - for moving files;
    > rname - for renaming files;
"""


def parse_command(command: str) -> None:
    # parse the input command
    splitted = command.split()
    if splitted[0] in commands.keys():
        match splitted[0]:
            case 'mkd':
                if len(splitted) == 2 and dirname_regexp.fullmatch(splitted[1].strip('"'))\
                        and splitted[1] not in banned_filenames:
                    commands['mkd'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled")
            case 'dld':
                if len(splitted) == 2 and dirname_regexp.fullmatch(splitted[1].strip('"'))\
                        and splitted[1] not in banned_filenames:
                    commands['dld'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled")
            case 'chd':
                if len(splitted) == 2:
                    commands['chd'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled")
            case 'mkf':
                if len(splitted) == 2 and filename_regexp.fullmatch(splitted[1].strip('"')):
                    commands['mkf'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'view':
                if len(splitted) == 2:
                    commands['view'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'copy':
                if len(splitted) == 3:
                    commands['copy'](splitted[1], splitted[2])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'move':
                if len(splitted) == 3:
                    commands['move'](splitted[1], splitted[2])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'dlf':
                if len(splitted) == 2:
                    commands['dlf'](splitted[1])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'rname':
                if len(splitted) == 3 and filename_regexp.fullmatch(splitted[1].strip('"')):
                    commands['rname'](splitted[1], splitted[2])
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled: wrong filename")
            case 'wrt':
                if len(splitted) >= 3:
                    text = command.split("<=")
                    commands['wrt'](splitted[1], text[1].strip('" "'))
                else:
                    raise exc.CommandWrongArguments("Wrong arguments was handled")
    else:
        raise exc.CommandDoesNotExist("This command doesn't exist")


def mkd(path: str) -> None:
    # make a directory
    os.mkdir(path)


def dld(path: str):
    # delete/drop a directory
    try:
        os.rmdir(path=path)
    except OSError:
        raise exc.CommandWrongArguments("This file doesn't exist")


def chd(path):
    # change a path of directory
    try:
        if os.getcwd() == username and path == "..":
            raise PermissionError
        else:
            os.chdir(path=path)
    except OSError:
        raise exc.CommandWrongArguments("This dir doesn't exist")


def mkf(path):
    # make an empty file
    try:
        open(path, 'w')
    except:
        raise exc.CommandWrongArguments("Как вы могли ошибиться в такой легкой команде :(")


def wrt(path: str, text: str):
    # write some text in file
    file = path
    try:
        with open(path, "a+") as file:
            file.write(text+'\n')
    except:
        raise FileNotFoundError("There isn't a file with that path")


def dlf(path: str):
    # delete a file *Sanechek
    try:
        os.remove(path)
    except OSError:
        raise exc.CommandWrongArguments("This file doesn't exist")


def view(path: str):
    try:
        with open(path) as file:
            print(*file.readlines())
    except:
        raise exc.CommandWrongArguments("This file doesn't exist")


def copy(name_of_file: str, new_directory: str):
    # copy a file from one directory to another *Andrey
    try:
        shutil.copy(name_of_file, new_directory)
    except:
        raise exc.CommandWrongArguments("Как вы могли ошибиться в такой легкой команде :(")


def move(path_to_file: str, new_directory: str):
    # move a file from one directory to another *Sanechek
    try:
        match system:
            case 'posix':
                os.rename(path_to_file, new_directory+'/'+path_to_file)
            case 'nt':
                os.rename(path_to_file, new_directory+'\\'+path_to_file)
    except:
        raise exc.CommandWrongArguments("Как вы могли ошибиться в такой легкой команде :(")


def rname(file_name: str, new_name: str):
    # change file name *Andrey
    try:
        os.rename(file_name, new_name)
    except:
        raise exc.CommandWrongArguments("Как вы могли ошибиться в такой легкой команде :(")


def run() -> str:
    command = input(
        f'\033[32m(filemanager\033[36m|\033[32m{os.getcwd()})\033[0m ')
    if command.strip() == "exit":
        exit()
    else:
        try:
            parse_command(command=command)
        except Exception as e:
            print(f"\033[31m{e}\n", end='')

commands = {'mkd': mkd, 'dld': dld,
            'chd': chd, 'mkf': mkf,
            'wrt': wrt, 'dlf': dlf,
            'view': view, 'copy': copy,
            'move': move, 'rname': rname}

if __name__ == "__main__":
    username = input("Your username: ")
    password = input("Your password: ")
    while True:
        run()