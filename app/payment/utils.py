import stripe
from django.http import HttpRequest
from django.urls import reverse

from app.settings import STRIPE_SECRET_KEY
from .models import Item


def get_stripe_session(item: Item, request: HttpRequest) -> stripe.checkout.Session:
    stripe.api_key = STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": int(item.price * 100),
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url=request.build_absolute_uri(reverse('payment:success_payment')),
        cancel_url=request.build_absolute_uri(reverse('payment:cancel_payment')),
    )
    return session
