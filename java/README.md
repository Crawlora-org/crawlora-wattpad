# Crawlora Wattpad API client for Java

The official Java client for Crawlora's hosted Wattpad API. It exposes 11 endpoints covering story, author, search, category, language, and public comment data. Requests use your `x-api-key`; the client does not connect to the upstream site directly.

## Install

```xml
<dependency>
  <groupId>net.crawlora</groupId>
  <artifactId>crawlora-wattpad</artifactId>
  <version>0.1.0</version>
</dependency>
```

## Use

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-java-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-java-console) to get an API key.

```java
import net.crawlora.wattpad.Client;
import java.time.Duration;
import java.util.Map;

try (Client client = new Client(System.getenv("CRAWLORA_API_KEY"))) {
    Object result = client.categories(Map.of());
    System.out.println(result);
}
```

Each operation has a direct method that accepts the parameters documented for that endpoint. Use `client.request(operationId, params)` for generic dispatch. `Client.OPERATION_IDS`, `Client.OPERATION_COUNT`, `client.getOperationIds()`, and `client.getOperationCount()` describe this platform's operations only.

For custom hosted API routing and timeouts, use `new Client(apiKey, baseUrl, Duration.ofSeconds(20))`. Text responses are returned as `String`; JSON responses are parsed into Java maps, lists, and scalar values.

## Supported Wattpad API endpoints

Browse every route included in this Java package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md) also lists parameters and response details.

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

## Links

- [Crawlora](https://crawlora.net/?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-java-homepage)
- [Crawlora platform clients](https://github.com/Crawlora-org/crawlora-wattpad)
- [API documentation](https://crawlora.net/docs?utm_source=maven-central&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-java-api-docs)
