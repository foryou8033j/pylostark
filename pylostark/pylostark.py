from .handler.news import News
from .handler.characters import Characters
from .handler.auctions import Auctions
from .handler.guilds import Guilds
from .handler.markets import Markets


class PyLostark:
    def __init__(self, api_key=None, region=None, language=None):
        self.api_key = api_key
        self.region = region
        self.language = language
        self._url = 'https://developer-lostark.game.onstove.com/'

    @property
    def headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}',
        }

    @property
    def news(self):
        return News(self)

    @property
    def characters(self):
        return Characters(self)

    @property
    def auctions(self):
        return Auctions(self)

    @property
    def guilds(self):
        return Guilds(self)

    @property
    def markets(self):
        return Markets(self)
