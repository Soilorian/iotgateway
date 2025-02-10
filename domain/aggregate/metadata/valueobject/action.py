from enum import Enum


class Action(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    FETCH = "FETCH"
    PATCH = "PATCH"
    PUBLISH = "PUBLISH"
    SUBSCRIBE = "SUBSCRIBE"
    UNSUBSCRIBE = "UNSUBSCRIBE"
    DISCOVER = "DISCOVER"

    @staticmethod
    def get_action(value: int):
        # Mapping CoAP numeric method codes to actions
        if value == 1:  # CoAP GET
            return Action.GET
        elif value == 2:  # CoAP POST
            return Action.POST
        elif value == 3:  # CoAP PUT
            return Action.PUT
        elif value == 4:  # CoAP DELETE
            return Action.DELETE
        elif value == 5:  # CoAP FETCH
            return Action.FETCH
        elif value == 6:  # CoAP PATCH
            return Action.PATCH
        elif value == 7:  # CoAP PUBLISH
            return Action.PUBLISH
        elif value == 8:  # CoAP SUBSCRIBE
            return Action.SUBSCRIBE
        elif value == 9:  # CoAP UNSUBSCRIBE
            return Action.UNSUBSCRIBE
        elif value == 11:  # CoAP DISCOVER
            return Action.DISCOVER
        else:
            raise ValueError(f"Unsupported code: {value}")

    @staticmethod
    def get_action(value: str):
        if value == "GET":
            return Action.GET
        elif value == "POST":
            return Action.POST
        elif value == "PUT":
            return Action.PUT
        elif value == "DELETE":
            return Action.DELETE
        elif value == "PUBLISH":
            return Action.PUBLISH
        elif value == "SUBSCRIBE":
            return Action.SUBSCRIBE
        elif value == "UNSUBSCRIBE":
            return Action.UNSUBSCRIBE
        elif value == "DISCOVER":
            return Action.DISCOVER
        elif value == "FETCH":
            return Action.FETCH
        else:
            raise ValueError(f"Unsupported value: {value}")

