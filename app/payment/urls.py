from django.urls import path
from django.views.generic import TemplateView
from .views import GetStripeSession, PayItem


app_name = "payment"

urlpatterns = [
    path('buy/<int:id>/', GetStripeSession.as_view(), name='get_session'),
    path('item/<int:pk>/', PayItem.as_view(), name='pay_item'),
    path('buy/success/', TemplateView.as_view(template_name='payment/success_payment.html'), name='success_payment'),
    path('buy/cancel/', TemplateView.as_view(template_name='payment/cancel_payment.html'), name='cancel_payment'),
]
