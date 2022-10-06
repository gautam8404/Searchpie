import requests
from .helpers.DataClass import dataclass
from .helpers.iso_language_codes import getLanguage


class TMDB:

    def __init__(self, api_key):
        self.base_url = "https://api.themoviedb.org/3"
        self.api_key = api_key

    def _call(self, result):
        if self.api_key is None or self.api_key == '':
            raise TMDbException("No Api Key")

        if "success" in result and result["success"] is False:
            raise TMDbException(result["status_message"])

        if result["results"] == [] or result["results"] is None:
            TMDbException("There are no results that matched your query")

    @staticmethod
    def sendRequest(url):
        return requests.get(url).json()

    def getGenre(self, media_type, genre_ids: list) -> str:
        url = f"https://api.themoviedb.org/3/genre/{media_type}/list?api_key={self.api_key}"
        res = self.sendRequest(url)
        genre_dict = {}

        for i in res["genres"]:
            genre_dict[i["id"]] = i["name"]

        genre_str_list = []
        for j in genre_ids:
            genre_str_list.append(genre_dict.get(j))

        return ", ".join(genre_str_list)

    def url_builder(self, media_type: str, query: str):
        query = query.replace(' ', '%20')
        return self.base_url + f"/search/{media_type}?api_key={self.api_key}&query={query}&page=1"

    def Movie(self, query: str):
        res = self.sendRequest(self.url_builder("movie", query))
        self._call(res)
        data_list = []
        for i in res["results"]:
            movie = dataclass()
            movie.title = i["title"]
            movie.id = i["id"]
            movie.genres = self.getGenre("movie", i["genre_ids"])
            movie.score = i["vote_average"]
            movie.language = getLanguage(i["original_language"])
            movie.synopsis = i["overview"]
            movie.identifier_type = "movie"
            movie.url = "https://www.themoviedb.org/" + movie.identifier_type + "/" + str(movie.id)

            data_list.append(movie)

        return data_list

    def Tv(self, query: str):
        res = self.sendRequest(self.url_builder("movie", query))
        self._call(res)
        data_list = []
        for i in res["results"]:
            tv = dataclass()
            tv.title = i["name"]
            tv.id = i["id"]
            tv.genres = self.getGenre("tv", i["genre_ids"])
            tv.score = i["vote_average"]
            tv.language = i["original_language"]
            tv.synopsis = i["overview"]
            tv.identifier_type = "tv"
            tv.url = "https://www.themoviedb.org/" + tv.identifier_type + "/" + str(tv.id)

            data_list.append(tv)

        return data_list


class TMDbException(Exception):
    pass



