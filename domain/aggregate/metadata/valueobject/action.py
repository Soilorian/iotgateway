from enum import Enum

class Action(Enum):
    GET = "GET",
    POST = "POST",
    PUT = "PUT",
    DELETE = "DELETE",
    PUBLISH = "PUBLISH",
    SUBSCRIBE = "SUBSCRIBE",
    UNSUBSCRIBE = "UNSUBSCRIBE",

    @staticmethod
    def get_action(value):
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
