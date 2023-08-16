import json


class Checking:
    """
     Methods for checking requests
    """

    # Метод для проверки статус кода
    @staticmethod
    def check_status_code(response, status_code):
        assert status_code == response.status_code, \
            f"Incorrect status code. Expected: {str(status_code)}. Actual: {str(response.status_code)}"
        print(f" - Checking status code. Success: correct status code {str(status_code)}")

    # Метод для проверки наличия обязательных полей в ответе запроса
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, \
            f"Incorrect JSON token. Expected: {expected_value}. Actual: {list(token)}"
        print(" - Checking JSON token. Success. All expected fields are present")

    # Метод для проверки значений обязательных полей в ответе запроса
    @staticmethod
    def check_json_value(response, field_name, expected_value):
        value = response.json()
        check_value = value.get(field_name)
        assert check_value == expected_value, \
            f"Incorrect JSON value. Expected: {expected_value}. Actual: {check_value}"
        print(" - Checking JSON value. Success. Correct value")

    # Метод для проверки значений обязательных полей в ответе запроса по заданному слову
    @staticmethod
    def check_json_value_search(response, field_name, search_value):
        value = response.json()
        check_value = value.get(field_name)
        assert search_value in check_value, \
            f"Incorrect JSON value. Expected: {search_value!r} in {check_value!r}."
        print(" - Checking JSON value search. Success. Value found")
