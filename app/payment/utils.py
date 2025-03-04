import stripe
from app.app import settings
from .models import Item


def get_stripe_session_id(item: Item):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                    },
                    "unit_amount": item.price,
                },
                "quantity": 1,
            },
        ],
        mode="payment",
        success_url="",
        cancel_url="",
    )
    return session
