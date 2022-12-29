from . import ApiRequestHandler


class News(ApiRequestHandler):
    def get_events(self):
        return self._get('/news/events')
