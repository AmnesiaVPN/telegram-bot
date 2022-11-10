import configparser
import pathlib
from dataclasses import dataclass

__all__ = (
    'BotConfig',
    'Config',
    'load_config',
)


@dataclass(frozen=True, slots=True)
class BotConfig:
    token: str


@dataclass(frozen=True, slots=True)
class Config:
    bot: BotConfig


def load_config(file_path: str | pathlib.Path) -> Config:
    config = configparser.ConfigParser()
    config.read(file_path)

    bot_config = config['telegram_bot']

    return Config(
        bot=BotConfig(
            token=bot_config.get('token'),
        ),
    )
