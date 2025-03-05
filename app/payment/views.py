import json
from django.db.models import Sum
from django.http import HttpRequest, JsonResponse
from django.views.generic import View, DetailView
from .utils import get_stripe_session, get_stripe_intent
from .models import Item, Order


class GetPaymentIntent(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        id_item = self.kwargs.get('id')
        item_obj = Item.objects.get(id=int(id_item))
        session_pay = get_stripe_session(item_obj, request)
        return JsonResponse(data={'session': session_pay})

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        order_id = data['order_id']
        order = Order.objects.filter(id=order_id).annotate(
            total_amount=Sum('items__price')
        ).first()
        intent = get_stripe_intent(order)
        return JsonResponse({'clientSecret': intent.client_secret})


class PayItem(DetailView):
    template_name = 'payment/buy_item.html'
    context_object_name = 'item'
    model = Item


class PayOrder(DetailView):
    template_name = 'payment/buy_order.html'
    context_object_name = 'order'
    model = Order

    def get_queryset(self):
        order_id = self.kwargs.get('pk')
        order = Order.objects.filter(id=order_id).annotate(
            total_amount=Sum('items__price'),
        )
        return order