from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def order(request):

    person_name = 'Deepak'
    order_list = ['Axe Perfume', 'Wild Stone Soap', 'Livon Hair Serum', 'Axe AfterShave Lotion']
    ordered_warranty = False
    return render(request, 'order.html', {'p_n': person_name, 'o_l': order_list, 'o_w': ordered_warranty})
