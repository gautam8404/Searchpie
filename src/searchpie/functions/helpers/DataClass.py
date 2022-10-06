class dataclass:
    title = None
    id = None
    identifier_type = None
    type = None
    genres = None
    score = None
    language = None
    episodes = None
    chapters = None
    duration = None
    status = None
    synopsis = None
    url = None

    _identifier_types = ["movie", "tv", "wiki", "anime", "manga"]

    def __init__(self):
        pass

    def __str__(self):
        if self.identifier_type is None or self.identifier_type not in self._identifier_types:
            return "Invalid Identifier Type"

        elif self.identifier_type == "wiki":
            msg = f"\033[4m{self.title}\033[0m:" + "\n\n" + self.synopsis
            return msg

        else:
            msg = []
            m = self.datadict()
            for i in m:
                if m[i] is not None:
                    msg.append(f"{i}: {m[i]}")
            return "\n".join(msg)

    def datadict(self):
        return {
            "Title": self.title,
            "ID": self.id,
            "Type": self.type,
            "Genres": self.genres,
            "Score": self.score,
            "Language": self.language,
            "Episodes": self.episodes,
            "Chapters": self.chapters,
            "Duration": self.duration,
            "Status": self.status,
            "Synopsis": self.synopsis,
            "Url": self.url
        }

    # [self.title, self.id, self.type, self.genres, self.score, self.language, self.episodes, self.chapters,
    # self.duration, self.status, self.synopsis, self.desc, self.url]
