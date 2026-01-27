import os from flask
import flask from azure.cosmos import CosmosClient

app = Flask(_name_)
url = os.environ.get("COSMOS_ENDPOINT")
key = os.environ.get("AZURE_COSMOS_CONNECTION_STRING")
client = CosmosClient(url,credential=key)
database = client.get_database_client("v-db")
container = database.get_container_client("v_container")

@app.route("/")
def fello():
  return "<h1>Hello! This is my Project 2 Website.</h1><p>The visitor counter is coming next!</p>"
  item = container.read_item(item="1", partition_key="1")
  item['count'] += 1
  current_count = item['count']
  item['count' = current_count + 1
  container.upsert_item(item)
  return f"<h1>Welcome!</h1><p>You are visitor number: {item['count']}</p>"

