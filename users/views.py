from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from users.models import Payment
from users.serializer import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filterset_fields = ('lesson', 'course', 'payment_method')

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('date_pay',)