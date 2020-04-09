from django.shortcuts import render
from django.core.serializers import serialize
from django.views import View
from .models import Emplyoee
from django.http import HttpResponse,JsonResponse
import json
from .serializemixin import serializemixin,HttpResponseMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import is_json
from .forms import EmplyoeeForm

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')#applicable  for all  request at class level
class EmployeeClassBasedView(View,serializemixin,HttpResponseMixin):
    def get(self,request,*args,**kwargs):
        employee = Emplyoee.objects.all()
        print("Employe = ",employee.values())
        # jsondata = serialize('json',employee,fields = {'id','name','age'})
        # print("json data from ",jsondata)
        # loads = json.loads(jsondata)
        # finallist = []
        # for item in loads:
        #     finallist.append(item['fields'])
        # # return JsonResponse(jsondata)
        # result = json.dumps(finallist)
        # # return HttpResponse(finallist,content_type='applicaiton/json')
        # serializemixinob = serializemixin()
        result = self.serialize(employee)
        return JsonResponse(result,safe=False)

    # @csrf_exempt at methos level
    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'Please provide valid data'})
        json_data_success = json.dumps({'msg':'Resource has been created'})
        data = str(request.body, encoding='utf-8')
        print("request.body is ",request.body)
        print("data is",data)
        if is_json(data):
            json_data = json.loads(data)
            form = EmplyoeeForm(json_data)
            if form.is_valid():
                form.save(commit=True)
            return self.response_to_render(json_data_success)
        else:
            return self.response_to_render(json_data)
class EmployeeClassBasedDetailsView(View,serializemixin):
    def get(self,request,id,*args,**kwargs):
        try:
            employee = Emplyoee.objects.get(id=id)
            result = self.serialize([employee,])
            return JsonResponse(result,safe=False)
            
        except ObjectDoesNotExist:
            return HttpResponse("<h3>Object Not Here<h3>")
