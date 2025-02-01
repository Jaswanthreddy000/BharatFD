import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_faq_model_translation():
    # Create an FAQ instance
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a web framework.",
        question_hi="Django क्या है?",
        answer_hi="Django एक वेब फ्रेमवर्क है।",
    )

    # Test English translation (default)
    assert faq.get_translated_question() == "What is Django?"
    assert faq.get_translated_answer() == "Django is a web framework."

    # Test Hindi translation
    assert faq.get_translated_question('hi') == "Django क्या है?"
    assert faq.get_translated_answer('hi') == "Django एक वेब फ्रेमवर्क है।"

    # Test fallback to English if translation is missing
    assert faq.get_translated_question('bn') == "What is Django?"
    assert faq.get_translated_answer('bn') == "Django is a web framework."