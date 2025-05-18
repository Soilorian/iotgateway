from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class MQTTResponseDto:
    status_code: int
    headers: Dict[str, Any]
    body: Any
    original_response: Any 