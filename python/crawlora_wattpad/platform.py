"""Platform-specific convenience clients."""
from __future__ import annotations
from typing import Any
from .client import CrawloraClient
from .async_client import AsyncCrawloraClient

class WattpadClient(CrawloraClient):
    """Synchronous Wattpad API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-wattpad-python/0.1.0')
        super().__init__(*args, **kwargs)

    def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    def languages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-languages', params, response_type=response_type, timeout=timeout, headers=headers)

    def part(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-part', params, response_type=response_type, timeout=timeout, headers=headers)

    def part_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-part-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-search', params, response_type=response_type, timeout=timeout, headers=headers)

    def search_users(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-search-users', params, response_type=response_type, timeout=timeout, headers=headers)

    def story(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-story', params, response_type=response_type, timeout=timeout, headers=headers)

    def story_parts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-story-parts', params, response_type=response_type, timeout=timeout, headers=headers)

    def story_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-story-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    def user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-user', params, response_type=response_type, timeout=timeout, headers=headers)

    def user_stories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return self.request('wattpad-user-stories', params, response_type=response_type, timeout=timeout, headers=headers)

class AsyncWattpadClient(AsyncCrawloraClient):
    """Asynchronous Wattpad API client."""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs.setdefault('user_agent', 'crawlora-wattpad-python/0.1.0')
        super().__init__(*args, **kwargs)

    async def categories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-categories', params, response_type=response_type, timeout=timeout, headers=headers)

    async def languages(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-languages', params, response_type=response_type, timeout=timeout, headers=headers)

    async def part(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-part', params, response_type=response_type, timeout=timeout, headers=headers)

    async def part_comments(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-part-comments', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-search', params, response_type=response_type, timeout=timeout, headers=headers)

    async def search_users(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-search-users', params, response_type=response_type, timeout=timeout, headers=headers)

    async def story(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-story', params, response_type=response_type, timeout=timeout, headers=headers)

    async def story_parts(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-story-parts', params, response_type=response_type, timeout=timeout, headers=headers)

    async def story_recommendations(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-story-recommendations', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-user', params, response_type=response_type, timeout=timeout, headers=headers)

    async def user_stories(self, **params: Any) -> Any:
        response_type = params.pop('_response_type', 'auto')
        timeout = params.pop('_timeout', None)
        headers = params.pop('_headers', None)
        return await self.request('wattpad-user-stories', params, response_type=response_type, timeout=timeout, headers=headers)
