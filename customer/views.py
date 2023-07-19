from django.shortcuts import render

# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customer_list = Customer.objects.order_by('-id')
    paginator = Paginator(customer_list,0,26)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'customer_list.html', {'page_obj': page_obj})
from django.shortcuts import render
from .models import Customer

def customer_search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query', '')
        customers = Customer.objects.filter(
            id_number__icontains=search_query,
            first_name__icontains=search_query,
            last_name__icontains=search_query,
            phone_number__icontains=search_query,
            city__icontains=search_query,
            town__icontains=search_query
        )
    else:
        customers = Customer.objects.all()
    return render(request, 'customer_search.html', {'customers': customers})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import CustomerForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})

def customer_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'customer_delete.html', {'customer': customer})

def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customer_create.html', {'form': form})

