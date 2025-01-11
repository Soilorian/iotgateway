class Protocol:
    values = [
        "HTTP",
        "COAP",
        "AMQP",
        "MQTT"
    ]

    def __init__(self, value: str):
        if value not in self.values:
            raise ValueError(f"{value} is not a valid protocol")

        self.value = value
