import pytest
from faq.models import FAQ


@pytest.mark.django_db
def test_faq_model_translation():
    # ✅ Create an FAQ instance with multiple languages
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक वेब फ्रेमवर्क है।",
        question_bn="জ্যাঙ্গো কী?",
        answer_bn="জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।",
        question_te="డ్జాంగో అంటే ఏమిటి?",
        answer_te="డ్జాంగో ఒక వెబ్ ఫ్రేమ్‌వర్క్.",
    )

    # ✅ Test English translation (default)
    assert faq.get_translated_question() == "What is Django?"
    assert faq.get_translated_answer() == "Django is a web framework."

    # ✅ Test Hindi translation
    assert faq.get_translated_question('hi') == "Django क्या है?"
    assert faq.get_translated_answer('hi') == "Django एक वेब फ्रेमवर्क है।"

    # ✅ Test Bengali translation
    assert faq.get_translated_question('bn') == "জ্যাঙ্গো কী?"
    assert faq.get_translated_answer('bn') == "জ্যাঙ্গো একটি ওয়েব ফ্রেমওয়ার্ক।"

    # ✅ Test Telugu translation
    assert faq.get_translated_question('te') == "డ్జాంగో అంటే ఏమిటి?"
    assert faq.get_translated_answer('te') == "డ్జాంగో ఒక వెబ్ ఫ్రేమ్‌వర్క్."

    # ✅ Ensure fallback to English if translation is missing
    assert faq.get_translated_question('fr') == "What is Django?"  # French ('fr') missing
    assert faq.get_translated_answer('fr') == "Django is a web framework."
