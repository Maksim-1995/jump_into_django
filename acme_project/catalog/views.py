# Импортируем функцию render()
from django.shortcuts import render
    
def product_detail(request):
    template = 'catalog/product_detail.html'
    return render(request, template)



def product_list(request):
    template_name = 'catalog/product_list'
    return render(request, template_name)