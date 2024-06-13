
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator

def index(request):
    return render(request, 'translator/index.html')

def translate_text(request):
    if request.method == 'POST':
        text_to_translate = request.POST.get('text_to_translate', '')
        destination_language = request.POST.get('destination_language', 'en')

        translator = Translator()
        translated_text = translator.translate(text_to_translate, dest=destination_language).text

        return JsonResponse({'translated_text': translated_text})
