import os from flask
import flask from azure.cosmos import CosmosClient

app = Flask(_name_)
endpoint = os.environ.get("AZURE_COSMOS_CONNECTION_STRING")

@app.route("/")
def fello():
  return "<h1>Hello! This is my Project 2 Website.</h1><p>The visitor counter is coming next!</p>"

if _name_== "_main_":
  app.run()

