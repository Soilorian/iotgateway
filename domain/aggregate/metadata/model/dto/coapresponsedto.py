from domain.aggregate.metadata.valueobject.requesttype import Protocol


class CoapResponseDto:
    def __init__(self, version: int, type_: int, code: int, token: bytes, message_id: int, payload: str):
        self.version = version
        self.type = type_
        self.code = code
        self.token = token
        self.message_id = message_id
        self.payload = payload

    @classmethod
    def fromResponse(cls, response):
        if response.type != Protocol.HTTP:
            raise NotImplementedError("Only HTTP to CoAP translation is implemented")

        # Step 1: Map HTTP status code to CoAP code
        http_to_coap_code_map = {
            200: (2 << 5) | 5,   # 2.05 Content
            201: (2 << 5) | 1,   # 2.01 Created
            204: (2 << 5) | 4,   # 2.04 Changed
            400: (4 << 5) | 0,   # 4.00 Bad Request
            404: (4 << 5) | 4,   # 4.04 Not Found
            500: (5 << 5) | 0,   # 5.00 Internal Server Error
        }

        coap_code = http_to_coap_code_map.get(response.status_code, (5 << 5))  # Default to 5.00

        # Step 2: Extract or generate CoAP fields
        version = 1
        type_ = 2  # ACK, assuming this is a response
        token = b'\x00' * 2  # Placeholder (you can improve this)
        message_id = 12345   # Placeholder (should come from original request context)
        payload = response.body if isinstance(response.body, str) else str(response.body)

        return cls(
            version=version,
            type_=type_,
            code=coap_code,
            token=token,
            message_id=message_id,
            payload=payload
        )
