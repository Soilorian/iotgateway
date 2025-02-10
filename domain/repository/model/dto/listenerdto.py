from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.port import Port
from domain.aggregate.metadata.valueobject.topic import Topic


class ListenerDto:
    src_address: Address
    dst_address: Address
    src_port: Port
    dst_port: Port
    topic: Topic

    def __init__(self, src_address: Address, dst_address: Address, src_port: Port, dst_port: Port, topic: Topic):
        self.src_address = src_address
        self.dst_address = dst_address
        self.src_port = src_port
        self.dst_port = dst_port
        self.topic = topic
