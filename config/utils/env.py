import os.path
from dotenv import dotenv_values


def load_env(path: str) -> None:
    for key, value in dotenv_values(dotenv_path=path).items():
        os.environ[key] = value
