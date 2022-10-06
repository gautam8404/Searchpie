import wikipedia
from .helpers.DataClass import dataclass


class WIKI:

    def __init__(self, query):
        self.query = query

    def _call(self, obj):
        if obj is None or obj == []:
            raise WikiExceptions("There are no results that matched your query")

    def result(self):
        search = wikipedia.search(self.query)
        self._call(search)
        page = wikipedia.page(search[0])
        wiki = dataclass()
        wiki.identifier_type = "wiki"
        wiki.title = page.title
        wiki.synopsis = page.summary
        wiki.url = page.url

        return [wiki]


class WikiExceptions(Exception):
    pass
