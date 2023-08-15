from requests import Response

from utils.api import GoogleMapsAPI


class TestCreatePlace:
    """
    Creating, updating and deleting a new location
    """

    def test_create_new_place(self):
        print("\nPOST request:")
        result_post: Response = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("\nGET request:")
        result_get: Response = GoogleMapsAPI.get_new_place(place_id)
