from django.http import HttpRequest
from django.views.generic import View

from .models import Item


class GetStripeSession(View):

    def get(self, request: HttpRequest, *args, **kwargs):
        id_item = self.kwargs.get('id')
        item = Item.objects.get(id=int(id_item))
