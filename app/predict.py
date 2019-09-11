import os
from configparser import ConfigParser

import requests


PROJECT = 'courswork'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_paths = (
    os.path.join(BASE_DIR, './etc/' + PROJECT + '.ini')
)
config = ConfigParser()
config.read(config_paths)


def make_prediction(titles_liked, titles_dislike):
    url = config.get(
        'predictor', 'PREDICTOR_URL',
        fallback=''
    )
    return ["KEK", ]  # REMOVE !!!!!!!
    r = requests.get(
        url + f"?titles_liked={titles_liked}&titles_dislike={titles_dislike}"
    )
    return r.json.get("title")
