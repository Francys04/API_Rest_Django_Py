import json
from django.http import JsonResponse


# create test view of django frame
def api_home(request, *args, **kwargs):
    # request -> HTTPRequest -> Django
    # request .body
    # print(dir(request))
    body = request.body  #byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string od JSON data -> Py Dict
    except:
        pass
    print(data)
    data['headers'] = request.headers #request.META ->
    data['content_type'] = request.content_type
    return JsonResponse({"message": "hi, this is your django"})
# Create your views here.
