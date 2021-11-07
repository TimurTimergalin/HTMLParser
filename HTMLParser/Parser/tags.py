def abstract(c):  # объекты встроенных абстрактных классов можно создать, если нет абстрактных методов
    method = c.__new__

    def new_new(cls, *args, **kwargs):
        if cls is c:
            raise TypeError(f"Can't instantiate abstract class {c.__name__}")
        return method(cls, *args, **kwargs)

    c.__new__ = new_new
    return c


@abstract
class HTMLElement:
    pass


@abstract
class Child(HTMLElement):
    def __init__(self):
        self._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, val):
        if val is not None and not isinstance(val, Container):
            raise TypeError(f"{val} cannot have children")
        self._parent = val


@abstract
class Container(HTMLElement):
    def __init__(self):
        self._children = []

    @property
    def children(self):
        return tuple(self._children)

    def append_child(self, el):
        if not isinstance(el, Child):
            raise TypeError(f"{el} cannot be a child")
        if el not in self._children:
            self._children.append(el)
            el.parent = self


@abstract
class HasInfo(HTMLElement):
    def __init__(self, tag_name, attrs):
        self.tag_name = tag_name
        self.attrs = attrs


class PlainText(Child):
    pass


class Document(Container):
    pass


@abstract
class Tag(HasInfo, Child):
    def __init__(self, name, attrs):
        HasInfo.__init__(self, name, attrs)
        Child.__init__(self)


class EmptyTag(Tag):
    pass


class ContainingTag(Tag, Container):
    def __init__(self, name, attrs):
        Tag.__init__(self, name, attrs)
        Container.__init__(self)
