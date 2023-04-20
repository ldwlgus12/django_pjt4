from django.shortcuts import render, redirect
from .forms import BalanceForm
from .models import Balance

# Create your views here.
def index(request):
    balances = Balance.objects.order_by('-pk')
    context = {
        'balances' : balances,
    }
    return render(request, 'balances/index.html', context)



def create(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST)
        if form.is_valid():
            balance = form.save(commit=False)
            balance.user = request.user
            balance.save()
            return redirect('balances:index')
    else:
        form = BalanceForm()
    context = {
        'form' : form,
    }
    return render(request, 'balances/create.html', context)




def detail(request, pk):
    balance = Balance.objects.get(pk=pk)
    context = {
        'balance' : balance,
    }    
    return render(request, 'balances/detail.html', context)


def answer(request, pk, balance_answer):
    balance = Balance.objects.get(pk=pk)
    

    if balance.select1_users.filter(pk=request.user.pk).exists():
        if not balance.select2_users.filter(pk=request.user.pk).exists():
            pass
    else:
        if not balance.select2_users.filter(pk=request.user.pk).exists():
            balance.select1_users.add(request.user)
    
    if balance.select2_users.filter(pk=request.user.pk).exists():
        if not balance.select1_users.filter(pk=request.user.pk).exists():
            pass
    else:
        if not balance.select1_users.filter(pk=request.user.pk).exists():
            balance.select1_users.add(request.user)

    return redirect('balances:detail', pk)