class MQTTRequest:
    def __init__(self):
        self.fixed_header = None
        self.variable_header = None
        self.payload = None

    def decode(self, raw_data):
        try:
            # Fixed Header (first byte: type and flags)
            self.fixed_header = raw_data[:2]
            message_type = (raw_data[0] >> 4) & 0x0F
            flags = raw_data[0] & 0x0F

            # Remaining Length
            remaining_length = raw_data[1]
            variable_header_start = 2

            # Variable Header and Payload
            self.variable_header = raw_data[variable_header_start:variable_header_start + remaining_length]
            self.payload = raw_data[variable_header_start + remaining_length:]

        except Exception as e:
            raise ValueError(f"Failed to decode MQTT request: {e}")

    def __repr__(self):
        return (
            f"MQTTRequest(fixed_header={self.fixed_header}, variable_header={self.variable_header}, "
            f"payload={self.payload})"
        )
