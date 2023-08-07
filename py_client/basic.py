"""The requests library provides a convenient way to send HTTP requests to web servers and receive HTTP responses. 
This can be useful for various tasks such as making API calls, fetching data from websites, and interacting with web services."""
import requests


# declare the endpoit of API, request of app
# endpoint = "http://httpbin.org/status/200/"
# endpoint = "http://httpbin.org/anything" # format the data 


# run server default of django frame in manage.py
endpoint = 'http://localhost:8000/api/'  #http://127.0.0.1:8000/
# requests.get() #API -> Method, aplication programming interface

#phone -> camera -> app -> api -> camera
# use HTTP request for python 
get_response = requests.get(endpoint,params={'abc':123}, json={"query": "Hello World"}) # HTTP request
# print(get_response.json()) # print raw text requiest
# print(get_response.status_code)

#HTTP request -> HTML
#Rest API HTTP Request ->Json
# print(get_response.json())
# {'args': {}, 'data': '', 'files': {}, 'form': {}, 'headers': 
#     {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 
#         'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.31.0', 'X-Amzn-Trace-Id': 'Root=1-64a1983a-3fbf059c13c82bb0697acb99'}, 
#  'json': None, 'method': 'GET', 'origin': '46.97.169.60', 'url': 'http://httpbin.org/anything'}

# have one client of py_clinet and browser client
# print(get_response.status_code)