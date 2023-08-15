import json

from utils.api import GoogleMapsAPI
from utils.checking import Checking


class TestCreatePlace:
    """
    Creating, updating and deleting a new location
    """

    def test_create_new_place(self):
        print("\nPOST request:")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        print("\nGET request (after create):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])

        print("\nPUT request:")
        result_put = GoogleMapsAPI.put_new_place(place_id=place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])

        print("\nGET request (after update):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])

        print("\nDELETE request:")
        result_delete = GoogleMapsAPI.delete_new_place(place_id=place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])

        print("\nGET request (after delete):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])

        print("\nTesting of creating, updating and deleting a new location was finished successfully.")
