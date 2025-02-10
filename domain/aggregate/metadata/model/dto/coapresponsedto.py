class CoapResponseDto:
    def __init__(self, version: int, type_: int, code: int, token: bytes, message_id: int, payload: str):
        self.version = version
        self.type = type_
        self.code = code
        self.token = token
        self.message_id = message_id
        self.payload = payload
