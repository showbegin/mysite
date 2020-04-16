from django.test import TestCase
from .models import *
from datetime import datetime
from django.utils import timezone
import pytz

class test_model(TestCase):
    def test_dates_correctess(self):
        newtime=Dates(date=datetime(2020,3,24,10, tzinfo=pytz.utc))
        self.assertIs(newtime.date>datetime(2020,3,24,8, tzinfo=pytz.utc), True)
