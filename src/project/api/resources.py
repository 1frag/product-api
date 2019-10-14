from tastypie.resources import ModelResource
from project.models import Product


class Products(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
