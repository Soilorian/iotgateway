from domain.aggregate.metadata.metadata import Metadata
from domain.aggregate.metadata.model.cmd.DirectToHttpCmd import DirectToHttpCmd
from domain.aggregate.metadata.model.cmd.receiveandforwardcmd import ReceiveAndForwardCmd
from domain.aggregate.metadata.usecase.command.directtohttp import direct_to_http
from domain.aggregate.metadata.valueobject.requesttype import Protocol
from infra.di.repository import device_repository


def receive_and_forward(cmd: ReceiveAndForwardCmd):
    device = device_repository.get(address=cmd.destination, port=cmd.port)
    if device is None:
        raise DeviceNotFoundException()

    metadata = Metadata(
        action=cmd.action,
        header=cmd.header,
        path=cmd.path,
        request_type=cmd.request_type,
        payload=cmd.payload,
    )

    if device.protocol == Protocol.HTTP:
        direct_to_http(
            DirectToHttpCmd(
                destination=cmd.destination,
                port=cmd.port,
                metadata=metadata,
            )
        )


class DeviceNotFoundException(Exception):
    def __init__(self):
        super().__init__('Device not found')
