import requests

# Swagger JSON URL
swagger_url = "http://petstore.swagger.io/v2/swagger.json"

# Fetch the Swagger JSON from the URL
swagger_json = requests.get(swagger_url).json()

# Parse the Swagger JSON and output all endpoints
for path, path_def in swagger_json["paths"].items():
    print(path)

