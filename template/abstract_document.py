"""An abstract document containing a combination of hooks and abstract methods"""
from abc import ABCMeta, abstractmethod


class AbstractDocument(metaclass=ABCMeta):
    """A template class containing a template method and primitive methods"""

    @staticmethod
    @abstractmethod
    def title(document):
        """must implement"""

    @staticmethod
    def description(description):
        """hook method"""

    @staticmethod
    def author(document):
        """hook method"""

    @staticmethod
    def background_colour(document):
        """optional with a default behaviour"""
        document["background_colour"] = "white"

    @staticmethod
    @abstractmethod
    def text(document, text):
        """must implement"""

    @staticmethod
    def footer(document):
        """optional"""

    @staticmethod
    def print(document):
        """optional with a default behaviour"""
        print("---------------------")
        for attribute in document:
            print(f"{attribute}\t: {document[attribute]}")
        print()

    @classmethod
    def create_document(cls, text):
        """The template method"""
        _document = {}
        cls.title(document=_document)
        cls.description(description=_document)
        cls.author(document=_document)
        cls.background_colour(document=_document)
        cls.text(document=_document, text=text)
        cls.footer(document=_document)
        cls.print(document=_document)
