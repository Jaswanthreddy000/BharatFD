from rest_framework import serializers
from .models import FAQ


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'

    def to_representation(self, instance):
        # Get the language parameter from the request
        lang = self.context['request'].query_params.get('lang', None)

        # If a language is specified, return only that translation
        if lang:
            return {
                'id': instance.id,
                'question': instance.get_translated_question(lang),
                'answer': instance.get_translated_answer(lang),
            }

        # If no language is specified, return all translations
        return super().to_representation(instance)

#blank line