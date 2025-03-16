import pytest  # type: ignore
from martinpykit.utils import EnvConfig


def get_env():
    return EnvConfig()


def test_env():
    env = get_env()
    assert env.database_url == "postgres://user:password@localhost/dbname"
    assert env.api_key == "your_api_key"
    assert env.debug == "True"
