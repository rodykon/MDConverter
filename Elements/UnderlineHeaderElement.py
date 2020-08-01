import re
from Elements import IElement
from LineIterator import LineIterator

HEADER_ONE_CHAR = "="
NEW_HEADER_FORMAT = "h{}. {}"
FIND_REGEX = r"^(-+|=+)$"


class UnderlineHeaderElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return re.search(FIND_REGEX, line.strip()) is not None

    def replace(self, line_iterator: LineIterator) -> None:
        header_char = line_iterator.value.strip()[0]
        header_num = 1 if header_char is HEADER_ONE_CHAR else 2

        line_iterator.remove_current()
        line_iterator.reverse()

        line_iterator.value = NEW_HEADER_FORMAT.format(header_num, line_iterator.value)
