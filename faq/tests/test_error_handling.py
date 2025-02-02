import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.urls import reverse

@pytest.mark.django_db
def test_invalid_language_parameter():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    client = APIClient()

    # Request with invalid language parameter
    response = client.get(reverse('faq-list') + '?lang=xx')  # 'xx' is invalid
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"  # Fallback to English
    assert response.data[0]['answer'] == "Django is a web framework."

@pytest.mark.django_db
def test_missing_faq():
    client = APIClient()

    # Request for a non-existent FAQ
    response = client.get(reverse('faq-detail', args=[999]))  # ID 999 does not exist
    assert response.status_code == 404
