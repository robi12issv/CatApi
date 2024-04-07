import unittest
from pprint import pprint

from api_requests.basic_requests import (get_an_image, get_ten_images, get_image_with_key, get_breeds,
                                         get_specific_breed, get_more_breeds, get_image_by_id, vote_picture, get_vote,
                                         get_image_link)

breed_name = 'toyg'


class TestApi(unittest.TestCase):

    def test_get_an_image(self):
        response = get_an_image()
        print(response)

    def test_get_ten_images(self):
        ten_images = get_ten_images()
        pprint(ten_images)

    def test_get_image_with_key(self):
        image_with_key = get_image_with_key()
        pprint(image_with_key)

    def test_get_image_link(self):
        response = get_image_link()
        pprint(response)

    def test_get_breeds(self):
        breed = get_breeds()
        pprint(breed, indent=4)

    def test_get_specific_breed(self):
        breed = get_specific_breed(breed_name)
        pprint(breed, indent=4)

    def test_get_more_breeds(self):
        more_breed = get_more_breeds(3, breed_name)
        print(type(more_breed))
        pprint(more_breed, indent=4)

    def test_get_image_by_id(self):
        image_id = get_image_by_id()
        print(type(image_id))
        pprint(image_id)

    def test_vote_picture(self):
        vote = vote_picture()
        pprint(vote)

    def test_get_vote(self):
        vote = get_vote()
        pprint(vote)
