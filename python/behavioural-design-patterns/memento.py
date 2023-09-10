
class TextEditorMemento:
    def __init__(self, text):
        self.text = text
    
    def get_text(self):
        return self.text
        
class TextEditor:
    def __init__(self):
        self.text = ""
    
    def set_text(self, text):
        self.text = text
    
    def get_text(self):
        return self.text
    
    def save(self):
        return TextEditorMemento(self.text)
    
    def restore(self, memento):
        self.text = memento.get_text()

class TextEditorCaretaker:
    def __init__(self):
        self.memento_stack = []
    
    def save(self, memento):
        self.memento_stack.append(memento)
    
    def undo(self):
        if self.memento_stack:
            return self.memento_stack.pop()
        return None
        
if __name__ == "__main__":
    textEditor = TextEditor()
    caretakerUI = TextEditorCaretaker()

    textEditor.set_text("Hello, Rishi!")
    print("Typed text: " + textEditor.get_text())


    caretakerUI.save(textEditor.save())

    textEditor.set_text("Hello, Rich")

    print("Auto corrected text: " + textEditor.get_text())

    previousState = caretakerUI.undo()
    if previousState is not None:
        textEditor.restore(previousState)

    print("Undone for correction: " + textEditor.get_text())