import re
from Elements import IElement
from LineIterator import LineIterator

ALL_LINK_RE = r"(?:!?\[([^\]]*)\]\(([^)]*)\))"
TIP_LINK_RE = r'(?:!?\[([^\]]*)\]\(([^\)]*)\s+(?:"([^"]*)")?\))'

NEW_LINK_FORMAT = "[{}|{}|{}]"
IMAGE_FORMAT = "!{}!"
IMAGE_CHAR = "!"


class LinkElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return re.search(ALL_LINK_RE, line) is not None

    def replace(self, line_iterator: LineIterator) -> None:
        line = line_iterator.value
        new_line = ""
        match = re.search(ALL_LINK_RE, line)

        while match is not None:
            new_line += line[:match.start()]
            new_line += self.__convert_link(match.group())
            line = line[match.end():]
            match = re.search(ALL_LINK_RE, line)
        line_iterator.value = new_line + line

    @staticmethod
    def __convert_link(text: str) -> str:
        tip = ""
        tip_link = re.search(TIP_LINK_RE, text)
        if tip_link:
            alias, link, tip = tip_link.groups()
        else:
            alias, link = re.search(ALL_LINK_RE, text).groups()
        if text[0] == IMAGE_CHAR:
            link = IMAGE_FORMAT.format(link)
        return NEW_LINK_FORMAT.format(alias, link, tip)

