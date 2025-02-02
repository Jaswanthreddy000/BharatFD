import pytest
from rest_framework.test import APIClient
from faq.models import FAQ
from django.urls import reverse

@pytest.mark.django_db
def test_sql_injection():
    client = APIClient()

    # Attempt SQL injection
    response = client.get(reverse('faq-list') + '?lang=hi; DROP TABLE faq_faq;')
    assert response.status_code == 200  # Should not execute the SQL command

@pytest.mark.django_db
def test_xss_protection():
    # Create an FAQ with potential XSS payload
    faq = FAQ.objects.create(
        question="<script>alert('XSS')</script>",
        answer="<script>alert('XSS')</script>",
    )

    client = APIClient()

    # Request the FAQ
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert "<script>" not in response.data[0]['question']  # XSS payload should be escaped
    assert "<script>" not in response.data[0]['answer']
