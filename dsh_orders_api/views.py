#!/usr/bin/python

from rest_framework import viewsets, permissions 
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions, renderers
from rest_framework.decorators import api_view 
from rest_framework.reverse import reverse
from dsh_shop_proj.permissions import IsOwnerOrReadOnly
from .serializers import OrderSerializer
from .models import Order


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'orders': reverse('order-list', request=request, format=format),
    })
    

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Orders.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        order = self.get_object()
        return Response(order.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
