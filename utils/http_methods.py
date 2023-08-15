import requests


class HttpMethods:
    """
    HTTP-methods list
    """
    HEADERS = {"Content-Type": "application/json"}
    COOKIES = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.HEADERS, cookies=HttpMethods.COOKIES)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.HEADERS, cookies=HttpMethods.COOKIES)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.HEADERS, cookies=HttpMethods.COOKIES)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.HEADERS, cookies=HttpMethods.COOKIES)
        return result
