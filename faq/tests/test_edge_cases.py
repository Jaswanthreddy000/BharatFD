import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.urls import reverse

@pytest.mark.django_db
def test_empty_faq_list():
    client = APIClient()

    # Request with no FAQs in the database
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert len(response.data) == 0

@pytest.mark.django_db
def test_long_faq_text():
    long_question = "What is Django? " * 100
    long_answer = "Django is a web framework. " * 100
    faq = FAQ.objects.create(
        question=long_question,
        answer=long_answer,
    )

    client = APIClient()

    # Request the FAQ
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == long_question
    assert response.data[0]['answer'] == long_answer
