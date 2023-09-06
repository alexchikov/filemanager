import os

system = os.name

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

def parse_command(command: str) -> ...:
    ...

def mkd():
    ...
    
def dld():
    ...
    
def chd():
    ...
    
def mkf():
    ...

def wrt():
    ...

def dlf():
    ...

def view():
    ...
    
def copy():
    ...
    
def move():
    ...
    
def rname():
    ...
    
def run():
    ...

commands = {'mkd': mkd, 'dld': dld,
            'chd':chd, 'mkf': mkf,
            'wrt': wrt, 'dlf': dlf,
            'view': view, 'copy': copy,
            }