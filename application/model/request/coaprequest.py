class CoAPRequest:
    def __init__(self):
        self.version = None
        self.type = None
        self.token = None
        self.code = None
        self.payload = None
        self.options = {}

    def decode(self, raw_data):
        """
        Decodes raw CoAP request data (in bytes) and populates the class attributes.
        """
        if len(raw_data) < 4:
            raise ValueError("Invalid CoAP request: insufficient data")

        # First byte: Version, Type, Token Length
        first_byte = raw_data[0]
        self.version = (first_byte >> 6) & 0x03
        self.type = (first_byte >> 4) & 0x03
        token_length = first_byte & 0x0F

        # Second byte: Code
        self.code = raw_data[1]

        # Message ID
        message_id = (raw_data[2] << 8) | raw_data[3]

        # Token (if any)
        if token_length > 0:
            self.token = raw_data[4:4 + token_length]
        else:
            self.token = None

        # Options and Payload
        options_start = 4 + token_length
        payload_marker = raw_data.find(b'\xFF', options_start)
        if payload_marker != -1:
            self.payload = raw_data[payload_marker + 1:].decode('utf-8', errors='ignore')
        else:
            self.payload = None

        # Options parsing (basic implementation)
        self.options = {}  # Extend this to parse CoAP options as needed

    def __repr__(self):
        return (
            f"CoAPRequest(version={self.version}, type={self.type}, token={self.token}, "
            f"code={self.code}, payload={self.payload}, options={self.options})"
        )
