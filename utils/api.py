from utils.http_methods import HttpMethods


class GoogleMapsAPI:
    """
    Methods for testing Google Maps API
    """

    BASE_URL = "https://rahulshettyacademy.com"  # Базовая URL
    PARAMETR_KEY = "?key=qaclick123"  # Параметр для всех запросов

    # Метод для создания новой локации
    @staticmethod
    def create_new_place():
        create_new_place_json = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "https://google.com",
            "language": "French-IN"
        }

        resourse_post = "/maps/api/place/add/json"  # Ресурс метода POST
        url_post = GoogleMapsAPI.BASE_URL + resourse_post + GoogleMapsAPI.PARAMETR_KEY
        print(f" - POST URL: {url_post}")

        result_post = HttpMethods.post(url=url_post, body=create_new_place_json)
        print(f" - POST response: {result_post.text}")

        return result_post

    # Метод для получения новой локации
    @staticmethod
    def get_new_place(place_id):
        resourse_get = "/maps/api/place/get/json"  # Ресурс метода GET
        url_get = GoogleMapsAPI.BASE_URL + resourse_get + GoogleMapsAPI.PARAMETR_KEY + "&place_id=" + place_id
        print(f" - GET URL: {url_get}")

        result_get = HttpMethods.get(url_get)
        print(f" - GET response: {result_get.text}")

        return result_get
