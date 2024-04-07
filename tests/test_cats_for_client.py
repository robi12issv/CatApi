import unittest
from pprint import pprint

from api_requests.cats_for_client import (get_cats_for_client, get_cat_names_for_client,
                                          get_cat_ids_for_client, images_and_ids, vote_image, get_sub_id,
                                          get_votes_by_subid, filter_cats, client)


class TestCatsForClient(unittest.TestCase):

    def test_get_cats_for_client(self):
        cats = get_cats_for_client(client)
        pprint(cats)

    def test_get_cat_names_for_client(self):
        cats = get_cat_names_for_client()
        pprint(cats)

    def test_get_cat_ids_for_client(self):
        cats = get_cat_ids_for_client()
        pprint(cats)

    def test_images_and_ids(self):
        cat, cats = images_and_ids()
        response = list(zip(cat, cats))
        pprint(response)

    def test_vote_image(self):
        cat, cats = vote_image(get_sub_id())
        response = list(zip(cat, cats))
        pprint(response)

    def test_get_votes_by_subid(self):
        response = get_votes_by_subid(get_sub_id())
        pprint(response.json())

    def test_filter_cats(self):
        response = filter_cats()
        pprint(response)
