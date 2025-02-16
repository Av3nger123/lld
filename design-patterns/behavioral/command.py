from abc import ABC, abstractmethod


class Command(ABC):
    
    @abstractmethod
    def execute(self):
        raise NotImplementedError
    
    @abstractmethod
    def undo(self):
        raise NotImplementedError
    
class TextEditor:
    def __init__(self):
        self.text = ""

    def insert(self, new_text):
        self.text += new_text
        print(f"Insert: '{new_text}' → Text: '{self.text}'")

    def delete(self, length):
        removed_text = self.text[-length:]  # Store deleted text
        self.text = self.text[:-length]  # Remove text from editor
        print(f"Delete: '{removed_text}' → Text: '{self.text}'")
        return removed_text  # Return deleted text for undo
    
class InsertCommand(Command):
    def __init__(self, editor, text):
        self.editor = editor
        self.text = text

    def execute(self):
        self.editor.insert(self.text)

    def undo(self):
        self.editor.delete(len(self.text))

class DeleteCommand(Command):
    def __init__(self, editor, length):
        self.editor = editor
        self.length = length
        self.deleted_text = ""

    def execute(self):
        self.deleted_text = self.editor.delete(self.length)

    def undo(self):
        self.editor.insert(self.deleted_text)

class CommandManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()  # Clear redo history when a new command is executed

    def undo(self):
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            self.redo_stack.append(command)
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.execute()
            self.undo_stack.append(command)
        else:
            print("Nothing to redo.")

if __name__ == "__main__":
    editor = TextEditor()
    manager = CommandManager()
    
    manager.execute_command(InsertCommand(editor,"Hello"))
    manager.execute_command(InsertCommand(editor," World"))
    manager.execute_command(DeleteCommand(editor, 5))  # Delete "World"

    manager.undo()
    manager.undo()

    manager.redo()
    manager.redo()

