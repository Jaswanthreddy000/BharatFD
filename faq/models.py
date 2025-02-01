from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator


translator = Translator()


def translate_text(text, dest_lang):
    if not text:  # Ensure text is not empty before translating
        return text
    try:
        return translator.translate(text, dest=dest_lang).text
    except Exception as e:
        print(f"Translation failed for {dest_lang}: {e}")  # Log the error
        return text  # Fallback to original text


class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    answer_hi = RichTextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_bn = RichTextField(blank=True, null=True)  # Bengali translation
    question_te = models.TextField(blank=True, null=True)  # Telugu translation
    answer_te = RichTextField(blank=True, null=True)  # Telugu translation

    def get_translated_question(self, lang='en'):
        return getattr(self, f'question_{lang}', self.question) or self.question

    def get_translated_answer(self, lang='en'):
        return getattr(self, f'answer_{lang}', self.answer) or self.answer

    def save(self, *args, **kwargs):
        # Translate only if the field is empty
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.answer_hi:
            self.answer_hi = translate_text(self.answer, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')
        if not self.answer_bn:
            self.answer_bn = translate_text(self.answer, 'bn')  
        if not self.question_te:
            self.question_te = translate_text(self.question, 'te')
        if not self.answer_te:
            self.answer_te = translate_text(self.answer, 'te')       
        super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return self.question

# Add a blank line here
