from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto


def encode_http_response(dto: HttpResponseDto) -> bytes:
    # Reason phrase mapping (optional, more precise than hardcoding "OK")
    reason_phrases = {
        200: "OK",
        400: "Bad Request",
        404: "Not Found",
        500: "Internal Server Error"
    }

    reason = reason_phrases.get(dto.status_code, "OK")

    # Convert headers to string
    headers_string = "".join(f"{key}: {value}\r\n" for key, value in dto.headers.items())

    # Serialize body safely
    if isinstance(dto.body, (str, bytes)):
        body_content = dto.body if isinstance(dto.body, str) else dto.body.decode('utf-8', errors='replace')
    else:
        # fallback to string representation
        body_content = dto.body

    # Construct the full HTTP response string
    response_data = (
        f"HTTP/1.1 {dto.status_code} {reason}\r\n"
        f"{headers_string}\r\n"
        f"{body_content}"
    )

    return response_data.encode("utf-8")
