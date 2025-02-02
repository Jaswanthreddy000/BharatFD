import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.urls import reverse

@pytest.mark.django_db
def test_large_dataset():
    # Create 1000 FAQs
    for i in range(1000):
        FAQ.objects.create(
            question=f"What is Django {i}?",
            answer=f"Django is a web framework {i}.",
        )

    client = APIClient()

    # Request the FAQ list
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert len(response.data) == 1000

@pytest.mark.django_db
def test_pagination():
    # Create 100 FAQs
    for i in range(100):
        FAQ.objects.create(
            question=f"What is Django {i}?",
            answer=f"Django is a web framework {i}.",
        )

    client = APIClient()

    # Request the first page
    response = client.get(reverse('faq-list') + '?page=1')
    assert response.status_code == 200
    assert len(response.data) == 10  # Assuming 10 FAQs per page

    # Request the second page
    response = client.get(reverse('faq-list') + '?page=2')
    assert response.status_code == 200
    assert len(response.data) == 10
