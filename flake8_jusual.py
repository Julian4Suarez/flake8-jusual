import ast
from email.generator import Generator

import importlib_metadata

from typing import Generator, Tuple, Type, Any


class Plugin:

    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: ast.AST) -> None:
        self._tree = tree

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        yield 1, 0, "JSA error argument", type(self)
