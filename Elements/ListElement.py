import re
from Elements import IElement
from LineIterator import LineIterator

ORDERED_LIST_REGEX = r"^\s*[0-9]+\.\s"
UNORDERED_LIST_REGEX = r"^\s*[\-\*\+]\s"

NEW_ORDERED_CHAR = "#"
NEW_UNORDERED_CHAR = "*"

SPACE = " "


class ListElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return self.__is_ordered_list(line) or self.__is_unordered_list(line)

    def replace(self, line_iterator: LineIterator) -> None:
        line = line_iterator.value
        list_char = NEW_ORDERED_CHAR if self.__is_ordered_list(line) else NEW_UNORDERED_CHAR
        num_indent = self.__get_indent_number(line)
        line = self.__unlist(line)
        line_iterator.value = "{}{}".format(list_char * (num_indent + 1), line)

    @staticmethod
    def __is_ordered_list(line: str) -> bool:
        return re.match(ORDERED_LIST_REGEX, line) is not None

    @staticmethod
    def __is_unordered_list(line: str) -> bool:
        return re.match(UNORDERED_LIST_REGEX, line) is not None

    @staticmethod
    def __get_indent_number(line: str) -> int:
        num_spaces = len(line) - len(line.lstrip())

        return int(num_spaces / 4)

    @staticmethod
    def __unlist(line: str):
        return line.lstrip()[line.lstrip().find(SPACE):]
