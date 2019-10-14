import pytest
from project.models import Product
from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from project.views import self_view, class_view
from datetime import datetime
from django.contrib.auth.models import User
import json


@pytest.fixture
@pytest.mark.django_db
def objects():
    Product(
        name='test#1',
        height=1,
        width=2,
        weigth=3,
    ).save()

    Product(
        name='test#2',
        height=3,
        width=4,
        weigth=5,
    ).save()


@pytest.fixture
def test_user():
    u = User(username='test_user')
    u.save()
    return u


@pytest.mark.django_db
def test_that_check_get_class(rf, objects, test_user):
    request: WSGIRequest = rf.get('/api/products/')
    request.user = test_user
    response: HttpResponse = class_view(request)
    data = json.loads(response.content)
    assert 'result' in data
    assert len(data['result'])


@pytest.mark.django_db
def test_that_check_post_query(rf, objects, test_user):
    count = Product.objects.count()
    data = {
        'name': 'qwe',
        'height': 3,
        'width': 4,
        'weigth': 5,
    }
    request: WSGIRequest = rf.post('/api/products/', data=data)
    request.user = test_user
    response: HttpResponse = class_view(request)
    data = json.loads(response.content)

    assert 'result' in data
    assert data['result'] == 'Success'
    assert count + 1 == Product.objects.count()


@pytest.mark.django_db
def test_that_check_put_query(rf, objects, test_user):
    product = Product.objects.get(name='test#1')
    data = 'name=asd'

    request: WSGIRequest = rf.put(f'/api/products/{product.id}/', data)
    request.user = test_user
    response: HttpResponse = self_view(request, product.id)
    data = json.loads(response.content)
    product = Product.objects.get(id=product.id)

    assert 'result' in data
    assert data['result'] == 'Success'

    assert product.name == 'asd'


@pytest.mark.django_db
def test_that_check_delete_query(rf, objects, test_user):
    count = Product.objects.count()
    product = Product.objects.all()[0]
    request: WSGIRequest = rf.delete(f'/api/products/{product.id}')
    request.user = test_user
    response: HttpResponse = self_view(request, product.id)
    data = json.loads(response.content)

    assert 'result' in data
    assert data['result'] == 'Success'
    assert count - 1 == Product.objects.count()


@pytest.mark.django_db
def test_that_check_get_self(rf, objects, test_user):
    product = Product.objects.all()[0]
    request: WSGIRequest = rf.get(f'/api/products/{product.id}')
    request.user = test_user
    response: HttpResponse = self_view(request, product.id)
    data = json.loads(response.content)

    assert data['id'] == product.id
    assert data['manufactured'] == datetime.isoformat(product.manufactured)
    assert data['name'] == product.name
    assert data['weigth'] == product.weigth
    assert data['width'] == product.width
    assert data['height'] == product.height
