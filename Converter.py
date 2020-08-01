from typing import List
from Elements import IElement
from LineIterator import LineIterator

NEWLINE = "\n"


class Converter:

    def __init__(self, elements: List[IElement]):
        self.__elements = elements

    def convert(self, markdown: str) -> str:
        """
        Convert the given markdown string to Atlassian Markup.
        """
        lines = markdown.split(NEWLINE)
        iterator = LineIterator(lines)

        while not iterator.is_done():
            for element in self.__elements:
                if element.is_relevant(iterator.value):
                    element.replace(iterator)
            iterator.advance()
        return NEWLINE.join(iterator.lines)
