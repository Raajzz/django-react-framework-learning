from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.serializers import ProductSerializer

# below we try to convert model instance directly into a dictionary before sending it to the client
def api_home_django(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data)
        data = model_to_dict(model_data, fields=["id", "price"])
    # JsonResponse does all the heavy lifting for us to convert from Dict to Json while sending the response
    # if you want to send it manually using HttpResponse, first you have to convert the dict to json and then you have to return the HttpResponse with the content-type: json, you also need to convert from dict to json data properly (considering all the data type conversions) else it won't work, so.
    return JsonResponse(data)

# in the below code we're converting a model instance manually into a dictionary before sending it to the client
def api_home_manual_serialization(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)


def api_check(request, *args, **kwargs):
    body = {}
    try:
        body = json.loads(request.body)
    except:
        pass
    print(body)
    body['query'] = request.GET
    body['params'] = dict(request.headers)
    body['content-type'] = request.content_type
    return JsonResponse(body)

# the below function is using django rest framework
@api_view(["GET"])
def api_home_rest(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data)
    return Response(data)

# model_to_dict, won't serialize method calls, here we have to use rest_framework's serializers

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        print(ProductSerializer(instance))
        data = ProductSerializer(instance).data
    return Response(data)