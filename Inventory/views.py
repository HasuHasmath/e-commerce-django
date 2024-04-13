from django.shortcuts import render


def HomePage(request):

    data = {
        "name": "Hasmath",
        "role": "manager",
        "numbers": [1, 2, 3, 4, 5, 6],
        "marks": {
            "tamil": "100",
            "maths": "97",
            "english": "85"
        }

    }

    return render(request, 'home.html', data)


def AboutPage(request):

    return render(request, 'about.html')


def ServicePage(request):

    return render(request, 'service.html')


def ContactPage(request):

    return render(request, 'contact.html')
