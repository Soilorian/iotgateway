from enum import Enum


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUBLISH = "PUBLISH"
    SUBSCRIBE = "SUBSCRIBE"

    @staticmethod
    def get_method(value):
        if value == "GET":
            return HttpMethod.GET
        elif value == "POST":
            return HttpMethod.POST
