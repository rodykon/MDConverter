from argparse import ArgumentParser, FileType
from Elements import NormalHeaderElement, UnderlineHeaderElement, EmphasisElement, BlockQuoteElement, ListElement, \
    CodeBlockElement, LinkElement, InlineCodeElement, LinkElement
from Converter import Converter


def main():
    converter = Converter([NormalHeaderElement(),
                           UnderlineHeaderElement(),
                           EmphasisElement(),
                           BlockQuoteElement(),
                           ListElement(),
                           CodeBlockElement(),
                           LinkElement(),
                           InlineCodeElement(),
                           LinkElement()])

    parser = ArgumentParser(description="Convert a markdown file to Atlassian markup language.")
    parser.add_argument("infile", type=FileType("r"))
    parser.add_argument("outfile", type=FileType("w"))

    args = parser.parse_args()

    args.outfile.write(converter.convert(args.infile.read()))


if __name__ == "__main__":
    main()
