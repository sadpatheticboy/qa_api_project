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
        resourse_post = "/maps/api/place/add/json"  # Ресурс метода POST
        url_post = GoogleMapsAPI.BASE_URL + resourse_post + GoogleMapsAPI.PARAMETR_KEY
        print(f" - POST URL: {url_post}")

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
        result_post = HttpMethods.post(url=url_post, body=create_new_place_json)
        print(f" - POST response: {result_post.text}")

        return result_post

    # Метод для получения новой локации
    @staticmethod
    def get_new_place(place_id):
        resourse_get = "/maps/api/place/get/json"  # Ресурс метода GET
        url_get = GoogleMapsAPI.BASE_URL + resourse_get + GoogleMapsAPI.PARAMETR_KEY + "&place_id=" + place_id
        print(f" - GET URL: {url_get}")

        result_get = HttpMethods.get(url=url_get)
        print(f" - GET response: {result_get.text}")

        return result_get

    # Метод для изменения новой локации
    @staticmethod
    def put_new_place(place_id):
        resourse_put = "/maps/api/place/update/json"  # Ресурс метода PUT
        url_put = GoogleMapsAPI.BASE_URL + resourse_put + GoogleMapsAPI.PARAMETR_KEY
        print(f" - PUT URL: {url_put}")

        update_new_location_json = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        result_put = HttpMethods.put(url=url_put, body=update_new_location_json)
        print(f" - PUT response: {result_put.text}")

        return result_put

    # Метод для удаления новой локации
    @staticmethod
    def delete_new_place(place_id):
        resourse_delete = "/maps/api/place/delete/json"  # Ресурс метода DELETE
        url_delete = GoogleMapsAPI.BASE_URL + resourse_delete + GoogleMapsAPI.PARAMETR_KEY
        print(f" - DELETE URL: {url_delete}")

        delete_new_location_json = {
            "place_id": place_id
        }
        result_delete = HttpMethods.put(url=url_delete, body=delete_new_location_json)
        print(f" - DELETE response: {result_delete.text}")

        return result_delete
