from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from django.contrib.auth.backends import ModelBackend

from project.models import Product


class CustomAuthentication(BasicAuthentication):
    def is_authenticated(self, request, **kwargs):
        auth = request.headers.get('Authorization', '')
        request.META['HTTP_AUTHORIZATION'] = auth

        try:
            username, password = self.extract_credentials(request)
        except ValueError:
            return self._unauthorized()

        user = self.backend.authenticate(request, username, password)

        if user is None:
            return self._unauthorized()

        request.user = user
        return True


class Products(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        list_allowed_methods = ['get', 'post']
        detail_allowed_methods = ['get', 'put', 'delete']
        serializer = Serializer(formats=['json'])
        authentication = CustomAuthentication(backend=ModelBackend())
        authorization = DjangoAuthorization()
        excludes = [
            'is_active',
            'is_staff',
            'is_superuser',
            'date_joined',
            'last_login'
        ]
