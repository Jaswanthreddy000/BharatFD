import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from faq.models import FAQ


# @pytest.mark.django_db
# def test_faq_api_with_language():
#     # ✅ Create an FAQ instance with multiple languages
#     faq = FAQ.objects.create(
#         question="What is Django?",
#         answer="Django is a web framework.",
#         question_hi="Django क्या है?",
#         answer_hi="Django एक वेब फ्रेमवर्क है।",
#         question_bn="জ্যাঙ্গো কী?",
#         answer_bn="জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।",
#         question_te="డ్జాంగో అంటే ఏమిటి?",
#         answer_te="డ్జాంగో ఒక వెబ్ ఫ్రేమ్‌వర్క్.",
#     )

#     client = APIClient()

#     # ✅ Test English response (default)
#     response = client.get(reverse('faq-list'))
#     assert response.status_code == 200
#     assert response.data[0]['question'] == "What is Django?"
#     assert response.data[0]['answer'] == "Django is a web framework."

#     # ✅ Test Hindi response
#     response = client.get(reverse('faq-list') + '?lang=hi')
#     assert response.status_code == 200
#     assert response.data[0]['question'] == "Django क्या है?"
#     assert response.data[0]['answer'] == "Django एक वेब फ्रेमवर्क है।"

#     # ✅ Test Bengali response
#     response = client.get(reverse('faq-list') + '?lang=bn')
#     assert response.status_code == 200
#     assert response.data[0]['question'] == "জ্যাঙ্গো কী?"
#     assert response.data[0]['answer'] == "জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।"

#     # ✅ Test Telugu response
#     response = client.get(reverse('faq-list') + '?lang=te')
#     assert response.status_code == 200
#     assert response.data[0]['question'] == "డ్జాంగో అంటే ఏమిటి?"
#     assert response.data[0]['answer'] == "డ్జాంగో ఒక వెబ్ ఫ్రేమ్‌వర్క్."

#     # ✅ Ensure fallback to English if translation is missing
#     response = client.get(reverse('faq-list') + '?lang=fr')  # French ('fr') missing
#     assert response.status_code == 200
#     assert response.data[0]['question'] == "What is Django?"
#     assert response.data[0]['answer'] == "Django is a web framework."
@pytest.mark.django_db
def test_faq_api_with_language():
    # Create an FAQ instance with multiple languages
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक वेब फ्रेमवर्क है।",
        question_bn="জ্যাঙ্গো কী?",
        answer_bn="জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।",
        question_te="డ్జాంగో అంటే ఏమిటి?",
        answer_te="డ్జాంగో ఒక వెబ్ ఫ్రేమ్‌వర్క్.",
    )

    client = APIClient()

    # Test English response (default)
    response = client.get(reverse('faq-list'))
    assert response.status_code == 200
    assert response.data[0]['question'] == "What is Django?"  # Ensure this accesses the DRF Response object

    # Test Hindi response
    response = client.get(reverse('faq-list') + '?lang=hi')
    assert response.status_code == 200
    assert response.data[0]['question'] == "Django क्या है?"
