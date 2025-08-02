from pip._vendor.cachecontrol import adapter

from application.model.request.httprequest import HttpRequest


def extract_port(request: HttpRequest):
    return 80