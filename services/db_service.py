import json
import os


def place_save(cid, city, service, base_info, full_info, coordinate, base_photo, reviews, photos) -> dict:
    data = dict()
    data['base_info'] = base_info
    data['full_info'] = full_info
    data['coordinate'] = coordinate
    data['base_photo'] = base_photo
    data['reviews'] = reviews
    data['photos'] = photos
    path = f'cities/{city}/{service}'
    if os.path.exists(path):
        with open(f'{path}/{cid}.json', 'w') as f:
            json.dump(data, f)
    else:
        with open(f'fake_db/{cid}.json', 'w') as f:
            json.dump(data, f)
    return data


def get_search_text():
    pass


def _get_current_city_service():
    pass


def change_current_city_service():
    pass
