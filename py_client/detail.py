"""This defines the URL endpoint to which the GET request will be sent. 
It appears to be an API endpoint for fetching information about a specific product with an ID of 1."""
import requests
"""This sends a GET request to the specified endpoint and assigns the response object to the get_response variable."""
endpoint = 'http://localhost:8000/api/products/1/'
"""This prints the JSON content of the response. 
The .json() method is used to parse the JSON data from the response content and convert it into a Python dictionary."""
get_response = requests.get(endpoint)
print(get_response.json())