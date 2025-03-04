from django.urls import path
from .views import GetStripeSession


app_name = "payment"

urlpatterns = [
    path('buy/<int:id>/', GetStripeSession.as_view(), name='get_session'),
]
