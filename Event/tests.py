from django.test import TestCase
from library.models import Author, Book, Event
from model_bakery import baker


class TestModels(TestCase):
    def test_event_model(self):
        event = baker.make(Event, title="The man in the high castle presentation")
        self.assertEqual(str(event), "The man in the high castle presentation")
