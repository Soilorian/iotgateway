from domain.aggregate.metadata.model.cmd.DirectToCoapCmd import DirectToCoapCmd
from domain.aggregate.metadata.model.dto.coaprequestdto import CoapRequestDto
from domain.aggregate.metadata.model.dto.coapresponsedto import CoapResponseDto
from domain.aggregate.metadata.model.dto.responsedto import ResponseDto
from domain.aggregate.metadata.valueobject.requesttype import Protocol
from infra.di.integration import coap_integration


def direct_to_coap(cmd: DirectToCoapCmd) -> ResponseDto:
    action = cmd.metadata.action
    response: CoapResponseDto

    if cmd.metadata.sender_protocol is Protocol.CoAP:
        response = coap_integration.send_payload(cmd.metadata.original_payload)
    else:
        # Construct the CoAP request
        request = CoapRequestDto(
            method=action,
            path=cmd.metadata.destination_path,
            query_params=cmd,
            headers=cmd.metadata.header,
            body=cmd.metadata.payload,
            port=cmd.destination_port,
            address=cmd.destination_address,
        )

        # Send the request to the CoAP server
        response = coap_integration.send(request)

    # Populate the ResponseDto with the CoAP response data
    return ResponseDto(
        status_code=response.code,
        headers={},  # You can map CoAP specific headers here if needed
        body=response.payload,
        original_response=response,
    )
