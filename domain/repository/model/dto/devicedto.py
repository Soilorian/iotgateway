from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port
from domain.aggregate.metadata.valueobject.requesttype import Protocol


class DeviceDto:
    address: Address
    port: Port
    protocol: Protocol
    def __init__(self,
                 address: Address,
                 port: Port,
                 protocol: Protocol
                 ):
        self.address = address
        self.port = port
        self.protocol = protocol