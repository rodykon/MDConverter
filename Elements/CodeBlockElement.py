from Elements import IElement
from LineIterator import LineIterator

OLD_CODE = "```"
NEW_CODE_FORMAT = "{{code:language={}}}"
CODE_CLOSE = "{code}"


class CodeBlockElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return line[:len(OLD_CODE)] == OLD_CODE

    def replace(self, line_iterator: LineIterator) -> None:
        language = line_iterator.value[3:]
        line_iterator.value = NEW_CODE_FORMAT.format(language)

        while not self.is_relevant(line_iterator.value):
            line_iterator.advance()

        line_iterator.value = CODE_CLOSE
