from text_interface import TextInterface

class Text(TextInterface):
    def __init__(self, text: str):
        self.text = text

    def get_text(self) -> str:
        return self.text
