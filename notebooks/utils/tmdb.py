import pandas as pd


def extract_first_movie_tmdb_id(content: dict) -> int | None:
    results: list[dict] = content.get("results")
    first_movie: dict = results[0] if results else dict()
    return first_movie.get("id")


def extract_movie_director(content: dict) -> str | None:
    crew: pd.DataFrame = pd.DataFrame(content.get("crew"))
    if crew.empty:
        return None
    MASK: pd.Series = crew["job"] == "Director"
    directors: pd.Series = crew.loc[MASK, "name"]
    if not directors.empty:
        return directors.to_string(index=False)


def extract_movie_imdb_id(content: dict) -> str | None:
    imdb_id: str = content.get("imdb_id")
    return imdb_id if imdb_id else None


def extract_movie_countries(content: dict) -> str | None:
    countries: list[dict] = content.get("production_countries")
    if not countries:
        return None
    countries_codes: list[str] = [country.get("iso_3166_1") for country in countries]
    return ";".join(countries_codes)


def extract_movie_genres(content: dict) -> str | None:
    genres: list[dict] = content.get("genres")
    if not genres:
        return None
    genres_names: list[str] = [genre.get("name") for genre in genres]
    return ";".join(genres_names)


def extract_movie_runtime(content: dict) -> int | None:
    runtime: int = content.get("runtime")
    return runtime if runtime else None


def extract_movie_credits_number(content: dict) -> int | None:
    cast: list[dict] = content.get("cast")
    crew: list[dict] = content.get("crew")
    credits_number: int = len(cast + crew)
    return credits_number if credits_number else None
