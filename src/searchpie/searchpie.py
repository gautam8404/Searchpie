import os
import json
from .functions.mal import MAL
from .functions.tmdb import TMDB
from .functions.wiki import WIKI


class SearchPie:

    working_dir = os.getcwd()
    _path = os.path.join(working_dir, 'configure.json')

    def __init__(self, args):
        self.args = args

    def _call(self, method: str):
        if method not in ["wiki", "movie", "tv", "anime", "manga"]:
            raise SearchPieExceptions("Invalid Default Method")

    @property
    def api_key(self):
        with open(self._path, "r") as file:
            api_key_dict = json.load(file)
        return api_key_dict["api_key"]

    @api_key.setter
    def api_key(self, key: str):
        with open(self._path, "r") as file:
            key_dict = json.load(file)

        key_dict["api_key"] = key
        with open(self._path, "w") as wfile:
            json.dump(key_dict, wfile, indent=4)

    @property
    def default(self):
        with open(self._path, "r") as file:
            api_key_dict = json.load(file)
        return api_key_dict["default"]

    @default.setter
    def default(self, default_method: str):
        self._call(default_method)
        with open(self._path, "r") as file:
            key_dict = json.load(file)

        key_dict["default"] = default_method
        with open(self._path, "w") as wfile:
            json.dump(key_dict, wfile, indent=4)

    def method_parser(self, method: str, query: list):
        self._call(method)
        args = self.args
        query = " ".join(query)
        if method == "wiki":
            w = WIKI(query)
            return w.result()
        elif method == "movie":
            m = TMDB(self.api_key)
            return m.Movie(query)
        elif method == "tv":
            t = TMDB(self.api_key)
            return t.Tv(query)
        elif method == "anime":
            a = MAL()
            return a.anime(query)
        elif method == "manga":
            manga = MAL()
            return manga.manga(query)

    def parser(self):
        args = self.args
        if args.default_method is not None and args.default_method != []:
            return self.method_parser(self.default, args.default_method)
        elif args.anime is not None and args.anime != []:
            return self.method_parser("anime", args.anime)
        elif args.manga is not None and args.manga != []:
            return self.method_parser("manga", args.manga)
        elif args.movie is not None and args.movie != []:
            return self.method_parser("movie", args.movie)
        elif args.tv is not None and args.tv != []:
            return self.method_parser("tv", args.tv)
        elif args.wiki is not None and args.wiki != []:
            return self.method_parser("wiki", args.wiki)


class SearchPieExceptions(Exception):
    pass
