# Crawlora Wattpad Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wattpad | `wattpad.categories` | `wattpad-categories` | `GET /wattpad/categories` | none | `ApiKeyAuth` | `WattpadCategoriesResponse` |  |
| wattpad | `wattpad.languages` | `wattpad-languages` | `GET /wattpad/languages` | none | `ApiKeyAuth` | `WattpadLanguagesResponse` |  |
| wattpad | `wattpad.part` | `wattpad-part` | `GET /wattpad/part` | `part_id` (query String required) | `ApiKeyAuth` | `WattpadPartResponse` |  |
| wattpad | `wattpad.part_comments` | `wattpad-part-comments` | `GET /wattpad/part-comments` | `part_id` (query String required)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `WattpadPartCommentsResponse` |  |
| wattpad | `wattpad.search` | `wattpad-search` | `GET /wattpad/search` | `query` (query String)<br>`filter` (query String enum{hot, new, featured})<br>`category` (query i64)<br>`language` (query String enum{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 53})<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `WattpadSearchResponse` |  |
| wattpad | `wattpad.search_users` | `wattpad-search-users` | `GET /wattpad/search-users` | `query` (query String required)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `WattpadSearchUsersResponse` |  |
| wattpad | `wattpad.story` | `wattpad-story` | `GET /wattpad/story` | `story_id` (query String required) | `ApiKeyAuth` | `WattpadStoryResponse` |  |
| wattpad | `wattpad.story_parts` | `wattpad-story-parts` | `GET /wattpad/story-parts` | `story_id` (query String required) | `ApiKeyAuth` | `WattpadStoryPartsResponse` |  |
| wattpad | `wattpad.story_recommendations` | `wattpad-story-recommendations` | `GET /wattpad/story-recommendations` | `story_id` (query String required)<br>`limit` (query i64) | `ApiKeyAuth` | `WattpadStoryRecommendationsResponse` |  |
| wattpad | `wattpad.user` | `wattpad-user` | `GET /wattpad/user` | `username` (query String required) | `ApiKeyAuth` | `WattpadUserResponse` |  |
| wattpad | `wattpad.user_stories` | `wattpad-user-stories` | `GET /wattpad/user-stories` | `username` (query String required)<br>`limit` (query i64)<br>`offset` (query i64) | `ApiKeyAuth` | `WattpadUserStoriesResponse` |  |
