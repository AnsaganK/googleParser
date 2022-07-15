import os

from database.cities import CITIES
from database.services import SERVICES


def create_cities():
    for city in CITIES:
        city_name = city['name']
        if not os.path.exists(city_name):
            os.mkdir(city)
        _create_services(city_name)


def _create_services(city_name):
    for service in SERVICES:
        service_name = service['name']
        if not os.path.exists(f'{city_name}/{service_name}'):
            os.mkdir(f'{city_name}/{service_name}')


create_cities()
