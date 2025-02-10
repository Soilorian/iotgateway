from domain.aggregate.metadata.model.dto.coaprequestdto import CoapRequestDto
from domain.aggregate.metadata.valueobject.payload import Payload


class CoapIntegration:
    def send(self, request: CoapRequestDto):
        pass

    def send_payload(self, payload: Payload):
        pass
