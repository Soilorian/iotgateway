class ResponseDto:
    def __init__(self, status_code: int, headers: dict, body: dict | str, original_response, type):
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.original_response = original_response
        self.type = type
