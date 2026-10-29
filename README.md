# Wattpad clients for Crawlora

Official Crawlora client packages for the hosted Wattpad API. Access 11 API endpoints covering story, author, search, category, language, and public comment data from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Wattpad locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Wattpad or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/wattpad`](javascript/README.md)
- Python: [`crawlora-wattpad`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-wattpad`](go.mod)
- Ruby: [`crawlora-wattpad`](ruby/README.md)
- Java: [`net.crawlora:crawlora-wattpad:0.1.0`](java/README.md)
- PHP: [`crawlora/wattpad`](php/README.md)
- Rust: [`crawlora-wattpad`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 11 selected public Wattpad API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/wattpad/categories` | `wattpad-categories` | List Wattpad story categories |
| `GET` | `/wattpad/languages` | `wattpad-languages` | List Wattpad story languages |
| `GET` | `/wattpad/part` | `wattpad-part` | Get a Wattpad chapter |
| `GET` | `/wattpad/part-comments` | `wattpad-part-comments` | List reader comments on a Wattpad chapter |
| `GET` | `/wattpad/search` | `wattpad-search` | Search and browse Wattpad stories |
| `GET` | `/wattpad/search-users` | `wattpad-search-users` | Search Wattpad authors by name |
| `GET` | `/wattpad/story` | `wattpad-story` | Get a Wattpad story |
| `GET` | `/wattpad/story-parts` | `wattpad-story-parts` | List a Wattpad story's chapters |
| `GET` | `/wattpad/story-recommendations` | `wattpad-story-recommendations` | List stories Wattpad recommends for a story |
| `GET` | `/wattpad/user` | `wattpad-user` | Get a Wattpad author profile |
| `GET` | `/wattpad/user-stories` | `wattpad-user-stories` | List a Wattpad author's stories |

## License

MIT. See [LICENSE](LICENSE).
