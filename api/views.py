from django.http import HttpRequest, JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import json
from .models import Mobile
from django.views import View

def get_product(request: HttpRequest) -> JsonResponse:
            products = Mobile.objects.filter(model='Oppo')
            data = []
            for product in products:
                data.append(product.to_dict())
            return JsonResponse(data, safe=False)

class MyView(View):
    def get(self,request:HttpRequest,name=None,pk=None,color=None,price=None) ->JsonResponse:
        if name:
                product = Mobile.objects.filter(model__contains = name)
                data = []
                for i in product:
                    data.append(i.to_dict())
                return JsonResponse(data=data, safe=False )
        elif pk:
                product = Mobile.objects.get(id = pk)
                return JsonResponse(product.to_dict())
        elif color:
                product = Mobile.objects.filter(color__contains = color)
                data = []
                for i in product:               
                    data.append(i.to_dict())
                return JsonResponse(data,safe=False)
        elif price:
                product = Mobile.objects.filter(price__lte = price)
                data = []
                for i in product:
                    data.append(i.to_dict())
                return JsonResponse(data,safe = False)   
        else:
            product = Mobile.objects.all()
            data = []
            for i in product:
                    data.append(i.to_dict())
            return JsonResponse({"data":data})
        
            

class myview(View):  
    def delete(request:HttpRequest,pk)->JsonResponse:
        if pk:  
            product = Mobile.objects.get(id=pk)
            
            product.delete()
            return JsonResponse({'status':"200 OK"})
        else:
            return "Delete_id"

def lst_models(request: HttpRequest) -> JsonResponse:
    """get all models"""
    try:
        product = Mobile.objects.all()
        data = []
        for i in product:
            data.append(i.to_dict()['model'])
        data = list(set(data))
    except:
        return JsonResponse({"data":"not found"})
    return JsonResponse(data=data, safe=False)
class MyViev(View):
     
    def post(request:HttpRequest,id:int):
        if id:
                data = request.body.decode('utf-8')
                data = json.loads(data)
                item = Mobile.objects.filter(id=id) 
                item.update(
                    name = data['name'],
                    model = data['model'],
                    color = data['color'],
                    ram = data['ram'],
                    memory = data['memory'],
                    price = data['price'], 
                    img_url = data['url'], 
                )
                obj = Mobile.objects.all()
                ruyxat = []
                for item in obj:
                    ruyxat.append(item.to_dict())
                return JsonResponse({"smartphes":ruyxat}, safe=False)
        else:
            return "Update not found."
def add_product(reqeust: HttpRequest) :
        if reqeust.method == 'POST':
                data = json.loads(reqeust.body.decode('utf-8'))
                s = ''
                mom = ''
                for i in data['RAM']:
                    if i.isdigit():
                        s+=i
                    else:
                        break
                for i in data['memory']:
                    if i.isalpha():
                        continue
                    else:
                        mom+=i
                n = eval(mom)
                product = Mobile.objects.create(
                    price=data['price'],
                    img_url=data['img_url'],
                    color=data['color'],
                    ram=int(s),
                    memory=int(n),
                    name=data['name'],
                    model=data['company']
                )
                return JsonResponse({'status': 'OK'})
        else:
            return HttpResponse("Method error")
    