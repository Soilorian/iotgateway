from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port
from domain.repository.devicerepository import DeviceRepository
from domain.repository.model.dto.devicedto import DeviceDto


class DeviceRepositoryImpl(DeviceRepository):
    def get(self,
            address: Address,
            port: Port
            ) -> DeviceDto:
        pass

    def add(self,
            address: Address,
            port: Port
            ):
        pass

# TODO write simple storage system with array in this class saeed