import { WattpadClient } from "../src/index.js";

const client = new WattpadClient({ apiKey: "test-key" });
void client.part({"part_id": "sample"});
void client.request("wattpad-part", {"part_id": "sample"});
const streamResponse: Promise<Response> = client.request("wattpad-part", {"part_id": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("wattpad-part", {"part_id": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.part({"part_id": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("wattpad-part", {"part_id": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("wattpad-part", {"part_id": "sample"}, { responseType: "text" });
void rawText;


void client.categories();
void client.request("wattpad-categories");
// @ts-expect-error The selected operation requires its documented params.
void client.part();
