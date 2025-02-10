from domain.aggregate.metadata.model.dto.coapresponsedto import CoapResponseDto


def encode_coap_response(dto: CoapResponseDto) -> bytes:
    """
    Encodes the response as a raw CoAP message in bytes.
    """
    # First byte: Version (2 bits), Type (2 bits), Token Length (4 bits)
    token_length = len(dto.token) if dto.token else 0
    first_byte = (dto.version << 6) | (dto.type << 4) | token_length

    # Second byte: Code
    second_byte = dto.code

    # Message ID (2 bytes)
    message_id_bytes = dto.message_id.to_bytes(2, byteorder='big')

    # Token (if any)
    token_bytes = dto.token if dto.token else b''

    # Payload (if any)
    payload_bytes = b'\xFF' + dto.payload.encode('utf-8') if dto.payload else b''

    # Construct final response
    return bytes([first_byte, second_byte]) + message_id_bytes + token_bytes + payload_bytes
