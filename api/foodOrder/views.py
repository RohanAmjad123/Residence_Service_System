from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def foodOrder(request):
    return render(request, 'foodOrder.html')