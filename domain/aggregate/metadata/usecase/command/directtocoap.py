from domain.aggregate.metadata.model.cmd.DirectToCoapCmd import DirectToCoapCmd
from domain.aggregate.metadata.model.dto.coaprequestdto import CoapRequestDto
from domain.aggregate.metadata.valueobject.requesttype import Protocol
from infra.di.integration import coap_integration


def direct_to_coap(cmd: DirectToCoapCmd):
    action = cmd.metadata.action
    if cmd.metadata.sender_protocol is Protocol.CoAP:
        coap_integration.send_payload(cmd.metadata.original_payload)

    else:
        request = CoapRequestDto(
            method=action,
            path=cmd.metadata.destination_path,
            query_params=cmd,
            headers=cmd.metadata.header,
            body=cmd.metadata.payload,
            port=cmd.destination_port,
            address=cmd.destination_address,
        )

        coap_integration.send(request)
