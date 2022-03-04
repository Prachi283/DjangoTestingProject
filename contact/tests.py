

from django.test import TestCase
from contact.models import EmployeeContact

class TestEmployeeContact(TestCase):
	def test_can_send_message(self):
		emp=EmployeeContact.objects.create(
		first_name="Prachi",
		last_name="Patil",
		message="She Likes travelling",
		)
		self.assertEqual(EmployeeContact.objects.count(),1)
		