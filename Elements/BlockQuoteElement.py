from Elements import IElement
from LineIterator import LineIterator

OLD_BQ = ">"
NEW_BQ = "bq."


class BlockQuoteElement(IElement):

    def is_relevant(self, line: str) -> bool:
        return line.strip() and line.strip()[0] == OLD_BQ

    def replace(self, line_iterator: LineIterator) -> None:
        line_iterator.value = line_iterator.value.replace(OLD_BQ, NEW_BQ, 1)
