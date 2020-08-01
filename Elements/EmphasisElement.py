import re
from Elements import IElement
from LineIterator import LineIterator

FIND_REGEX = r"(\*+|_+)(.+?)\1"

OLD_EMPHASIS = ("_", "*")
NEW_EMPHASIS = "_"
NEW_STRONG = "*"


class EmphasisElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return re.search(FIND_REGEX, line) is not None

    def replace(self, line_iterator: LineIterator) -> None:
        line = line_iterator.value
        new_line = ""
        match = re.search(FIND_REGEX, line)

        while match is not None:
            new_line += line[:match.start()]
            new_line += self.__convert_emphasis(match.group())
            line = line[match.end():]
            match = re.search(FIND_REGEX, line)
        new_line += line
        line_iterator.value = new_line

    @staticmethod
    def __convert_emphasis(emphasis: str) -> str:
        text = list(emphasis)
        index_a = 0
        index_b = len(text) - 1
        current_char = ""
        num_a_chars = 0
        num_b_chars = 0

        while index_a != index_b:
            if num_a_chars == 0 and num_b_chars == 0:
                if text[index_a] in OLD_EMPHASIS:
                    current_char = text[index_a]
                    num_a_chars = 1
                index_a += 1
            elif num_a_chars == 1 and num_b_chars == 0:
                if text[index_a] == current_char:
                    num_a_chars += 1
                    index_a += 1
                elif text[index_b] == current_char:  # Emphasis
                    text[index_a - 1] = NEW_EMPHASIS
                    text[index_b] = NEW_EMPHASIS
                    num_a_chars = 0
                    index_b -= 1
                else:
                    index_b -= 1
            elif num_a_chars == 2 and num_b_chars == 0:
                if text[index_b] == current_char:
                    num_b_chars += 1
                index_b -= 1
            elif num_a_chars == 2 and num_b_chars == 1:
                if text[index_b] == current_char:  # Strong
                    del text[index_a - 1]
                    del text[index_b]
                    index_a -= 1
                    index_b -= 2
                    text[index_a - 1] = NEW_STRONG
                    text[index_b + 1] = NEW_STRONG
                    num_a_chars = 0
                    num_b_chars = 0
                else:  # Emphasis
                    text[index_a - 1] = NEW_EMPHASIS
                    text[index_b + 1] = NEW_EMPHASIS
                    num_a_chars = 1
                    num_b_chars = 0
        return "".join(text)
