from application.model.request.coaprequest import CoapRequest
from application.model.request.httprequest import HttpRequest
from config.log import logger
from domain.aggregate.metadata.model.cmd.receiveandforwardcmd import ReceiveAndForwardCmd
from domain.aggregate.metadata.model.dto.coapresponsedto import CoapResponseDto
from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto
from domain.aggregate.metadata.usecase.command.receiveandforward import receive_and_forward
from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.header import Header
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.requesttype import Protocol


def consume_http_request(request: HttpRequest) -> HttpResponseDto:
    request_type = Protocol.HTTP
    action = Action.get_action(request.method)
    payload = Payload(request.body)
    path = Path(request.path)
    header = Header(request.headers)
    destination = request.headers["Host"]
    port = request.headers["Port"]

    response = receive_and_forward(
        ReceiveAndForwardCmd(destination=destination, port=port, request_type=request_type, action=action,
                             payload=payload, path=path, header=header, ))

    if isinstance(response.original_response, HttpResponseDto):
        return response.original_response

    return HttpResponseDto(
        status_code=response.status_code,
        headers=response.headers,
        body=response.body,
        original_response=response.original_response
    )


def consume_coap_request(request: CoapRequest) -> CoapResponseDto:
    request_type = Protocol.CoAP
    action = Action.get_action(request.code)
    payload = Payload(request.payload)

    # Extract Uri-Path from options for the path
    path = Path(request.options.get("Uri-Path", ""))  # CoAP path is in Uri-Path option

    header = Header(request.options)  # Treat CoAP options as headers
    destination = request.options.get("Uri-Host", "localhost")  # Extract host if available
    port = request.options.get("Uri-Port", 5683)  # Extract port if available

    response = receive_and_forward(
        ReceiveAndForwardCmd(
            destination=destination,
            port=port,
            request_type=request_type,
            action=action,
            payload=payload,
            path=path,
            header=header,
        )
    )

    if isinstance(response.original_response, CoapResponseDto):
        return response.original_response

    return CoapResponseDto(
        version=request.version,
        type_=request.type,
        code=response.status_code,
        token=request.token,
        message_id=0,
        payload=response.body,
    )


# TODO add amqp consumer to get the amqp request, get its data and call receive and forward, and if needed return a response ostad

# TODO add mqtt consumer to get the amqp request, get its data and call receive and forward, and if needed return a response saeed