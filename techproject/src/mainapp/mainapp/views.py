from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "strawberries", "Oranges", "Apples", "Pears", "Watermelons"]
     # user = request.user
    context = {
        # 'user':user,
        'products': products,
    }
    return render(request, "home.html", context)




