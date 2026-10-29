from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelWattpadUserStoriesResponseDoc = TypedDict('ModelWattpadUserStoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadUserStoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadUserStoriesResponse = TypedDict('ModelWattpadUserStoriesResponse', {
    'limit': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'stories': NotRequired[list[ModelWattpadStory]],
    'total': NotRequired[int],
    'username': NotRequired[str],
}, total=False)

ModelWattpadStory = TypedDict('ModelWattpadStory', {
    'author': NotRequired[ModelWattpadAuthor],
    'category_ids': NotRequired[list[int]],
    'comments': NotRequired[int],
    'completed': NotRequired[bool],
    'cover': NotRequired[str],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'id': NotRequired[str],
    'language': NotRequired[ModelWattpadLanguage],
    'mature': NotRequired[bool],
    'modified_at': NotRequired[str],
    'parts': NotRequired[int],
    'reads': NotRequired[int],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'votes': NotRequired[int],
}, total=False)

ModelWattpadLanguage = TypedDict('ModelWattpadLanguage', {
    'id': NotRequired[int],
    'name': NotRequired[str],
}, total=False)

ModelWattpadAuthor = TypedDict('ModelWattpadAuthor', {
    'avatar': NotRequired[str],
    'name': NotRequired[str],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelWattpadUserResponseDoc = TypedDict('ModelWattpadUserResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadUserResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadUserResponse = TypedDict('ModelWattpadUserResponse', {
    'user': NotRequired[ModelWattpadUserProfile],
}, total=False)

ModelWattpadUserProfile = TypedDict('ModelWattpadUserProfile', {
    'ambassador': NotRequired[bool],
    'avatar': NotRequired[str],
    'background': NotRequired[str],
    'description': NotRequired[str],
    'followers': NotRequired[int],
    'following': NotRequired[int],
    'joined_at': NotRequired[str],
    'lists': NotRequired[int],
    'location': NotRequired[str],
    'modified_at': NotRequired[str],
    'name': NotRequired[str],
    'stories_published': NotRequired[int],
    'url': NotRequired[str],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
    'votes_received': NotRequired[int],
    'website': NotRequired[str],
}, total=False)

ModelWattpadRecommendationsResponseDoc = TypedDict('ModelWattpadRecommendationsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadRecommendationsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadRecommendationsResponse = TypedDict('ModelWattpadRecommendationsResponse', {
    'stories': NotRequired[list[ModelWattpadStory]],
    'story_id': NotRequired[str],
}, total=False)

ModelWattpadStoryPartsResponseDoc = TypedDict('ModelWattpadStoryPartsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadStoryPartsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadStoryPartsResponse = TypedDict('ModelWattpadStoryPartsResponse', {
    'parts': NotRequired[list[ModelWattpadPart]],
    'story_id': NotRequired[str],
    'title': NotRequired[str],
    'total': NotRequired[int],
}, total=False)

ModelWattpadPart = TypedDict('ModelWattpadPart', {
    'comments': NotRequired[int],
    'created_at': NotRequired[str],
    'draft': NotRequired[bool],
    'id': NotRequired[str],
    'length': NotRequired[int],
    'modified_at': NotRequired[str],
    'reads': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'votes': NotRequired[int],
    'word_count': NotRequired[int],
}, total=False)

ModelWattpadStoryResponseDoc = TypedDict('ModelWattpadStoryResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadStoryResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadStoryResponse = TypedDict('ModelWattpadStoryResponse', {
    'story': NotRequired[ModelWattpadStoryDetail],
}, total=False)

ModelWattpadStoryDetail = TypedDict('ModelWattpadStoryDetail', {
    'author': NotRequired[ModelWattpadAuthor],
    'category_ids': NotRequired[list[int]],
    'comments': NotRequired[int],
    'completed': NotRequired[bool],
    'copyright': NotRequired[int],
    'cover': NotRequired[str],
    'created_at': NotRequired[str],
    'description': NotRequired[str],
    'first_part_id': NotRequired[str],
    'id': NotRequired[str],
    'language': NotRequired[ModelWattpadLanguage],
    'last_published_at': NotRequired[str],
    'mature': NotRequired[bool],
    'modified_at': NotRequired[str],
    'paid_model': NotRequired[str],
    'parts': NotRequired[int],
    'paywalled': NotRequired[bool],
    'rating': NotRequired[int],
    'reads': NotRequired[int],
    'tags': NotRequired[list[str]],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'votes': NotRequired[int],
}, total=False)

ModelWattpadSearchUsersResponseDoc = TypedDict('ModelWattpadSearchUsersResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadSearchUsersResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadSearchUsersResponse = TypedDict('ModelWattpadSearchUsersResponse', {
    'limit': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'users': NotRequired[list[ModelWattpadUserSummary]],
}, total=False)

ModelWattpadUserSummary = TypedDict('ModelWattpadUserSummary', {
    'avatar': NotRequired[str],
    'description': NotRequired[str],
    'followers': NotRequired[int],
    'name': NotRequired[str],
    'stories_published': NotRequired[int],
    'username': NotRequired[str],
    'verified': NotRequired[bool],
}, total=False)

ModelWattpadSearchResponseDoc = TypedDict('ModelWattpadSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadSearchResponse = TypedDict('ModelWattpadSearchResponse', {
    'limit': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'stories': NotRequired[list[ModelWattpadStory]],
    'total': NotRequired[int],
}, total=False)

ModelWattpadPartCommentsResponseDoc = TypedDict('ModelWattpadPartCommentsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadPartCommentsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadPartCommentsResponse = TypedDict('ModelWattpadPartCommentsResponse', {
    'comments': NotRequired[list[ModelWattpadComment]],
    'limit': NotRequired[int],
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'part_id': NotRequired[str],
}, total=False)

ModelWattpadComment = TypedDict('ModelWattpadComment', {
    'author': NotRequired[str],
    'author_avatar': NotRequired[str],
    'body': NotRequired[str],
    'created_at': NotRequired[str],
    'id': NotRequired[str],
    'is_reply': NotRequired[bool],
    'parent_id': NotRequired[str],
    'replies': NotRequired[int],
    'url': NotRequired[str],
}, total=False)

ModelWattpadPartResponseDoc = TypedDict('ModelWattpadPartResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadPartResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadPartResponse = TypedDict('ModelWattpadPartResponse', {
    'part': NotRequired[ModelWattpadPartDetail],
}, total=False)

ModelWattpadPartDetail = TypedDict('ModelWattpadPartDetail', {
    'comments': NotRequired[int],
    'created_at': NotRequired[str],
    'draft': NotRequired[bool],
    'id': NotRequired[str],
    'length': NotRequired[int],
    'modified_at': NotRequired[str],
    'reads': NotRequired[int],
    'story_id': NotRequired[str],
    'story_title': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'votes': NotRequired[int],
    'word_count': NotRequired[int],
}, total=False)

ModelWattpadLanguagesResponseDoc = TypedDict('ModelWattpadLanguagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadLanguagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadLanguagesResponse = TypedDict('ModelWattpadLanguagesResponse', {
    'languages': NotRequired[list[ModelWattpadLanguage]],
}, total=False)

ModelWattpadCategoriesResponseDoc = TypedDict('ModelWattpadCategoriesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelWattpadCategoriesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelWattpadCategoriesResponse = TypedDict('ModelWattpadCategoriesResponse', {
    'categories': NotRequired[list[ModelWattpadCategory]],
}, total=False)

ModelWattpadCategory = TypedDict('ModelWattpadCategory', {
    'id': NotRequired[int],
    'name': NotRequired[str],
    'name_english': NotRequired[str],
}, total=False)

WattpadCategoriesResponse = ModelWattpadCategoriesResponseDoc
WattpadCategoriesParams = TypedDict('WattpadCategoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

WattpadLanguagesResponse = ModelWattpadLanguagesResponseDoc
WattpadLanguagesParams = TypedDict('WattpadLanguagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
}, total=False)

WattpadPartResponse = ModelWattpadPartResponseDoc
WattpadPartParams = TypedDict('WattpadPartParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'part_id': Required[str],
}, total=False)

WattpadPartCommentsResponse = ModelWattpadPartCommentsResponseDoc
WattpadPartCommentsParams = TypedDict('WattpadPartCommentsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'part_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchResponse = ModelWattpadSearchResponseDoc
WattpadSearchParams = TypedDict('WattpadSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': NotRequired[str],
    'filter': NotRequired[Literal['hot', 'new', 'featured']],
    'category': NotRequired[int],
    'language': NotRequired[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '46', '47', '48', '49', '50', '51', '53']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchUsersResponse = ModelWattpadSearchUsersResponseDoc
WattpadSearchUsersParams = TypedDict('WattpadSearchUsersParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'query': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadStoryResponse = ModelWattpadStoryResponseDoc
WattpadStoryParams = TypedDict('WattpadStoryParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'story_id': Required[str],
}, total=False)

WattpadStoryPartsResponse = ModelWattpadStoryPartsResponseDoc
WattpadStoryPartsParams = TypedDict('WattpadStoryPartsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'story_id': Required[str],
}, total=False)

WattpadStoryRecommendationsResponse = ModelWattpadRecommendationsResponseDoc
WattpadStoryRecommendationsParams = TypedDict('WattpadStoryRecommendationsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'story_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

WattpadUserResponse = ModelWattpadUserResponseDoc
WattpadUserParams = TypedDict('WattpadUserParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
}, total=False)

WattpadUserStoriesResponse = ModelWattpadUserStoriesResponseDoc
WattpadUserStoriesParams = TypedDict('WattpadUserStoriesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'username': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

class WattpadGroup:
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesDefaultParams]) -> WattpadCategoriesResponse: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesTextResponseParams]) -> str: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesDefaultParams]) -> WattpadLanguagesResponse: ...
    @overload
    def part(self, **params: Unpack[WattpadPartStreamParams]) -> BinaryIO: ...
    @overload
    def part(self, **params: Unpack[WattpadPartTextResponseParams]) -> str: ...
    @overload
    def part(self, **params: Unpack[WattpadPartDefaultParams]) -> WattpadPartResponse: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsTextResponseParams]) -> str: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsDefaultParams]) -> WattpadPartCommentsResponse: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchDefaultParams]) -> WattpadSearchResponse: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersStreamParams]) -> BinaryIO: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersTextResponseParams]) -> str: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersDefaultParams]) -> WattpadSearchUsersResponse: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryStreamParams]) -> BinaryIO: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryTextResponseParams]) -> str: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryDefaultParams]) -> WattpadStoryResponse: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsStreamParams]) -> BinaryIO: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsTextResponseParams]) -> str: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsDefaultParams]) -> WattpadStoryPartsResponse: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsTextResponseParams]) -> str: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsDefaultParams]) -> WattpadStoryRecommendationsResponse: ...
    @overload
    def user(self, **params: Unpack[WattpadUserStreamParams]) -> BinaryIO: ...
    @overload
    def user(self, **params: Unpack[WattpadUserTextResponseParams]) -> str: ...
    @overload
    def user(self, **params: Unpack[WattpadUserDefaultParams]) -> WattpadUserResponse: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesStreamParams]) -> BinaryIO: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesTextResponseParams]) -> str: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesDefaultParams]) -> WattpadUserStoriesResponse: ...

OperationId = Literal[
    'wattpad-categories',
    'wattpad-languages',
    'wattpad-part',
    'wattpad-part-comments',
    'wattpad-search',
    'wattpad-search-users',
    'wattpad-story',
    'wattpad-story-parts',
    'wattpad-story-recommendations',
    'wattpad-user',
    'wattpad-user-stories',
]

class CrawloraClient:
    wattpad: WattpadGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-categories'],
        params: WattpadCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadCategoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-languages'],
        params: WattpadLanguagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadLanguagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-part'],
        params: WattpadPartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadPartResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-part-comments'],
        params: WattpadPartCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadPartCommentsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-search'],
        params: WattpadSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-search-users'],
        params: WattpadSearchUsersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadSearchUsersResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-story'],
        params: WattpadStoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-story-parts'],
        params: WattpadStoryPartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryPartsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-story-recommendations'],
        params: WattpadStoryRecommendationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryRecommendationsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-user'],
        params: WattpadUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadUserResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['wattpad-user-stories'],
        params: WattpadUserStoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadUserStoriesResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-categories'],
        params: WattpadCategoriesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadCategoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-languages'],
        params: WattpadLanguagesParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadLanguagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-part'],
        params: WattpadPartParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadPartResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-part-comments'],
        params: WattpadPartCommentsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadPartCommentsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-search'],
        params: WattpadSearchParams = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-search-users'],
        params: WattpadSearchUsersParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadSearchUsersResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-story'],
        params: WattpadStoryParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-story-parts'],
        params: WattpadStoryPartsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryPartsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-story-recommendations'],
        params: WattpadStoryRecommendationsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadStoryRecommendationsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-user'],
        params: WattpadUserParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadUserResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['wattpad-user-stories'],
        params: WattpadUserStoriesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> WattpadUserStoriesResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class WattpadClient(CrawloraClient):
    def __enter__(self) -> WattpadClient: ...
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesTextResponseParams]) -> str: ...
    @overload
    def categories(self, **params: Unpack[WattpadCategoriesDefaultParams]) -> WattpadCategoriesResponse: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesTextResponseParams]) -> str: ...
    @overload
    def languages(self, **params: Unpack[WattpadLanguagesDefaultParams]) -> WattpadLanguagesResponse: ...
    @overload
    def part(self, **params: Unpack[WattpadPartStreamParams]) -> BinaryIO: ...
    @overload
    def part(self, **params: Unpack[WattpadPartTextResponseParams]) -> str: ...
    @overload
    def part(self, **params: Unpack[WattpadPartDefaultParams]) -> WattpadPartResponse: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsStreamParams]) -> BinaryIO: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsTextResponseParams]) -> str: ...
    @overload
    def part_comments(self, **params: Unpack[WattpadPartCommentsDefaultParams]) -> WattpadPartCommentsResponse: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[WattpadSearchDefaultParams]) -> WattpadSearchResponse: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersStreamParams]) -> BinaryIO: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersTextResponseParams]) -> str: ...
    @overload
    def search_users(self, **params: Unpack[WattpadSearchUsersDefaultParams]) -> WattpadSearchUsersResponse: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryStreamParams]) -> BinaryIO: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryTextResponseParams]) -> str: ...
    @overload
    def story(self, **params: Unpack[WattpadStoryDefaultParams]) -> WattpadStoryResponse: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsStreamParams]) -> BinaryIO: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsTextResponseParams]) -> str: ...
    @overload
    def story_parts(self, **params: Unpack[WattpadStoryPartsDefaultParams]) -> WattpadStoryPartsResponse: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsTextResponseParams]) -> str: ...
    @overload
    def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsDefaultParams]) -> WattpadStoryRecommendationsResponse: ...
    @overload
    def user(self, **params: Unpack[WattpadUserStreamParams]) -> BinaryIO: ...
    @overload
    def user(self, **params: Unpack[WattpadUserTextResponseParams]) -> str: ...
    @overload
    def user(self, **params: Unpack[WattpadUserDefaultParams]) -> WattpadUserResponse: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesStreamParams]) -> BinaryIO: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesTextResponseParams]) -> str: ...
    @overload
    def user_stories(self, **params: Unpack[WattpadUserStoriesDefaultParams]) -> WattpadUserStoriesResponse: ...

class AsyncWattpadClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncWattpadClient: ...
    wattpad: _AsyncWattpadGroup
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesDefaultParams]) -> WattpadCategoriesResponse: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesTextResponseParams]) -> str: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesDefaultParams]) -> WattpadLanguagesResponse: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartStreamParams]) -> BinaryIO: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartTextResponseParams]) -> str: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartDefaultParams]) -> WattpadPartResponse: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsTextResponseParams]) -> str: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsDefaultParams]) -> WattpadPartCommentsResponse: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchDefaultParams]) -> WattpadSearchResponse: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersStreamParams]) -> BinaryIO: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersTextResponseParams]) -> str: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersDefaultParams]) -> WattpadSearchUsersResponse: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryStreamParams]) -> BinaryIO: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryTextResponseParams]) -> str: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryDefaultParams]) -> WattpadStoryResponse: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsStreamParams]) -> BinaryIO: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsTextResponseParams]) -> str: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsDefaultParams]) -> WattpadStoryPartsResponse: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsDefaultParams]) -> WattpadStoryRecommendationsResponse: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserStreamParams]) -> BinaryIO: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserTextResponseParams]) -> str: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserDefaultParams]) -> WattpadUserResponse: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesTextResponseParams]) -> str: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesDefaultParams]) -> WattpadUserStoriesResponse: ...

class _AsyncWattpadGroup:
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesTextResponseParams]) -> str: ...
    @overload
    async def categories(self, **params: Unpack[WattpadCategoriesDefaultParams]) -> WattpadCategoriesResponse: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesStreamParams]) -> BinaryIO: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesTextResponseParams]) -> str: ...
    @overload
    async def languages(self, **params: Unpack[WattpadLanguagesDefaultParams]) -> WattpadLanguagesResponse: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartStreamParams]) -> BinaryIO: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartTextResponseParams]) -> str: ...
    @overload
    async def part(self, **params: Unpack[WattpadPartDefaultParams]) -> WattpadPartResponse: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsStreamParams]) -> BinaryIO: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsTextResponseParams]) -> str: ...
    @overload
    async def part_comments(self, **params: Unpack[WattpadPartCommentsDefaultParams]) -> WattpadPartCommentsResponse: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[WattpadSearchDefaultParams]) -> WattpadSearchResponse: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersStreamParams]) -> BinaryIO: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersTextResponseParams]) -> str: ...
    @overload
    async def search_users(self, **params: Unpack[WattpadSearchUsersDefaultParams]) -> WattpadSearchUsersResponse: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryStreamParams]) -> BinaryIO: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryTextResponseParams]) -> str: ...
    @overload
    async def story(self, **params: Unpack[WattpadStoryDefaultParams]) -> WattpadStoryResponse: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsStreamParams]) -> BinaryIO: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsTextResponseParams]) -> str: ...
    @overload
    async def story_parts(self, **params: Unpack[WattpadStoryPartsDefaultParams]) -> WattpadStoryPartsResponse: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsStreamParams]) -> BinaryIO: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsTextResponseParams]) -> str: ...
    @overload
    async def story_recommendations(self, **params: Unpack[WattpadStoryRecommendationsDefaultParams]) -> WattpadStoryRecommendationsResponse: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserStreamParams]) -> BinaryIO: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserTextResponseParams]) -> str: ...
    @overload
    async def user(self, **params: Unpack[WattpadUserDefaultParams]) -> WattpadUserResponse: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesStreamParams]) -> BinaryIO: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesTextResponseParams]) -> str: ...
    @overload
    async def user_stories(self, **params: Unpack[WattpadUserStoriesDefaultParams]) -> WattpadUserStoriesResponse: ...

WattpadCategoriesDefaultParams = TypedDict('WattpadCategoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

WattpadCategoriesTextResponseParams = TypedDict('WattpadCategoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

WattpadCategoriesStreamParams = TypedDict('WattpadCategoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

WattpadLanguagesDefaultParams = TypedDict('WattpadLanguagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
}, total=False)

WattpadLanguagesTextResponseParams = TypedDict('WattpadLanguagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
}, total=False)

WattpadLanguagesStreamParams = TypedDict('WattpadLanguagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
}, total=False)

WattpadPartDefaultParams = TypedDict('WattpadPartDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'part_id': Required[str],
}, total=False)

WattpadPartTextResponseParams = TypedDict('WattpadPartTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'part_id': Required[str],
}, total=False)

WattpadPartStreamParams = TypedDict('WattpadPartStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'part_id': Required[str],
}, total=False)

WattpadPartCommentsDefaultParams = TypedDict('WattpadPartCommentsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'part_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadPartCommentsTextResponseParams = TypedDict('WattpadPartCommentsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'part_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadPartCommentsStreamParams = TypedDict('WattpadPartCommentsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'part_id': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchDefaultParams = TypedDict('WattpadSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': NotRequired[str],
    'filter': NotRequired[Literal['hot', 'new', 'featured']],
    'category': NotRequired[int],
    'language': NotRequired[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '46', '47', '48', '49', '50', '51', '53']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchTextResponseParams = TypedDict('WattpadSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': NotRequired[str],
    'filter': NotRequired[Literal['hot', 'new', 'featured']],
    'category': NotRequired[int],
    'language': NotRequired[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '46', '47', '48', '49', '50', '51', '53']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchStreamParams = TypedDict('WattpadSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': NotRequired[str],
    'filter': NotRequired[Literal['hot', 'new', 'featured']],
    'category': NotRequired[int],
    'language': NotRequired[Literal['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '46', '47', '48', '49', '50', '51', '53']],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchUsersDefaultParams = TypedDict('WattpadSearchUsersDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'query': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchUsersTextResponseParams = TypedDict('WattpadSearchUsersTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'query': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadSearchUsersStreamParams = TypedDict('WattpadSearchUsersStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'query': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadStoryDefaultParams = TypedDict('WattpadStoryDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryTextResponseParams = TypedDict('WattpadStoryTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryStreamParams = TypedDict('WattpadStoryStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryPartsDefaultParams = TypedDict('WattpadStoryPartsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryPartsTextResponseParams = TypedDict('WattpadStoryPartsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryPartsStreamParams = TypedDict('WattpadStoryPartsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'story_id': Required[str],
}, total=False)

WattpadStoryRecommendationsDefaultParams = TypedDict('WattpadStoryRecommendationsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'story_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

WattpadStoryRecommendationsTextResponseParams = TypedDict('WattpadStoryRecommendationsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'story_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

WattpadStoryRecommendationsStreamParams = TypedDict('WattpadStoryRecommendationsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'story_id': Required[str],
    'limit': NotRequired[int],
}, total=False)

WattpadUserDefaultParams = TypedDict('WattpadUserDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
}, total=False)

WattpadUserTextResponseParams = TypedDict('WattpadUserTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
}, total=False)

WattpadUserStreamParams = TypedDict('WattpadUserStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
}, total=False)

WattpadUserStoriesDefaultParams = TypedDict('WattpadUserStoriesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadUserStoriesTextResponseParams = TypedDict('WattpadUserStoriesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)

WattpadUserStoriesStreamParams = TypedDict('WattpadUserStoriesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'username': Required[str],
    'limit': NotRequired[int],
    'offset': NotRequired[int],
}, total=False)
