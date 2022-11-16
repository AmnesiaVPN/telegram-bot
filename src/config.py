import configparser
import pathlib
from dataclasses import dataclass

__all__ = (
    'ROOT_PATH',
    'BotConfig',
    'Config',
    'DonationAlertsConfig',
    'load_config',
)

ROOT_PATH = pathlib.Path(__file__).parent.parent


@dataclass(frozen=True, slots=True)
class BotConfig:
    token: str


@dataclass(frozen=True, slots=True)
class ServerAPIConfig:
    base_url: str


@dataclass(frozen=True, slots=True)
class DonationAlertsConfig:
    payment_page_url: str


@dataclass(frozen=True, slots=True)
class Config:
    bot: BotConfig
    server_api: ServerAPIConfig
    donationalerts: DonationAlertsConfig


def load_config(file_path: str | pathlib.Path) -> Config:
    config = configparser.ConfigParser()
    config.read(file_path)

    bot_config = config['telegram_bot']
    server_api_config = config['server_api']
    donationalerts_config = config['donationalerts']

    return Config(
        bot=BotConfig(
            token=bot_config.get('token'),
        ),
        server_api=ServerAPIConfig(
            base_url=server_api_config.get('base_url'),
        ),
        donationalerts=DonationAlertsConfig(
            payment_page_url=donationalerts_config.get('payment_page_url'),
        ),
    )
