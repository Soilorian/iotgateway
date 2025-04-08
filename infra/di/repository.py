from domain.repository.devicerepository import DeviceRepository
from domain.repository.listenerrepository import ListenerRepository
from infra.repository.devicerepositoryimpl import DeviceRepositoryImpl
from infra.repository.listenerrepositoryimpl import ListenerRepositoryImpl

device_repository: DeviceRepository = DeviceRepositoryImpl()

listener_repository: ListenerRepository = ListenerRepositoryImpl()
