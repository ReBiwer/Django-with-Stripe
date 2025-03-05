from django.urls import path
from django.views.generic import TemplateView
from .views import GetPaymentIntent, PayItem, PayOrder


app_name = "payment"

urlpatterns = [
    path('buy/', GetPaymentIntent.as_view(), name='get_intent'),
    path('order/<int:pk>/', PayOrder.as_view(), name='pay_order'),
    path('item/<int:pk>/', PayItem.as_view(), name='pay_item'),
    path('buy/success/', TemplateView.as_view(template_name='payment/success_payment.html'), name='success_payment'),
    path('buy/cancel/', TemplateView.as_view(template_name='payment/cancel_payment.html'), name='cancel_payment'),
]
