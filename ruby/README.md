# Crawlora Wattpad API client for Ruby (`crawlora-wattpad`)

This Ruby gem calls Crawlora's hosted Wattpad API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering story, author, search, category, language, and public comment data; it does not call or scrape Wattpad directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-wattpad"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/wattpad"

client = Crawlora::Wattpad::Client.new
result = client.request("wattpad-search", JSON.parse("{\"query\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 11 API operations.

```ruby
client = Crawlora::Wattpad::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Wattpad API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-wattpad) for account setup, the API operation reference, and release history.
