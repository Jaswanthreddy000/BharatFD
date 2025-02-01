import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_api_with_language():
    # Create an FAQ instance
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक वेब फ्रेमवर्क है।",
    )

    client = APIClient()

    # Test English response (default)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"
    assert response.data[0]['answer'] == "Django is a web framework."

    # Test Hindi response
    response = client.get(reverse('faq-list') + '?lang=hi')
    assert response.status_code == 200
    assert response.data[0]['question'] == "Django क्या है?"
    assert response.data[0]['answer'] == "Django एक वेब फ्रेमवर्क है।"

    # Test fallback to English if translation is missing
    response = client.get(reverse('faq-list') + '?lang=bn')
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"
    assert response.data[0]['answer'] == "Django is a web framework."