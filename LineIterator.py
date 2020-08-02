from typing import List
from Exceptions import IteratorException


class LineIterator:

    def __init__(self, lines: List[str]):
        self.lines = lines
        self.__index = 0
        self.value = self.lines[self.__index]

    def advance(self):
        """
        Advance the iterator one line forward.
        """
        if self.is_done():
            raise IteratorException("Attempted to advance iterator that is done.")
        self.lines[self.__index] = self.value
        self.__index += 1
        if not self.is_done():
            self.value = self.lines[self.__index]

    def reverse(self):
        """
        Reverse the iterator one line backward.
        """
        if self.__index == 0:
            raise IteratorException("Attempted to reverse iterator that is at start.")
        self.lines[self.__index] = self.value
        self.__index -= 1
        self.value = self.lines[self.__index]

    def remove_current(self):
        """
        Remove current line from the iterator.
        """
        del self.lines[self.__index]
        self.value = self.lines[self.__index]

    def is_done(self) -> bool:
        """
        Return true if iterator is at the last line.
        """
        return self.__index == len(self.lines)
