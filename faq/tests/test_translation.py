import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.urls import reverse

@pytest.mark.django_db
def test_missing_translation():
    # Create an FAQ with only English text
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    client = APIClient()

    # Request with a language that has no translation
    response = client.get(reverse('faq-list') + '?lang=fr')  # French ('fr') missing
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"  # Fallback to English
    assert response.data[0]['answer'] == "Django is a web framework."
