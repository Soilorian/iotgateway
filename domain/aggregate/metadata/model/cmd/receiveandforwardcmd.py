import string

from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.header import Header
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.port import Port
from domain.aggregate.metadata.valueobject.requesttype import Protocol


class ReceiveAndForwardCmd:
    destination: Address
    port: Port
    request_type: Protocol
    action: Action
    payload: Payload
    path: Path
    header: Header
    sender_addr: string
    raw: string

    def __init__(self,
                 destination: Address,
                 request_type: Protocol,
                 action: Action,
                 payload: Payload,
                 path: Path,
                 header: Header,
                 port: Port,
                 sender_addr: string,
                 raw: string
                 ):
        self.destination = destination
        self.request_type = request_type
        self.action = action
        self.payload = payload
        self.path = path
        self.header = header
        self.port = port
        self.sender_addr = sender_addr
        self.raw = raw
