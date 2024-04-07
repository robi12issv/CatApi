import random
import requests
from operator import itemgetter

from main import (BASE_URL, ALL_BREEDS_URL, VOTES_URL, headers, dog_params, kids_params)


def get_sub_id(client):
    sub_id = client + '_parent'
    return sub_id


def get_params(*args):
    response = requests.get(ALL_BREEDS_URL)
    param_list = []
    for arg in args:
        param = list([d[arg] for d in response.json()])
        param_list.append(param)
    all_results = (list(zip(*param_list)))
    return all_results


def get_cats_for_client(for_whom):
    if for_whom == 'dog':
        response = get_params(*dog_params)
    else:
        response = get_params(*kids_params)
    correct_list = []
    for cat in response:
        if for_whom == 'dog':
            if itemgetter(2)(cat) == 5 and itemgetter(3)(cat) == 5 and itemgetter(4)(cat) == 5:
                correct_list.append(cat)
        else:
            if itemgetter(1)(cat) == 4 and itemgetter(2)(cat) >= 3 and itemgetter(3)(cat) >= 4 and itemgetter(4)(
                    cat) <= 2 and itemgetter(5)(cat) >= 3:
                correct_list.append(cat)
    return correct_list


def get_cat_names_for_client(client):
    response = get_cats_for_client(client)
    names_list = []
    for cat in response:
        names_list.append(itemgetter(0)(cat))
    return names_list


def get_cat_ids_for_client(client):
    response = get_cats_for_client(client)
    ids_list = []
    for cat in response:
        ids_list.append(itemgetter(1)(cat))
    return ids_list


def extract_links(url):
    cactus = requests.get(url)
    link = [d['url'] for d in cactus.json()]
    return link


def images_and_ids(client):
    response = get_cat_ids_for_client(client)
    cats_images = []
    cats_ids = []
    for cat in response:
        picture_link = extract_links(BASE_URL + '?breed_ids=' + cat)
        for link in picture_link:
            picture = link.split('/')[-1]
            image_id = picture.split('.')[0]
            cats_ids.append(image_id)
            cats_images.append(picture_link)
    return cats_ids, cats_images


def vote_picture(image_id, sub_id):
    body = {
        "image_id": image_id,
        "sub_id": sub_id,
        "value": random.randint(-1, 10)
    }
    response = requests.post(VOTES_URL, json=body, headers=headers)
    return response.json()


def vote_image(sub_id, client):
    cats_ids, cats_images = images_and_ids(client)
    image_id_list = []
    vt_value_list = []
    for image_id in cats_ids:
        vote = vote_picture(image_id, sub_id)
        vt_value = vote['value']
        image_id_list.append(image_id)
        vt_value_list.append(vt_value)
    return image_id_list, vt_value_list


def get_votes_by_subid(sub_id):
    response = requests.get(VOTES_URL + '?sub_id=' + sub_id, headers=headers)
    return response


def filter_cats(client):
    response = get_votes_by_subid(get_sub_id(client))
    best_cats = []
    for cat in response.json():
        value = cat['value']
        image_data = cat['image']
        url = image_data.get('url')
        cats = [value, url]
        if value > 7:
            best_cats.append(cats)
    return best_cats
