from domain.aggregate.metadata.model.dto.coaprequestdto import CoapRequestDto
from domain.aggregate.metadata.model.dto.coapresponsedto import CoapResponseDto
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.integration.coapintegration import CoapIntegration


class CoapIntegrationImpl(CoapIntegration):
    def send(self, request: CoapRequestDto) -> CoapResponseDto:
        pass

    def send_payload(self, payload: Payload) -> CoapResponseDto:
        pass

# TODO fill this integration to function ostad