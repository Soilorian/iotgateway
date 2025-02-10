from domain.aggregate.metadata.model.cmd.DirectToHttpCmd import DirectToHttpCmd
from domain.aggregate.metadata.model.dto.httprequestdto import HttpRequestDto
from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto
from domain.aggregate.metadata.model.dto.responsedto import ResponseDto
from domain.aggregate.metadata.valueobject.HttpMethod import HttpMethod
from domain.aggregate.metadata.valueobject.action import Action
from domain.aggregate.metadata.valueobject.requesttype import Protocol
from domain.aggregate.metadata.valueobject.topic import Topic
from domain.repository.model.dto.listenerdto import ListenerDto
from infra.di.integration import http_integration
from infra.di.repository import listener_repository


def direct_to_http(cmd: DirectToHttpCmd) -> HttpResponseDto:
    response: HttpResponseDto
    action = cmd.metadata.action
    if cmd.metadata.sender_protocol is Protocol.HTTP:
        response = http_integration.send_payload(cmd.metadata.original_payload,
                                                 destination_address=cmd.destination_address,
                                                 destination_port=cmd.destination_port,
                                                 destination_path=cmd.metadata.destination_path)

    elif action in [Action.GET, Action.POST, Action.PUT, Action.PATCH, Action.DELETE]:
        request = HttpRequestDto(
            method=action,
            path=cmd.metadata.destination_path,
            query_params=cmd,
            headers=cmd.metadata.header,
            body=cmd.metadata.payload,
            port=cmd.destination_port,
            address=cmd.destination_address,
        )

        response = http_integration.send(request)

    elif action is Action.FETCH:
        request = HttpRequestDto(
            method=Action.GET,
            path=cmd.metadata.destination_path,
            query_params=cmd,
            headers=cmd.metadata.header,
            body=cmd.metadata.payload,
            port=cmd.destination_port,
            address=cmd.destination_address,
        )

        response = http_integration.send(request)

    elif action is Action.DISCOVER:
        request = HttpRequestDto(
            method=Action.GET,
            path="\\topics",
            query_params=cmd,
            headers=cmd.metadata.header,
            body=cmd.metadata.payload,
            port=cmd.destination_port,
            address=cmd.destination_address,
        )

        response = http_integration.send(request)
    else:
        topic = Topic(cmd.metadata.destination_path.value)
        if action is Action.SUBSCRIBE:
            listener = ListenerDto(
                src_address=cmd.metadata.sender_address,
                dst_address=cmd.destination_address,
                src_port=cmd.metadata.sender_port,
                dst_port=cmd.destination_port,
                topic=topic
            )

            listener_repository.add(listener)
            request = HttpRequestDto(
                method=HttpMethod.get_method(cmd.metadata.action.value),
                path=cmd.metadata.destination_path,
                query_params=cmd,
                headers=cmd.metadata.header,
                body=cmd.metadata.payload,
                port=cmd.destination_port,
                address=cmd.destination_address,
            )

            response = http_integration.add_poller(
                request=request,
                listener=listener,
            )

        elif action is Action.PUBLISH:
            listeners = listener_repository.find(
                dst_address=cmd.destination_address,
                dst_port=cmd.destination_port,
            )

            if find_listener(listeners=listeners, src_port=cmd.metadata.sender_port,
                             src_address=cmd.metadata.sender_address,
                             topic=Topic(cmd.metadata.destination_path.value)) is not None:
                request = HttpRequestDto(
                    method=HttpMethod.POST,
                    path=cmd.metadata.destination_path,
                    query_params=cmd,
                    headers=cmd.metadata.header,
                    body=cmd.metadata.payload,
                    port=cmd.destination_port,
                    address=cmd.destination_address,
                )

                response = http_integration.send(request)

        elif action is Action.UNSUBSCRIBE:
            listeners = listener_repository.find(
                dst_address=cmd.destination_address,
                dst_port=cmd.destination_port,
            )

            listener = find_listener(listeners=listeners, src_port=cmd.metadata.sender_port,
                             src_address=cmd.metadata.sender_address,
                             topic=Topic(cmd.metadata.destination_path.value))

            if listener:
                http_integration.stop_polling(listener)

        else:
            raise NotImplemented

    return response


def find_listener(listeners, src_port, src_address, topic):
    return next(
        (listener for listener in listeners
         if listener.src_port == src_port and
         listener.src_address == src_address and
         listener.topic == topic),
        None  # Return None if no match is found
    )
