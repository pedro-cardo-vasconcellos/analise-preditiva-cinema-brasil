import re

import unidecode


def is_same_director(director_1: str, director_2: str) -> bool:
    names_1: set[str] = set(director_1.split(" "))
    names_2: set[str] = set(director_2.split(" "))
    return names_1.issuperset(names_2) or names_1.issubset(names_2)


def sanitize_director_name(name: str) -> str | None:
    if not isinstance(name, str):
        return None
    name: str = unidecode.unidecode(name)
    name: str = name.lower()
    name: str = re.sub(r"[^a-z]", " ", name)
    name: str = re.sub(r"\b[a-z]{1,2}\b", "", name)
    name: str = re.sub(r"\s{2,}", " ", name)
    name: str = name.strip()
    return name if name else None


def sanitize_movie_title(title: str) -> str | None:
    if not isinstance(title, str):
        return None
    title: str = unidecode.unidecode(title)
    title: str = title.lower()
    title: str = re.sub(r"[^a-z0-9]", " ", title)
    title: str = re.sub(r"\s{2,}", " ", title)
    title: str = title.strip()
    return title if title else None
