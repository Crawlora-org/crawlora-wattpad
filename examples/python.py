import os

from crawlora_wattpad import WattpadClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with WattpadClient(api_key=api_key) as client:
    search = client.search(query='romance')
    print('search', search)
    categories = client.categories()
    print('categories', categories)
