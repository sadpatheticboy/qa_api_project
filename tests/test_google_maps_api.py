from requests import Response
from utils.api import GoogleMapsAPI


class TestCreatePlace:
    """
    Creating, updating and deleting a new location
    """

    def test_create_new_place(self):
        print("\nPOST request:")
        result_post: Response = GoogleMapsAPI.create_new_place()
