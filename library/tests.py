from django.test import TestCase
#  Testing Models ******

from library.models import Author, Book,Event
from datetime import datetime

class TestModels(TestCase):
    def test_book_has_an_author(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        juliana = Author.objects.create(first_name="Juliana", last_name="Crain")
        book.authors.set([philip.pk, juliana.pk])
        self.assertEqual(book.authors.count(), 2)

# testing model strings
    def test_model_str(self):
        book = Book.objects.create(title="The man in the high castle")
        philip = Author.objects.create(first_name="Philip", last_name="K. Dick")
        self.assertEqual(str(book), "The man in the high castle")
        self.assertEqual(str(philip), "Philip K. Dick")

# testing model fields 
    
    def test_event_model(self):
        event = Event.objects.create(
            title="Some title",
            seo_title="Some Seo title",
            seo_description="Some description",
            abstract="The abstract",
            body="The body",
            duration=2,
            slug="the-slug",
            start_date=datetime.now(),
            price=800,
            location="Rome",
            published=False,
        )