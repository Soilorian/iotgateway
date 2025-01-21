from application.model.request.httprequest import HttpRequest
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.header import Header
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.requesttype import Protocol


def consume_http_request(request: HttpRequest):
    request_type = Protocol.HTTP
    action = Action.get_action(request.method)
    payload = Payload(request.body)
    path = Path(request)
    header = Header(request.headers)
    dest = request.headers["Host"]




