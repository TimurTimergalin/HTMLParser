from enum import Enum

from HTMLParser.Parser.tags import Tag


class TagTypes(Enum):
    OPENING = 1  # <html style="scroll-behaviour: smooth;">
    CLOSING = 2  # </span>
    SPECIAL = 3  # <!DOCTYPE html>
    EMPTY = 4  # <input type="submit" />


class TagBracket:
    def __init__(self, st):  # st - строка, задающая тег, например <a href="www.google.com"> или </body>
        self._init(self._parse_tag_string(st))

    def _parse_tag_string(self, st) -> dict:
        pass  # Здесь строка st преобразуется в словарь с нужными значениями: название тега, аттрибуты, тип (TagTypes)

    def _init(self, dc):
        pass  # Здесь на основе словаря, полученного _parse_tag_string инициализируется объект

    def to_parsed_element(self) -> Tag:
        pass  # Если тег не CLOSING, создаёт на основе TagBracket объект AbstractTag
