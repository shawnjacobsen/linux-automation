# defines queries to interest with the Notion API

import requests, json, os
from dotenv import load_dotenv
load_dotenv()

# Default HTTP headers
HEADERS = {
  "Authorization": "Bearer " + os.getenv('NOTION_SECRET'),
  "Content-Type": "application/json",
  "Notion-Version": "2022-06-28"
}

# returns pages in databse based on provided filter, returning json
def getPages(databaseId, filter={}, headers=HEADERS):
  endpoint = f"https://api.notion.com/v1/databases/{databaseId}/query"
  data = {}
  if (bool(filter)):
    data["filter"] = filter

  res = requests.request("POST", endpoint, headers=headers, json=data)
  data = res.json()

  return (res.status_code, data)

# returns response after adding a new page to the specified database
def addPageToDatabase(databaseId, pageProperties, headers=HEADERS):
  endpoint = f"https://api.notion.com/v1/pages"
  data = {
    "parent": { "type": "database_id", "database_id": databaseId },
    "properties": pageProperties
  }

  res = requests.request("POST", endpoint, headers=headers, json=data)
  data = res.json()

  return (res.status_code, data)