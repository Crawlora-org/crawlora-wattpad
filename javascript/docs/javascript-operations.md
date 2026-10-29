# Crawlora Wattpad JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `11`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| wattpad | `wattpad.categories` | `wattpad-categories` | `GET /wattpad/categories` | none | `ApiKeyAuth` | `WattpadCategoriesResponse` |  |
| wattpad | `wattpad.languages` | `wattpad-languages` | `GET /wattpad/languages` | none | `ApiKeyAuth` | `WattpadLanguagesResponse` |  |
| wattpad | `wattpad.part` | `wattpad-part` | `GET /wattpad/part` | `part_id` (query string required) | `ApiKeyAuth` | `WattpadPartResponse` |  |
| wattpad | `wattpad.partComments` | `wattpad-part-comments` | `GET /wattpad/part-comments` | `part_id` (query string required)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `WattpadPartCommentsResponse` |  |
| wattpad | `wattpad.search` | `wattpad-search` | `GET /wattpad/search` | `query` (query string)<br>`filter` (query "hot" \| "new" \| "featured")<br>`category` (query number)<br>`language` (query "1" \| "2" \| "3" \| "4" \| "5" \| "6" \| "7" \| "8" \| "9" \| "10" \| "11" \| "12" \| "13" \| "14" \| "15" \| "16" \| "17" \| "18" \| "19" \| "20" \| "21" \| "22" \| "23" \| "24" \| "25" \| "26" \| "27" \| "28" \| "29" \| "30" \| "32" \| "33" \| "34" \| "35" \| "36" \| "37" \| "38" \| "39" \| "40" \| "41" \| "42" \| "43" \| "44" \| "46" \| "47" \| "48" \| "49" \| "50" \| "51" \| "53")<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `WattpadSearchResponse` |  |
| wattpad | `wattpad.searchUsers` | `wattpad-search-users` | `GET /wattpad/search-users` | `query` (query string required)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `WattpadSearchUsersResponse` |  |
| wattpad | `wattpad.story` | `wattpad-story` | `GET /wattpad/story` | `story_id` (query string required) | `ApiKeyAuth` | `WattpadStoryResponse` |  |
| wattpad | `wattpad.storyParts` | `wattpad-story-parts` | `GET /wattpad/story-parts` | `story_id` (query string required) | `ApiKeyAuth` | `WattpadStoryPartsResponse` |  |
| wattpad | `wattpad.storyRecommendations` | `wattpad-story-recommendations` | `GET /wattpad/story-recommendations` | `story_id` (query string required)<br>`limit` (query number) | `ApiKeyAuth` | `WattpadStoryRecommendationsResponse` |  |
| wattpad | `wattpad.user` | `wattpad-user` | `GET /wattpad/user` | `username` (query string required) | `ApiKeyAuth` | `WattpadUserResponse` |  |
| wattpad | `wattpad.userStories` | `wattpad-user-stories` | `GET /wattpad/user-stories` | `username` (query string required)<br>`limit` (query number)<br>`offset` (query number) | `ApiKeyAuth` | `WattpadUserStoriesResponse` |  |
