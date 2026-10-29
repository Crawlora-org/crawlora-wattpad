"""Typed Wattpad client for the Crawlora hosted API."""

from .platform import WattpadClient, AsyncWattpadClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = WattpadClient
AsyncClient = AsyncWattpadClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Wattpad'
PLATFORM = 'wattpad'
CONTRACT_REVISION = 'sha256:0a05aa59778d80a0ee980e309da1cb454ba2040754e8c8a27594ad903b0b5320'

__all__ = [
    "WattpadClient", "AsyncWattpadClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
