import requests

from main import (BASE_URL, ALL_BREEDS_URL, VOTES_URL, headers, sub_id, image_id)


def get_an_image():
    response = requests.get(BASE_URL)
    return response.json()


def get_ten_images():
    response = requests.get(BASE_URL + '?limit=20')
    return response.json()


def get_image_with_key():
    response = requests.get(BASE_URL, headers=headers)
    return response.json()


def get_image_link():
    image = get_an_image()
    link = [d['url'] for d in image]
    return link


def get_breeds():
    response = requests.get(ALL_BREEDS_URL)
    return response.json()


def get_specific_breed(breed_name):
    response = requests.get(BASE_URL + '?breed_ids=' + breed_name)
    return response.json()


def get_more_breeds(limit_nr: int, breed_name: str) -> list:
    response = requests.get(BASE_URL + '?limit=' + str(limit_nr) + '&breed_ids=' + breed_name, headers=headers)
    return response.json()


def get_image_by_id():
    response = requests.get('https://api.thecatapi.com/v1/images/' + 'O3F3_S1XN')
    return response.json()


def vote_picture():
    body = {
        "image_id": image_id,
        "sub_id": sub_id,
        "value": 1
    }
    response = requests.post(VOTES_URL, json=body, headers=headers)
    return response.json()


def get_vote():
    response = requests.get(VOTES_URL, headers=headers)
    return response.json()
