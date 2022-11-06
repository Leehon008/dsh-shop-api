"""dsh_shop_proj URL Configuration
"""
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from dsh_accounts_api import views as accounts_views
from dsh_shop_api import views as shop_views
from dsh_orders_api import views as order_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="DSH  API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
#    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'api/users', accounts_views.UserViewSet, basename='user')
router.register(r'api/groups', accounts_views.GroupViewSet, basename='group')
router.register(r'api/categories', shop_views.CategoryViewSet, basename='category')
router.register(r'api/products', shop_views.ProductViewSet, basename='product')
router.register(r'api/orders', order_views.OrderViewSet, basename='order')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]