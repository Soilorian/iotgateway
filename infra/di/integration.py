from domain.integration.coapintegration import CoapIntegration
from domain.integration.httpintegration import HttpIntegration
from infra.integration.coapintegrationimpl import CoapIntegrationImpl
from infra.integration.httpintegrationimpl import HttpIntegrationImpl

http_integration: HttpIntegration = HttpIntegrationImpl()

coap_integration: CoapIntegration = CoapIntegrationImpl()
