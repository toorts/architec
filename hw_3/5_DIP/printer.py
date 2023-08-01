from printer_interface import PrinterInterface
from text_interface import TextInterface

class Printer(PrinterInterface):
    def print(self, text: TextInterface) -> None:
        print(text.get_text())
