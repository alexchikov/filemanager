import sys

class CommandDoesNotExist(Exception):
    def __init__(self, *args: object) -> None:
        self.message = args
    def __str__(self) -> str:
        return f"{self.message[0]}"
    
class CommandWrongArguments(Exception):
    def __init__(self, *args: object) -> None:
        self.message = args
    def __str__(self) -> str:
        return f"{self.message[0]}"
    
