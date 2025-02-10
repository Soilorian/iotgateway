class HttpResponseDto:
    def __init__(self, status_code: int, headers: dict, body: dict | str, original_response):
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.original_response = original_response

    def is_success(self) -> bool:
        """Returns True if the status code indicates success (2xx)."""
        return 200 <= self.status_code < 300
