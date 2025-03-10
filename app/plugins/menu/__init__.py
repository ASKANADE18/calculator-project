import logging
from app.commands import Command

class MenuCommand(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        logging.info("Displaying available commands.")
        print("Available commands:")
        for command_name in self.command_handler.commands.keys():
            print(f" - {command_name}")
            