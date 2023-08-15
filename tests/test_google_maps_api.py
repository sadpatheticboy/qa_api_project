from utils.api import GoogleMapsAPI


class TestCreatePlace:
    """
    Creating, updating and deleting a new location
    """

    def test_create_new_place(self):
        print("\nPOST request:")
        result_post = GoogleMapsAPI.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("\nGET request (after create):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)

        print("\nPUT request:")
        result_put = GoogleMapsAPI.put_new_place(place_id=place_id)

        print("\nGET request (after update):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)

        print("\nDELETE request:")
        result_delete = GoogleMapsAPI.delete_new_place(place_id=place_id)

        print("\nGET request (after delete):")
        result_get = GoogleMapsAPI.get_new_place(place_id=place_id)
