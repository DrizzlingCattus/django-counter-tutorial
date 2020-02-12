from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Counter

# Create your views here.

def insert_count(delta):
    try:
        c = Counter.objects.order_by("-id").first()
        Counter.objects.create(count=c.count + delta)
    except:
        Counter.objects.create(count=delta)
        print("occuring exception")

def update_status():
    ecs = Counter.objects.filter(time_limit__lte=timezone.now())
    ecs.update(status='e')

def up(request):
    insert_count(1)
    return HttpResponseRedirect(reverse('counter:index'))

def down(request):
    insert_count(-1)
    return HttpResponseRedirect(reverse('counter:index'))

def clear(request):
    cs = Counter.objects.all()
    cs.delete()
    return HttpResponseRedirect(reverse('counter:index'))

def index(request):
    update_status()
    cs = Counter.objects.order_by("-id")[0:]
    context = {
        'counters': cs,
    }
    return render(request, 'counter/index.html', context)
