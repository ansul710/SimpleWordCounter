from django.shortcuts import render


def word_counter(request):
    return render(request, 'home.html', {})


def count(request):
    text = request.GET['userinput']
    words = text.split(' ')
    word_length = len(words)
    context = {'key': text, 'total_words': word_length}
    return render(request, 'counter.html', context)
