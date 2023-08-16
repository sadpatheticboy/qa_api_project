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
        Checking.check_json_value(result_post, "status", "OK")

        print("\nGET request (after create):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "29, side layout, cohen 09")

        print("\nPUT request:")
        result_put = GoogleMapsAPI.put_new_place(place_id=place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ["msg"])
        Checking.check_json_value(result_put, "msg", "Address successfully updated")

        print("\nGET request (after update):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])
        Checking.check_json_value(result_get, "address", "100 Lenina street, RU")

        print("\nDELETE request:")
        result_delete = GoogleMapsAPI.delete_new_place(place_id=place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ["status"])
        Checking.check_json_value(result_delete, "status", "OK")

        print("\nGET request (after delete):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_value_search(result_get, "msg", "failed")

        print("\nTesting of creating, updating and deleting a new location was finished successfully.")
