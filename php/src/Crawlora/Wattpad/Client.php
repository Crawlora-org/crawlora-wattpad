<?php

declare(strict_types=1);

namespace Crawlora\Wattpad;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'wattpad';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 11;
    public const OPERATION_IDS = ["wattpad-categories", "wattpad-languages", "wattpad-part", "wattpad-part-comments", "wattpad-search", "wattpad-search-users", "wattpad-story", "wattpad-story-parts", "wattpad-story-recommendations", "wattpad-user", "wattpad-user-stories"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"wattpad-categories": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-categories", "method": "GET", "params": [], "path": "/wattpad/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "wattpad-languages": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-languages", "method": "GET", "params": [], "path": "/wattpad/languages", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "wattpad-part": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-part", "method": "GET", "params": [{"description": "Numeric chapter id from the id field of wattpad-story-parts", "in": "query", "name": "part_id", "required": true, "type": "string", "x-example": "1353317758"}], "path": "/wattpad/part", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "part_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wattpad-part-comments": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-part-comments", "method": "GET", "params": [{"description": "Numeric chapter id from the id field of wattpad-story-parts", "in": "query", "name": "part_id", "required": true, "type": "string", "x-example": "1353317758"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 5}, {"description": "Zero-based result offset, below 100000; defaults to 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/wattpad/part-comments", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "part_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wattpad-search": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-search", "method": "GET", "params": [{"description": "Text to search for in story titles, descriptions and tags, up to 200 characters", "in": "query", "name": "query", "type": "string", "x-example": "romance"}, {"description": "Ranking: hot is currently popular, new is recently published, featured is Wattpad's featured stories", "enum": ["hot", "new", "featured"], "in": "query", "name": "filter", "type": "string", "x-example": "hot"}, {"description": "Category id from wattpad-categories, for example 4 for Romance", "in": "query", "name": "category", "type": "integer", "x-example": 4}, {"description": "Story language id from wattpad-languages, for example 1 for English", "enum": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 51, 53], "in": "query", "name": "language", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 20}, {"description": "Zero-based result offset; below 10000 with query, below 1500 without", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/wattpad/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "type": "string"}, {"enum": ["hot", "new", "featured"], "in": "query", "name": "filter", "type": "string"}, {"in": "query", "name": "category", "type": "integer"}, {"enum": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "46", "47", "48", "49", "50", "51", "53"], "in": "query", "name": "language", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wattpad-search-users": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-search-users", "method": "GET", "params": [{"description": "Author name to search for, up to 200 characters", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "notjust"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 5}, {"description": "Zero-based result offset, below 10000; defaults to 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/wattpad/search-users", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wattpad-story": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-story", "method": "GET", "params": [{"description": "Numeric Wattpad story id, such as 344352588; a wattpad.com/story link is also accepted", "in": "query", "name": "story_id", "required": true, "type": "string", "x-example": "344352588"}], "path": "/wattpad/story", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "story_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wattpad-story-parts": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-story-parts", "method": "GET", "params": [{"description": "Numeric Wattpad story id, such as 344352588; a wattpad.com/story link is also accepted", "in": "query", "name": "story_id", "required": true, "type": "string", "x-example": "344352588"}], "path": "/wattpad/story-parts", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "story_id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wattpad-story-recommendations": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-story-recommendations", "method": "GET", "params": [{"description": "Numeric Wattpad story id, such as 344352588; a wattpad.com/story link is also accepted", "in": "query", "name": "story_id", "required": true, "type": "string", "x-example": "344352588"}, {"description": "Maximum recommendations to return, 1 to 20; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 5}], "path": "/wattpad/story-recommendations", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "story_id", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "wattpad-user": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-user", "method": "GET", "params": [{"description": "Wattpad username from wattpad.com/user/{username}; a profile link or @name is also accepted", "in": "query", "name": "username", "required": true, "type": "string", "x-example": "notjustarandomgirl"}], "path": "/wattpad/user", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "wattpad-user-stories": {"bodyParam": null, "bodyRequired": false, "id": "wattpad-user-stories", "method": "GET", "params": [{"description": "Wattpad username from wattpad.com/user/{username}; a profile link or @name is also accepted", "in": "query", "name": "username", "required": true, "type": "string", "x-example": "notjustarandomgirl"}, {"description": "Page size, 1 to 100; defaults to 20", "in": "query", "name": "limit", "type": "integer", "x-example": 5}, {"description": "Zero-based result offset; defaults to 0", "in": "query", "name": "offset", "type": "integer", "x-example": 0}], "path": "/wattpad/user-stories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "username", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "offset", "type": "integer"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-wattpad-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function categories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-categories", $params, $responseType);
    }
    public function languages(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-languages", $params, $responseType);
    }
    public function part(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-part", $params, $responseType);
    }
    public function part_comments(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-part-comments", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-search", $params, $responseType);
    }
    public function search_users(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-search-users", $params, $responseType);
    }
    public function story(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-story", $params, $responseType);
    }
    public function story_parts(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-story-parts", $params, $responseType);
    }
    public function story_recommendations(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-story-recommendations", $params, $responseType);
    }
    public function user(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-user", $params, $responseType);
    }
    public function user_stories(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("wattpad-user-stories", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
