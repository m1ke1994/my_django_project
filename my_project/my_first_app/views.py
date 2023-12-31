from django.shortcuts import render, get_object_or_404
from my_first_app.models import Аpartments  # Поменяйте "Apartments" на "Аpartments"
from orders.forms import OrderForm



def my_first_app_list(request):
    apartments = Аpartments.objects.all()
    return render(request, "my_first_app/my_first_app_list.html", {"apartments": apartments})

def my_first_app_detail(request, apart_id):
    form=OrderForm()
    apart = get_object_or_404(Аpartments, id=apart_id)
    return render(request, "my_first_app/my_first_app_detail.html", {"apart": apart,"form":form})


def my_first_app_company(request):
    return render(request, "my_first_app/my_first_app_company.html")