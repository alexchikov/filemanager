import os
import re
import exc
import traceback

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

    else:
        raise exc.CommandDoesNotExist("This command doesn't exist")


def mkd(path: str) -> None:
    os.mkdir(path)


def dld(path: str):
    try:
        os.rmdir(path=path)
    except OSError:
        raise exc.CommandWrongArguments("This file doesn't exist")


def chd(path):
    try:
        os.chdir(path=path)
    except OSError:
        raise exc.CommandWrongArguments("This dir doesn't exist")


def mkf(path):
    open(path, 'w')


def wrt():
    ...


def dlf():
    ...


def view(path: str):
    try:
        with open(path) as file:
            print(*file.readlines())
    except:
        raise exc.CommandWrongArguments("This file doesn't exist")


def copy():
    ...


def move():
    ...


def rname():
    ...


def run() -> str:
    command = input(f'\033[32m(filemanager\033[36m|\033[32m{os.getcwd()})\033[0m ')
    if command.strip() == "exit":
        exit()
    else:
        try:
            parse_command(command=command)
        except:
            print(f"\033[31m{traceback.format_exc()}", end='')


commands = {'mkd': mkd, 'dld': dld,
            'chd': chd, 'mkf': mkf,
            'wrt': wrt, 'dlf': dlf,
            'view': view, 'copy': copy,
            'move': move, 'rname': rname}

if __name__ == "__main__":
    while True:
        run()
