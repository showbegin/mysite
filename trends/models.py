from django.db import models
from datetime import datetime
import pytz
import json

class Dates(models.Model):
    date = models.DateTimeField('date published')
    
    def fill_cases(self, cases_dict):
        for key,value in cases_dict.items():
            r,created=Regions.objects.get_or_create(region=key)
            self.cases_set.create(region=r, quantity=value)
    
    def __str__(self):
        return datetime.strftime(self.date, "%m/%d/%Y, %H:%M:%S")

class Regions(models.Model):
    region = models.CharField(max_length=100)
    
    def __str__(self):
        return self.region
    
class Cases(models.Model):
    date = models.ForeignKey(Dates, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
           
    def __str__(self):
        return datetime.strftime(self.date.date, "%m/%d/%Y, %H:%M:%S")+' '+str(self.quantity)+' инфицированных в '+self.region.region
    
def load_cases(path):
    with open(path) as f:
        cases=json.load(f)
    dic={}
    for strkey, value in cases.items():
        key=datetime.strptime(strkey, '%d-%m-%Y %H:%M').replace(tzinfo=pytz.utc)
        dic[key]=value
    for timepoint, stats in dic.items():
        dt,created=Dates.objects.get_or_create(date=timepoint)
        if created:
            dt.fill_cases(stats)
        