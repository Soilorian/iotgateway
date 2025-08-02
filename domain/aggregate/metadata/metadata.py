from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.header import Header
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.port import Port
from domain.aggregate.metadata.valueobject.requesttype import Protocol


class Metadata:
    action: Action
    header: Header
    destination_path: Path
    sender_protocol: Protocol
    payload: Payload
    original_payload: Payload
    sender_address: Address
    sender_port: Port

    def __init__(self,
                 action: Action,
                 header: Header,
                 path: Path,
                 request_type: Protocol,
                 payload: Payload,
                 original_payload: Payload,
                 sender_address: Address,
                 sender_port: Port):
        self.action = action
        self.header = header
        self.destination_path = path
        self.sender_protocol = request_type
        self.payload = payload
        self.original_payload = original_payload
        self.sender_address = sender_address
        self.sender_port = sender_port
