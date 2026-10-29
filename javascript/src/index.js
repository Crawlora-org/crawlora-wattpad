import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class WattpadClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-wattpad-js/0.1.0" });
    this["categories"] = (...args) => this.request("wattpad-categories", ...args);
    this["languages"] = (...args) => this.request("wattpad-languages", ...args);
    this["part"] = (...args) => this.request("wattpad-part", ...args);
    this["partComments"] = (...args) => this.request("wattpad-part-comments", ...args);
    this["search"] = (...args) => this.request("wattpad-search", ...args);
    this["searchUsers"] = (...args) => this.request("wattpad-search-users", ...args);
    this["story"] = (...args) => this.request("wattpad-story", ...args);
    this["storyParts"] = (...args) => this.request("wattpad-story-parts", ...args);
    this["storyRecommendations"] = (...args) => this.request("wattpad-story-recommendations", ...args);
    this["user"] = (...args) => this.request("wattpad-user", ...args);
    this["userStories"] = (...args) => this.request("wattpad-user-stories", ...args);
  }
}

export { WattpadClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.0";
export default WattpadClient;
