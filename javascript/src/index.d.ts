import type {
  CrawloraGeneratedGroups,
  OperationId,
  OperationParamsMap,
  OperationRequestArgs,
  OperationResponseMap
} from "./types.js";

export type CrawloraParams = Record<string, unknown>;
export type CrawloraLogEvent = { event: string; [key: string]: unknown };
export interface CrawloraRequestContext { operationId: string; method: string; url: string; headers: Record<string, string> }
export type CrawloraBeforeRequest = (ctx: CrawloraRequestContext) => void | Promise<void>;
export type CrawloraAfterResponse = (operationId: string, status: number, headers: Record<string, string>, body: unknown) => unknown;

export interface CrawloraClientOptions {
  apiKey?: string;
  jwtToken?: string;
  baseUrl?: string;
  timeout?: number;
  retries?: number;
  retryDelay?: number;
  maxRetryDelay?: number;
  retryStatuses?: Iterable<number>;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
  onRetry?: (attempt: number, error: CrawloraError, delay: number) => void;
  requestId?: boolean;
  idempotencyKeys?: boolean;
  rateLimit?: number;
  maxConcurrency?: number;
  logger?: (event: CrawloraLogEvent) => void;
  beforeRequest?: CrawloraBeforeRequest | Iterable<CrawloraBeforeRequest>;
  afterResponse?: CrawloraAfterResponse | Iterable<CrawloraAfterResponse>;
  headers?: Record<string, string>;
  userAgent?: string | false;
  fetch?: typeof globalThis.fetch;
}

export interface CrawloraRequestOptions {
  headers?: Record<string, string>;
  responseType?: "auto" | "json" | "text" | "stream";
  timeout?: number;
  signal?: AbortSignal;
  retries?: number;
  isRetryable?: (status: number, error: CrawloraError) => boolean;
}

export interface OperationDefinition {
  id: string; method: string; path: string; pathParams: string[];
  queryParams: Array<{ name: string; in?: "query"; collectionFormat?: string; type?: string; required?: boolean; enum?: string[] }>;
  formParams: Array<{ name: string; in?: "formData"; type?: string; required?: boolean; enum?: string[] }>;
  bodyParam?: string; bodyRequired?: boolean; consumes: string[]; produces: string[]; security: string[];
  paginatable?: boolean; cursorParams?: string[];
}

export class CrawloraError extends Error {
  status: number; code?: number; body: unknown; headers: Record<string, string>;
  response?: Response; cause?: unknown; retryable?: boolean; requestId?: string;
}
export class CrawloraClientError extends CrawloraError {}
export class CrawloraServerError extends CrawloraError {}
export class CrawloraNetworkError extends CrawloraError {}

export interface CrawloraPaginateOptions extends CrawloraRequestOptions {
  pageParam?: string; cursorParam?: string; nextCursor?: (page: unknown) => unknown;
  start?: unknown; step?: number; maxPages?: number;
}
export interface CrawloraPaginateItemsOptions extends CrawloraPaginateOptions {
  items?: (page: unknown) => Iterable<unknown>;
}

export class CrawloraClient {
  constructor(options?: CrawloraClientOptions);
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  paginate<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateOptions): AsyncGenerator<OperationResponseMap[I], void, unknown>;
  paginateItems<I extends OperationId>(operationId: I, params?: OperationParamsMap[I], options?: CrawloraPaginateItemsOptions): AsyncGenerator<unknown, void, unknown>;
  [group: string]: unknown;
}
export interface CrawloraClient extends CrawloraGeneratedGroups {}

export class WattpadClient extends CrawloraClient {
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  categories(params?: OperationParamsMap["wattpad-categories"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  languages(params?: OperationParamsMap["wattpad-languages"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  part(params: OperationParamsMap["wattpad-part"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  partComments(params: OperationParamsMap["wattpad-part-comments"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  search(params?: OperationParamsMap["wattpad-search"], options?: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  searchUsers(params: OperationParamsMap["wattpad-search-users"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  story(params: OperationParamsMap["wattpad-story"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  storyParts(params: OperationParamsMap["wattpad-story-parts"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  storyRecommendations(params: OperationParamsMap["wattpad-story-recommendations"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  user(params: OperationParamsMap["wattpad-user"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  userStories(params: OperationParamsMap["wattpad-user-stories"], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  categories(params?: OperationParamsMap["wattpad-categories"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  languages(params?: OperationParamsMap["wattpad-languages"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  part(params: OperationParamsMap["wattpad-part"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  partComments(params: OperationParamsMap["wattpad-part-comments"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  search(params?: OperationParamsMap["wattpad-search"], options?: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  searchUsers(params: OperationParamsMap["wattpad-search-users"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  story(params: OperationParamsMap["wattpad-story"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  storyParts(params: OperationParamsMap["wattpad-story-parts"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  storyRecommendations(params: OperationParamsMap["wattpad-story-recommendations"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  user(params: OperationParamsMap["wattpad-user"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;
  userStories(params: OperationParamsMap["wattpad-user-stories"], options: CrawloraRequestOptions & { responseType: "text" }): Promise<string>;

  request<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  request<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  operation<I extends OperationId>(operationId: I, params: OperationParamsMap[I], options: CrawloraRequestOptions & { responseType: "stream" }): Promise<Response>;
  operation<I extends OperationId>(operationId: I, ...args: OperationRequestArgs<I>): Promise<OperationResponseMap[I]>;
  categories(...args: OperationRequestArgs<"wattpad-categories">): Promise<OperationResponseMap["wattpad-categories"]>;
  languages(...args: OperationRequestArgs<"wattpad-languages">): Promise<OperationResponseMap["wattpad-languages"]>;
  part(...args: OperationRequestArgs<"wattpad-part">): Promise<OperationResponseMap["wattpad-part"]>;
  partComments(...args: OperationRequestArgs<"wattpad-part-comments">): Promise<OperationResponseMap["wattpad-part-comments"]>;
  search(...args: OperationRequestArgs<"wattpad-search">): Promise<OperationResponseMap["wattpad-search"]>;
  searchUsers(...args: OperationRequestArgs<"wattpad-search-users">): Promise<OperationResponseMap["wattpad-search-users"]>;
  story(...args: OperationRequestArgs<"wattpad-story">): Promise<OperationResponseMap["wattpad-story"]>;
  storyParts(...args: OperationRequestArgs<"wattpad-story-parts">): Promise<OperationResponseMap["wattpad-story-parts"]>;
  storyRecommendations(...args: OperationRequestArgs<"wattpad-story-recommendations">): Promise<OperationResponseMap["wattpad-story-recommendations"]>;
  user(...args: OperationRequestArgs<"wattpad-user">): Promise<OperationResponseMap["wattpad-user"]>;
  userStories(...args: OperationRequestArgs<"wattpad-user-stories">): Promise<OperationResponseMap["wattpad-user-stories"]>;
}
export { WattpadClient as Client };
export const operations: Record<string, OperationDefinition>;
export const groups: Record<string, Record<string, string>>;
export const operationCount: number;
export const OperationIds: Readonly<Record<string, OperationId>>;
export const VERSION: string;
export * from "./types.js";
export default WattpadClient;
