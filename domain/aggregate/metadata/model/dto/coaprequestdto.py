from domain.aggregate.metadata.valueobject import CoapMethod


class CoapRequestDto:
    def __init__(self,
                 method: CoapMethod,
                 path,
                 query_params,
                 headers,
                 body,
                 port,
                 address,
                 ):
        self.method = method
        self.path = path
        self.query_params = query_params
        self.headers = headers
        self.body = body
        self.port = port
        self.address = address
