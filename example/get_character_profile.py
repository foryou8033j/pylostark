import sys, pprint, _helper
from pylostark import PyLostark


if __name__ == '__main__':
    api_key = _helper.get_api_key()
    character_name = sys.argv[1]

    raw_profile = PyLostark(api_key=api_key).characters.get(character_name).get_profile()
    pprint.pprint(raw_profile)

