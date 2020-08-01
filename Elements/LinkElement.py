import re
from Elements import IElement
from LineIterator import LineIterator

IMAGE_RE = r"(?:!\[([^\]]*)\]\(([^)]*)\))"

NEW_LINK_FORMAT = "[{}|!{}!]"


class LinkElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return re.search(IMAGE_RE, line) is not None

    def replace(self, line_iterator: LineIterator) -> None:
        line = line_iterator.value
        new_line = ""
        match = re.search(IMAGE_RE, line)

        while match is not None:
            new_line += line[:match.start()]
            new_line += self.__convert_link(match.group())
            line = line[match.end():]
            match = re.search(IMAGE_RE, line)
        line_iterator.value = new_line + line

    @staticmethod
    def __convert_link(text: str) -> str:
        alias, link = re.search(IMAGE_RE, text).groups()
        return NEW_LINK_FORMAT.format(alias, link)

