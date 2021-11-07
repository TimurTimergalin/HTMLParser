known_tags = {
    'empty': [  # Без закрывающего тега
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "menuitem",
        "meta",
        "param",
        "source",
        "track",
        "wbr"
    ],
    "nonformatted": [  # Не форматирующие содержимое
        "style",
        "script"
    ],
    "special": [  # начинается с <!
        "DOCTYPE"
    ],
    "other": [
        "a",
        "abbr",
        "address",
        "article",
        "aside",
        "audio",
        "b",
        "bdi",
        "bdo",
        "blockquote",
        "body",
        "button",
        "canvas",
        "caption",
        "cite",
        "code",
        "colgroup",
        "data",
        "datalist",
        "dd",
        "del",
        "details",
        "dfn",
        "dialog",
        "div",
        "dl",
        "dt",
        "em",
        "fieldset",
        "figcaption",
        "figure",
        "footer",
        "form",
        "h1", "h2", "h3", "h4", "h5", "h6",
        "head",
        "header",
        "html",
        "i",
        "iframe",
        "ins",
        "kbd",
        "label",
        "legend",
        "li",
        "main",
        "map",
        "mark",
        "meter",
        "nav",
        "noscript",
        "object",
        "ol",
        "optgroup",
        "option",
        "output",
        "p",
        "picture",
        "pre",
        "progress",
        "q",
        "ruby",
        "rb",
        "rt",
        "rtc",
        "rp",
        "s",
        "samp",
        "section",
        "select",
        "small",
        "span",
        "strong",
        "sub",
        "summary",
        "sup",
        "table",
        "tbody",
        "td",
        "template",
        "textarea",
        "tfoot",
        "th",
        "thead",
        "time",
        "title",
        "tr",
        "u",
        "ul",
        "var",
        "video"
    ]
}


class Config:
    PARSE_UNKNOWN_TAGS = True  # Если True, неизвестные теги будут восприниматься как элементы, иначе как plain text
    ACCEPT_SPECIAL_SYMBOLS = True  # Если True, служебные символы (<, > и т.д.), использованные неправильно,
    # парсер попытается воспринять как plain text, иначе поднимется ошибка
    CHECK_EMPTY_TAGS = True  # Если True, известные пустые (т.е. без закрывающегося тега) теги можно писать
    # без / в конце, например <input type="submit"> вместо <input type="submit" />, иначе поднимется ошибка
    CHECK_UNIQUE_IDS = True  # Если True, попытка создать тег с неуникальным id приведет к ошибке,
    # иначе к предупреждению

    def __init__(self, **kwargs):
        for i in self.get_all_params():
            if kwargs.get(i) is None:
                kwargs[i] = getattr(type(self), i)

        for i, val in kwargs.items():
            setattr(self, i, val)

    @classmethod
    def get_all_params(cls):
        res = []
        for i in dir(cls):
            if i.isupper():
                res.append(i)
        return res
