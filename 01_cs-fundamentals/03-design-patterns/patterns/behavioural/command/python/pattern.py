from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    """The Command interface declares a method for executing a command."""
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class TextEditor:
    """The Receiver class contains some important business logic."""
    def __init__(self):
        self._text = ""

    def get_text(self) -> str:
        return self._text

    def set_text(self, text: str) -> None:
        self._text = text

class InsertCommand(Command):
    """A concrete command for inserting text."""
    def __init__(self, editor: TextEditor, text: str):
        self._editor = editor
        self._text_to_insert = text
        self._previous_text = ""

    def execute(self) -> None:
        self._previous_text = self._editor.get_text()
        self._editor.set_text(self._previous_text + self._text_to_insert)

    def undo(self) -> None:
        self._editor.set_text(self._previous_text)

class DeleteCommand(Command):
    """A concrete command for deleting all text."""
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._previous_text = ""

    def execute(self) -> None:
        self._previous_text = self._editor.get_text()
        self._editor.set_text("")

    def undo(self) -> None:
        self._editor.set_text(self._previous_text)

class CommandInvoker:
    """The Invoker is associated with one or several commands."""
    def __init__(self):
        self._history: List[Command] = []

    def execute_command(self, command: Command):
        command.execute()
        self._history.append(command)

    def undo(self):
        if self._history:
            command = self._history.pop()
            command.undo()

if __name__ == "__main__":
    editor = TextEditor()
    invoker = CommandInvoker()
    
    invoker.execute_command(InsertCommand(editor, "Hello "))
    invoker.execute_command(InsertCommand(editor, "World!"))
    print(f"Current Text: '{editor.get_text()}'")
    
    invoker.undo()
    print(f"After Undo: '{editor.get_text()}'")
    
    invoker.execute_command(DeleteCommand(editor))
    print(f"After Delete: '{editor.get_text()}'")
    
    invoker.undo()
    print(f"After Undo Delete: '{editor.get_text()}'")
