from abc import ABC, abstractmethod
from LineIterator import LineIterator


class IElement(ABC):

    @abstractmethod
    def is_relevant(self, line: str) -> bool:
        """
        Return true if this element is present in the given line.
        """
        pass

    @abstractmethod
    def replace(self, line_iterator: LineIterator) -> None:
        """
        Use the given LineIterator to to replace all instances of this element in the current line.
        """
        pass
