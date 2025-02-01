from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from django.shortcuts import render, redirect
from .forms import FAQForm



class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        queryset = cache.get(cache_key)
        if not queryset:
            queryset = FAQ.objects.all()
            for faq in queryset:
                faq.question = faq.get_translated_question(lang)
                faq.answer = faq.get_translated_answer(lang)
            cache.set(cache_key, queryset, timeout=60 * 15)  # Cache for 15 minutes
        return queryset


def faq_list(request):
    lang = request.GET.get('lang', 'en')  # Get the selected language
    faqs = FAQ.objects.all()

    # Translate FAQs dynamically
    for faq in faqs:
        faq.question = faq.get_translated_question(lang)
        faq.answer = faq.get_translated_answer(lang)

    return render(request, 'faq/faq_list.html', {'faqs': faqs})



def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faq-list')  # Redirect to the FAQ list page after saving
    else:
        form = FAQForm()
    return render(request, 'faq/add_faq.html', {'form': form})