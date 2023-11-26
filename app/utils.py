import tomllib


def get_version() -> str:
    """Get the version from pyproject.toml."""

    with open("../pyproject.toml", "rb") as f:
        return tomllib.load(f)["tool"]["poetry"]["version"]

