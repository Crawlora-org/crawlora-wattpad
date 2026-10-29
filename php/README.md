# Crawlora Wattpad API client for PHP (`crawlora/wattpad`)

This PHP package calls Crawlora's hosted Wattpad API at `https://api.crawlora.net/api/v1`. It exposes 11 endpoints covering story, author, search, category, language, and public comment data. It does not call or scrape Wattpad directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/wattpad
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Wattpad\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("wattpad-search", ['query' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 11 API operations.

## Supported Wattpad API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md) includes parameter and response details.

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

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-wattpad). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md).
