from Elements import IElement
from LineIterator import LineIterator

HEADER_CHAR = "#"
NEW_HEADER_FORMAT = "h{}."
SPACE = " "


class NormalHeaderElement(IElement):

    def is_relevant(self, line: str) -> bool:
        header_number = self.__get_header_number(line)
        return 1 <= header_number <= 6 and line[header_number] == SPACE

    def replace(self, line_iterator: LineIterator) -> None:
        header_number = self.__get_header_number(line_iterator.value)
        old_header_string = HEADER_CHAR * header_number
        new_header_string = NEW_HEADER_FORMAT.format(header_number)
        line_iterator.value = line_iterator.value.replace(old_header_string, new_header_string, 1)

    @staticmethod
    def __get_header_number(line) -> int:
        header_number = 0
        for char in line:
            if char == HEADER_CHAR:
                header_number += 1
            else:
                return header_number
        return 0
