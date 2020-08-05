import base64

SRC_FORMAT = ' src="data:image/{type};base64,{data}"'
TITLE_FORMAT = ' title="{}"'
ALT_FORMAT = ' alt="{}"'
OPEN_IMG = '<img'
CLOSE_IMG = '>'


class ImageTagGenerator:

    def generate(self, path: str, title: str = None, alt: str = None) -> str:
        """
        Generate an img html tag for the image at the given path that can be used offline.
        """
        tag = OPEN_IMG
        tag += SRC_FORMAT.format(type=self.__extract_filetype(path), data=self.__b64_read(path))
        if title:
            tag += TITLE_FORMAT.format(title)
        if alt:
            tag += ALT_FORMAT.format(alt)
        return tag + CLOSE_IMG

    @staticmethod
    def __extract_filetype(path: str) -> str:
        return path.split(".")[-1]

    @staticmethod
    def __b64_read(path):
        with open(path, "rb") as image:
            return base64.b64encode(image.read()).decode()
