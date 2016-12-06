#  !/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from test_app.models import ForeingModel

from faker import Factory
fake = Factory.create()

class Command(BaseCommand):
    help = "populate data for hand testing propose"

    def handle(self, *args, **options):
        for _ in range(0, 1000):
            fm = ForeingModel(name=fake.name())
            fm.save()
