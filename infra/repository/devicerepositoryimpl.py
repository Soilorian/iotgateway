from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port
from domain.aggregate.metadata.valueobject.requesttype import Protocol
from domain.repository.devicerepository import DeviceRepository
from domain.repository.model.dto.devicedto import DeviceDto


class DeviceRepositoryImpl(DeviceRepository):
    devices: list[DeviceDto] = [
        DeviceDto(Address("localhost"), Port(5683), Protocol.HTTP),
    ]

    def get(self,
            address: Address,
            port: Port
            ) -> DeviceDto | None:
        for device in self.devices:
            if device.address.value == address and device.port.value == port:
                return device

        return None

    def add(self,
            address: Address,
            port: Port
            ):
        pass
