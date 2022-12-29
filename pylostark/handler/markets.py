from . import ApiRequestHandler


class Markets(ApiRequestHandler):
    def get_events(self):
        return self._get('/news/events')
