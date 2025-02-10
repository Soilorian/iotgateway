from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto


def encode_http_response(dto: HttpResponseDto) -> bytes:
    response_data = (
            f"HTTP/1.1 {dto.status_code} OK\r\n"
            + "".join(f"{key}: {value}\r\n" for key, value in dto.headers.items())
            + "\r\n"
            + (dto.body if isinstance(dto.body, str) else str(dto.body))
    )
    return response_data.encode('utf-8')