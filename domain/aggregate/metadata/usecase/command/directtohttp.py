from domain.aggregate.metadata.model.cmd.DirectToHttpCmd import DirectToHttpCmd
from domain.aggregate.metadata.model.dto.httprequestdto import HttpRequestDto
from infra.di.integration import http_integration

def direct_to_http(cmd: DirectToHttpCmd):
    request = HttpRequestDto(
        method=cmd.metadata.action,
        path=cmd.metadata.path,
        query_params=cmd,
        headers=cmd.metadata.header,
        body=cmd.metadata.payload,
        port=cmd.port,
        address=cmd.destination,
    )

    http_integration.send(request)
