import requests
from .helpers.DataClass import dataclass


class WIKI:

    def __init__(self, query: str):
        self.query = query
        self.search = "https://en.wikipedia.org/w/api.php?action=opensearch&search={}&limit=1&format=json"
        self.page = "https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exlimit=1&titles={}&explaintext=1&exsectionformat=plain&format=json"

    @staticmethod
    def sendRequest(url):
        return requests.get(url).json()

    def url_builder(self, query: str, base_url: str):
        query = query.replace(" ", "+")
        return base_url.format(query)

    def _call(self, result):
        if self.query == [] or self.query == '' or self.query is None:
            raise WikiExceptions("Empty query")
        if result is None or result == []:
            raise WikiExceptions(f"There are no results that matched \"{self.query}\"")
        if type(result) is list and result[1] == []:
            raise WikiExceptions(f"There are no results that matched \"{self.query}\"")
        if result is int and result == -1:
            raise WikiExceptions(f"No page exists for \"{self.query}\" ")

    def result(self):
        search = self.sendRequest(self.url_builder(self.query, self.search))
        self._call(search)
        page_id = search[1][0]
        page = self.sendRequest(self.url_builder(page_id, self.page))
        self._call(page)
        page = page["query"]["pages"]

        for i in page:
            self._call(i)
            page = page[i]
        wiki = dataclass()
        wiki.identifier_type = "wiki"
        wiki.title = page['title'].replace(" ", "_")
        wiki.synopsis = page['extract']
        wiki.url = "https://en.wikipedia.org/wiki/{}".format(wiki.title)

        return [wiki]


class WikiExceptions(Exception):
    pass
