# Wattpad API endpoint reference and client usage

This reference lists all 11 public Wattpad API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/wattpad`, `crawlora-wattpad`, and `crawlora-wattpad` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Wattpad locally; Crawlora is independent from and not endorsed by Wattpad or its owners.

The package tracks the public API contract revision `sha256:0a05aa59778d80a0ee980e309da1cb454ba2040754e8c8a27594ad903b0b5320` bundled with release `0.1.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `wattpad`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `categories` | `categories` | `wattpad.categories` | `GET /wattpad/categories` | — | List Wattpad story categories |
| `languages` | `languages` | `wattpad.languages` | `GET /wattpad/languages` | — | List Wattpad story languages |
| `part` | `part` | `wattpad.part` | `GET /wattpad/part` | `part_id` (query, required) | Get a Wattpad chapter |
| `partComments` | `part_comments` | `wattpad.part_comments` | `GET /wattpad/part-comments` | `part_id` (query, required), `limit` (query, optional), `offset` (query, optional) | List reader comments on a Wattpad chapter |
| `search` | `search` | `wattpad.search` | `GET /wattpad/search` | `query` (query, optional), `filter` (query, optional; values: `hot`, `new`, `featured`), `category` (query, optional), `language` (query, optional; values: `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`, `32`, `33`, `34`, `35`, `36`, `37`, `38`, `39`, `40`, `41`, `42`, `43`, `44`, `46`, `47`, `48`, `49`, `50`, `51`, `53`), `limit` (query, optional), `offset` (query, optional) | Search and browse Wattpad stories |
| `searchUsers` | `search_users` | `wattpad.search_users` | `GET /wattpad/search-users` | `query` (query, required), `limit` (query, optional), `offset` (query, optional) | Search Wattpad authors by name |
| `story` | `story` | `wattpad.story` | `GET /wattpad/story` | `story_id` (query, required) | Get a Wattpad story |
| `storyParts` | `story_parts` | `wattpad.story_parts` | `GET /wattpad/story-parts` | `story_id` (query, required) | List a Wattpad story's chapters |
| `storyRecommendations` | `story_recommendations` | `wattpad.story_recommendations` | `GET /wattpad/story-recommendations` | `story_id` (query, required), `limit` (query, optional) | List stories Wattpad recommends for a story |
| `user` | `user` | `wattpad.user` | `GET /wattpad/user` | `username` (query, required) | Get a Wattpad author profile |
| `userStories` | `user_stories` | `wattpad.user_stories` | `GET /wattpad/user-stories` | `username` (query, required), `limit` (query, optional), `offset` (query, optional) | List a Wattpad author's stories |

## Client forms

- JavaScript: import `WattpadClient` (also exported as `Client`) from `@crawlora-org/wattpad`; use `new WattpadClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `WattpadClient` (also exported as `Client`) from `crawlora_wattpad`; use `with WattpadClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncWattpadClient`, used with `async with` and `await`.
- Rust: add `crawlora-wattpad` with Cargo; import `Client` and the generated operation parameter struct, then call `client.wattpad.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
