from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer
from django.core.cache import cache
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .forms import FAQForm
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, redirect



# class FAQViewSet(viewsets.ModelViewSet):
#     queryset = FAQ.objects.all()
#     serializer_class = FAQSerializer

#     def get_queryset(self):
#         lang = self.request.query_params.get('lang', 'en')
#         cache_key = f'faqs_{lang}'
#         queryset = cache.get(cache_key)
#         if not queryset:
#             queryset = FAQ.objects.all()
#             for faq in queryset:
#                 faq.question = faq.get_translated_question(lang)
#                 faq.answer = faq.get_translated_answer(lang)
#             cache.set(cache_key, queryset, timeout=60 * 15)  # Cache for 15 minutes
#         return queryset
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', None)
        cache_key = f'faqs_{lang}' if lang else 'faqs_all'

        queryset = cache.get(cache_key)

        if not queryset:
            queryset = FAQ.objects.all()

            # Filter translations if a language is specified
            if lang:
                for faq in queryset:
                    faq.question = faq.get_translated_question(lang)
                    faq.answer = faq.get_translated_answer(lang)

            cache.set(cache_key, queryset, timeout=60 * 15)  # Cache for 15 minutes

        return queryset

    def retrieve(self, request, *args, **kwargs):
        # Override the retrieve method to include all translations for a single FAQ
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


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


@require_POST
@csrf_exempt  # Only use this if you're not using Django's CSRF middleware
def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    faq.delete()
    return redirect('faq-list')  # Redirect to the FAQ list page after deletion