from pattern import TextEditor, InsertCommand, DeleteCommand, CommandInvoker

class EditorApplication:
    """A real-world application that uses the Command pattern to manage text editing."""
    
    def __init__(self):
        self.editor = TextEditor()
        self.invoker = CommandInvoker()
        
    def type(self, text: str):
        print(f"User types: '{text}'")
        self.invoker.execute_command(InsertCommand(self.editor, text))
        
    def undo(self):
        print("User hits Undo")
        self.invoker.undo()
        
    def delete_all(self):
        print("User deletes all text")
        self.invoker.execute_command(DeleteCommand(self.editor))
        
    def show_content(self):
        print(f"Editor Content: [{self.editor.get_text()}]")

if __name__ == "__main__":
    app = EditorApplication()
    
    app.type("Design ")
    app.type("Patterns ")
    app.type("in Practice")
    app.show_content()
    
    app.undo()
    app.show_content()
    
    app.delete_all()
    app.show_content()
    
    app.undo()
    app.show_content()
