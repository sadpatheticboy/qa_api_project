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
