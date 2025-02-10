from domain.aggregate.metadata.metadata import Metadata
from domain.aggregate.metadata.model.dto.responsedto import ResponseDto
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port


class SendHttpResponseCmd:
    response: ResponseDto
    destination_address: Address
    destination_port: Port
    metadata: Metadata

    def __init__(self,
                 response: ResponseDto,
                 destination: Address,
                 port: Port,
                 metadata: Metadata
                 ):
        self.destination_address = destination
        self.destination_port = port
        self.metadata = metadata
        self.response = response
