import requests
from .helpers.DataClass import dataclass


class MAL:
    order_by = "favorites"
    limit = 10
    sort = "desc"

    def __init__(self):
        self.base_url = "https://api.jikan.moe/v4/"

    @staticmethod
    def sendRequest(url):
        return requests.get(url).json()

    def url_builder(self, media_type: str, query: str):
        query = query.replace(" ", "+")
        return self.base_url + media_type + f"?q={query}&limit={self.limit}&order_by={self.order_by}&sort={self.sort}"

    def _call(self, result):
        if result["data"] == [] or result["data"] is None:
            raise MalExceptions("There are no results that matched your query, use japnese name for better search results")
        if self.order_by not in ["mal_id", "title", "type", "rating", "start_date", "end_date", "episodes", "score",
                                 "scored_by", "rank", "popularity", "members", "favorites"]:
            raise MalExceptions("Invalid OrderBy Flag")
        if self.sort not in ["asc", "desc"]:
            MalExceptions("Invalid sort flag")

    @staticmethod
    def getGenre(data) -> list:
        genre_list = []
        for i in data["genres"]:
            genre_list.append(i["name"])
        return ", ".join(genre_list)

    def anime(self, query):
        res = self.sendRequest(self.url_builder("anime", query))
        self._call(res)
        data_list = []
        for i in res["data"]:
            anime = dataclass()
            anime.identifier_type = "anime"
            anime.id = i["mal_id"]
            anime.url = i["url"]
            anime.title = i["title"]
            anime.type = i["type"]
            anime.episodes = i["episodes"]
            anime.status = i["status"]
            anime.duration = i["duration"]
            anime.score = i["score"]
            anime.synopsis = i["synopsis"]
            anime.genres = self.getGenre(i)

            data_list.append(anime)

        return data_list

    def manga(self, query):
        res = self.sendRequest(self.url_builder("manga", query))
        self._call(res)
        data_list = []
        for i in res["data"]:
            manga = dataclass()
            manga.identifier_type = "anime"
            manga.id = i["mal_id"]
            manga.url = i["url"]
            manga.title = i["title"]
            manga.type = i["type"]
            manga.chapters = i["chapters"]
            manga.status = i["status"]
            manga.score = i["score"]
            manga.synopsis = i["synopsis"]
            manga.genres = self.getGenre(i)

            data_list.append(manga)

        return data_list


class MalExceptions(Exception):
    pass

