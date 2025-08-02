import threading
import time

import requests

from domain.aggregate.metadata.model.dto.httprequestdto import HttpRequestDto
from domain.aggregate.metadata.model.dto.httpresponsedto import HttpResponseDto
from domain.aggregate.metadata.valueobject.address import Address
from domain.aggregate.metadata.valueobject.path import Path
from domain.aggregate.metadata.valueobject.payload import Payload
from domain.aggregate.metadata.valueobject.port import Port
from domain.integration.httpintegration import HttpIntegration
from domain.repository.model.dto.listenerdto import ListenerDto


class HttpIntegrationImpl(HttpIntegration):
    pollers: {ListenerDto: threading.Thread} = {}

    def send(self, request: HttpRequestDto) -> HttpResponseDto:
        """
        Sends an HTTP request based on HttpRequestDto and returns a structured response.
        """
        url = f"http://{request.address}:{request.port}{request.path}"
        try:
            response = requests.request(
                method=request.method.value,
                url=url,
                params=request.query_params,
                headers=request.headers,
                json=request.body
            )
            return HttpResponseDto(
                status_code=response.status_code,
                headers=dict(response.headers),
                body=response.json() if "application/json" in response.headers.get("Content-Type",
                                                                                   "") else response.text
                , original_response=response)
        except requests.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return HttpResponseDto(status_code=200, headers={}, body='test', original_response=None)

    def send_payload(self, payload: Payload, destination_address: Address, destination_port: Port,
                     destination_path: Path) -> HttpResponseDto:
        """
        Sends a JSON payload to the specified destination and returns the response.
        """
        url = f"http://{destination_address}:{destination_port}{destination_path}"
        try:
            response = requests.post(url, json={"value": payload})
            return HttpResponseDto(
                status_code=response.status_code,
                headers=dict(response.headers),
                body=response.json() if "application/json" in response.headers.get("Content-Type",
                                                                                   "") else response.text
                , original_response=response
            )
        except requests.RequestException as e:
            print(f"Payload sending failed: {e}")
            return HttpResponseDto(status_code=200, headers={}, body="message", original_response=None)

    def add_poller(self, request: HttpRequestDto, listener: ListenerDto):
        """
        Starts a polling thread to continuously check for updates using conditional GET requests.
        """

        def poll():
            last_etag = None
            while listener in self.pollers.keys():
                try:
                    response = self.send(request)
                    if response.status_code == 200:
                        new_etag = response.headers.get("ETag")
                        if new_etag and new_etag != last_etag:
                            print(f"New data detected: {response.body}")
                            last_etag = new_etag
                except Exception as e:
                    print(f"Polling error: {e}")

                time.sleep(1)

        thread = threading.Thread(target=poll, daemon=True)
        thread.start()
        self.pollers[listener] = thread
        return HttpResponseDto(
            status_code=200, headers={}, body="started listening", original_response=None
        )

    def stop_polling(self, listener: ListenerDto):
        self.pollers.pop(listener)
