from django.core.serializers import serialize
from django.http import HttpResponse
import json

class serializemixin(object):
    def serialize(self,qs,**options):
        print("Options are",**options)
        jsondata = serialize('json',qs,**options)
        print("json data from ",jsondata)
        loads = json.loads(jsondata)
        finallist = []
        for item in loads:
            finallist.append(item['fields'])
        # return JsonResponse(jsondata)
        result = json.dumps(finallist)
        return result
        # return finallist
class HttpResponseMixin(object):
    def response_to_render(self,json_data):
        return HttpResponse(json_data,content_type='application/json')        