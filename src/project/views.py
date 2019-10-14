from django.http import JsonResponse, HttpResponse
from .models import Product
from .forms import PostQuery, PutQuery
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import QueryDict
from datetime import datetime
from django.contrib.auth.decorators import login_required

args = ['height', 'id', 'manufactured', 'name', 'weigth', 'width']


@csrf_exempt
@login_required
def class_view(request):
    if request.method == 'GET':
        result = list(Product.objects.values(*args))
        return JsonResponse(data={'result': result})
    elif request.method == 'POST':
        """
        name    - строка
        weigth  - целое число
        width   - целое число
        height  - целое число
        id      - выдается сервером при создании
        """

        form = PostQuery(request.POST)
        if not form.is_valid():
            return HttpResponse(status=400, reason=form.errors)

        data = form.cleaned_data
        Product(
            name=data['name'],
            weigth=data['weigth'],
            width=data['width'],
            height=data['height'],
        ).save()
        return JsonResponse(data={'result': 'Success'})
    else:
        return HttpResponse(status=405)


@csrf_exempt
@login_required
def self_view(request, code):

    if request.method not in ['PUT', 'DELETE', 'GET']:
        return HttpResponse(status=405)

    product = get_object_or_404(Product, id=code)

    if request.method == 'PUT':
        body = QueryDict(request.body)
        form = PutQuery(body)

        if not form.is_valid():
            return HttpResponse(status=400, reason=form.errors)

        for key, value in form.cleaned_data.items():
            if key in body:
                setattr(product, key, value)
        product.save()
        return JsonResponse(data={'result': 'Success'})

    elif request.method == 'DELETE':
        product.delete()
        return JsonResponse(data={'result': 'Success'})

    else:
        return JsonResponse({
            'id': product.id,
            'manufactured': datetime.isoformat(product.manufactured),
            'name': product.name,
            'weigth': product.weigth,
            'height': product.height,
            'width': product.width,
        })
