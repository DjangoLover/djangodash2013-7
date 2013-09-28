"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from .utils import parse_famous, parse_events_by_date


class SimpleTest(TestCase):
    def test_basic_parse(self):
        people = parse_famous(1986, 1, 12)

        self.assertEqual(people[0]['name'], 'ZAYN MALIK')

    def test_parse_events(self):
        events = parse_events_by_date(1986, 1, 12)

        self.assertEqual(events[0], '- 24th space shuttle (61-C) mission-Columbia 7-launched')