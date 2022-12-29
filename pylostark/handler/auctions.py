from . import ApiRequestHandler


class Auctions(ApiRequestHandler):
    def get_events(self):
        return self._get('/news/events')
