from django.shortcuts import render, redirect
from .forms import BalanceForm, CommentForm
from .models import Balance, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q


# Create your views here.
def index(request):
    balances = Balance.objects.order_by('-pk')
    context = {
        'balances' : balances,
    }
    return render(request, 'balances/index.html', context)



@login_required
def create(request):
    if request.method == 'POST':
        form = BalanceForm(request.POST, request.FILES)
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


@login_required
def delete(request, pk):
    balance = Balance.objects.get(pk=pk)
    if balance.user == request.user:
        balance.delete()
    return redirect('balances:index')


def detail(request, pk):
    balance = Balance.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = balance.comment_set.order_by('-pk')
    balance.view_count += 1
    balance.save()
    context = {
        'balance' : balance,
        'comment_form' : comment_form,
        'comments' : comments,
    }    
    return render(request, 'balances/detail.html', context)



@login_required
def answer(request, pk, balance_answer):
    balance = Balance.objects.get(pk=pk)
    
    if balance_answer == balance.select1_content:
        if request.user not in balance.select2_users.all():
            balance.select1_users.add(request.user)
    else:
        if request.user not in balance.select1_users.all():
            balance.select2_users.add(request.user)
    return redirect('balances:detail', pk)



@login_required
def comment_create(request, pk):
    # if request.method == 'POST':
    balance = Balance.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.balance = balance
        comment.user = request.user
        comment.save()
        return redirect('balances:detail', pk)

    context = {
        'balance' : balance,
        'comment_form' : comment_form,
    }
    return render(request, 'balances/detail.html', context)


@login_required
def likes(request, pk):
    balance = Balance.objects.get(pk=pk)

    if balance.like_users.filter(pk=request.user.pk).exists():
        balance.like_users.remove(request.user)
    else:
        balance.like_users.add(request.user)
    return redirect('balances:index')


def search(request):
    query = request.GET.get('q', '')
    if query:
        search = Balance.objects.filter(
            Q(title__icontains=query)|
            Q(user__username__exact=query)
        )
    else:
        search = Balance.objects.all()[::-1]
    return render(request, 'balances/index.html', {'balances':search})