import os

import stripe
from django.http import HttpRequest
from django.urls import reverse

from app.settings import STRIPE_SECRET_KEY
from .models import Item, Order


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


def get_api_key(item: Item) -> str:
    currency = str(item.currency)
    return os.environ.get(f'STRIPE_KEY_{currency.upper()}')


def get_stripe_intent(order: Order) -> stripe.PaymentIntent:
    stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')
    intent = stripe.PaymentIntent.create(
        amount=int(order.total_amount * 100),
        currency='usd',
        automatic_payment_methods={'enabled': True},
        discount=order.discount.stripe_id if order.discount else None,
        tax_rates=[order.tax.stripe_id] if order.tax else None,
    )
    return intent
