import pytest
from django.core.cache import cache
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_cache_hit():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    client = APIClient()

    # First request (cache miss)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200

    # Second request (cache hit)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200

    # Verify cache is used
    assert cache.get('faqs_en') is not None

@pytest.mark.django_db
def test_cache_invalidation():
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
    )

    client = APIClient()

    # First request (cache miss)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200

    # Update the FAQ
    faq.question = "What is Django Framework?"
    faq.save()

    # Second request (cache should be invalidated)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django Framework?"
