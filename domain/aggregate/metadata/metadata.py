from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.header import Header
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.requesttype import Protocol


class Metadata:
    action: Action
    header: Header
    path: Path
    request_type: Protocol
    payload: Payload

    def __init__(self,
                 action: Action,
                 header: Header,
                 path: Path,
                 request_type: Protocol,
                 payload: Payload):
        self.action = action
        self.header = header
        self.path = path
        self.request_type = request_type
        self.payload = payload
