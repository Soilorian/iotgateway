from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port
from domain.repository.listenerrepository import ListenerRepository
from domain.repository.model.dto.listenerdto import ListenerDto


class ListenerRepositoryImpl(ListenerRepository):
    def add(self, listenerDto: ListenerDto):
        pass

    def find(self,
             dst_address: Address,
             dst_port: Port
             ) -> [ListenerDto]:
        pass


# TODO write simple storage system with array in this class saeed
