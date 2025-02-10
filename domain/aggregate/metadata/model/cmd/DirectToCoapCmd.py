from domain.aggregate.metadata.metadata import Metadata
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port


class DirectToCoapCmd:
    destination_address: Address
    destination_port: Port
    metadata: Metadata

    def __init__(self,
                 destination: Address,
                 port: Port,
                 metadata: Metadata
                 ):
        self.destination_address = destination
        self.destination_port = port
        self.metadata = metadata
