# @crawlora-org/wattpad — Wattpad API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Wattpad API.
It exposes 11 API endpoints for story, author, search, category, language, and public comment data through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-javascript-homepage). It does not run a browser or scrape Wattpad locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Wattpad or its owners.

## Install

```sh
npm install @crawlora-org/wattpad
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=wattpad-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { WattpadClient } from "@crawlora-org/wattpad";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new WattpadClient({ apiKey });
const result1 = await client.search({ query: "romance" });
console.log(result1);
const result2 = await client.categories({});
console.log(result2);
```

The client also exports `Client` as an alias for `WattpadClient`. Operation
methods are available directly in camelCase and through the `wattpad`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Wattpad API endpoints

This package exposes each route below as a direct method and through the `wattpad` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-wattpad/blob/main/docs/usage.md) for complete input details.

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

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
