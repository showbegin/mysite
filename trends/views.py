from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'trends/index.html'
    context_object_name = 'last_dates'
    def get_queryset(self):
        return Dates.objects.order_by('date')

def date(request,date_id):
    date = get_object_or_404(Dates, pk=date_id)
    return render(request, 'trends/dayinfo.html', {'date': date})



def region(request,date_id,region):
    return HttpResponse("you are looking cases for the {} date at {} region".format(date_id, region))