from . import ApiRequestHandler


class Character(ApiRequestHandler):
    def __init__(self, pylostark, raw: dict):
        self._raw = raw
        self.server_name = self._raw.get('ServerName')
        self.character_name = self._raw.get('CharacterName')
        self.character_level = self._raw.get('CharacterLevel')
        self.character_class_name = self._raw.get('CharacterClassName')
        self.item_average_level = float(self._raw.get('ItemAvgLevel').replace(',', ''))
        self.item_max_level = float(self._raw.get('ItemMaxLevel').replace(',', ''))

        super().__init__(pylostark)

    def __repr__(self):
        return f'{self}'

    def __str__(self):
        return f'<{self.server_name}> {self.character_name} ({self.character_class_name})'

    def get_profile(self):
        return self._get(f'/armories/characters/{self.character_name}/profiles')

    def get_equipment(self):
        return self._get(f'/armories/characters/{self.character_name}/equipments')

    def get_avatars(self):
        return self._get(f'/armories/characters/{self.character_name}/avatars')

    def get_combat_skills(self):
        return self._get(f'/armories/characters/{self.character_name}/combat-skills')

    def get_engravings(self):
        return self._get(f'/armories/characters/{self.character_name}/engravings')

    def get_cards(self):
        return self._get(f'/armories/characters/{self.character_name}/cards')

    def get_gems(self):
        return self._get(f'/armories/characters/{self.character_name}/gems')

    def get_colosseums(self):
        return self._get(f'/armories/characters/{self.character_name}/colosseums')

    def get_collectibles(self):
        return self._get(f'/armories/characters/{self.character_name}/collectibles')


class Characters(ApiRequestHandler):
    def __init__(self, pylostark):
        super().__init__(pylostark)

    def get_all(self, character_name) -> dict[str, Character]:
        raw_characters = self._get('/characters/{}/siblings'.format(character_name))
        return {raw_character['CharacterName']: Character(self.pylostark, raw_character) for raw_character in raw_characters}

    def get(self, character_name):
        return self.get_all(character_name).get(character_name)

