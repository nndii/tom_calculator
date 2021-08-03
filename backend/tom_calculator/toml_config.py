from decimal import Decimal
from functools import lru_cache
from typing import Dict

import toml
from pydantic import BaseModel, BaseSettings


class TomlConfigModel(BaseModel):
    """For fields that doesnt fit in env."""

    taxes: Dict[str, Decimal]
    discounts: Dict[Decimal, Decimal]

    class Config:  # noqa: D106
        allow_population_by_field_name = True
        ignore_extra = True


class Settings(BaseSettings):
    """Env variables."""

    toml_config_path: str = "config.toml"


@lru_cache()
def get_toml_config() -> TomlConfigModel:
    """Retrieve toml config.

    Returns:
        TomlConfigModel: ...
    """
    with open(Settings().toml_config_path, 'r') as f:
        obj = toml.load(f)
        return TomlConfigModel.parse_obj(obj)
