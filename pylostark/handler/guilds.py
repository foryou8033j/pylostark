from . import ApiRequestHandler


class Guilds(ApiRequestHandler):
    def get_rankings(self, server_name: str):
        return self._get('/guilds/rankings', params={
            'serverName': server_name
        })

