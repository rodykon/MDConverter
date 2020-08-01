import re
from Elements import IElement
from LineIterator import LineIterator

FIND_REGEX = r"`(.*?)`"
NEW_CODE_FORMAT = "{{code}}{}{{code}}"


class InlineCodeElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return re.search(FIND_REGEX, line) is not None

    def replace(self, line_iterator: LineIterator) -> None:
        line = line_iterator.value
        new_line = ""
        match = re.search(FIND_REGEX, line)

        while match is not None:
            new_line += line[:match.start()]
            new_line += self.__convert_code(match.group())
            line = line[match.end():]
            match = re.search(FIND_REGEX, line)
        line_iterator.value = new_line + line

    @staticmethod
    def __convert_code(text: str) -> str:
        content = re.search(FIND_REGEX, text).groups()[0]
        return NEW_CODE_FORMAT.format(content)

