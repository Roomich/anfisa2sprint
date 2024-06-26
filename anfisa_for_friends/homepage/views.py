from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import Category, IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        category__is_published=True,
        is_published=True,
        is_on_main=True,
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
