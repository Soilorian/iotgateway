from domain.aggregate.metadata.model.dto.httprequestdto import HttpRequestDto
from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.port import Port


class HttpIntegration:
    def send(self, request: HttpRequestDto) -> HttpResponseDto:
        pass

    def send_payload(self, payload: Payload, destination_address: Address, destination_port: Port,
                     destination_path: Path) -> HttpResponseDto:
        pass

    def add_poller(self, request: HttpRequestDto) -> HttpResponseDto:
        pass
