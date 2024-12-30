from django.shortcuts import render
import datetime
def home(request):
    d = {'name': 'Mahfuza','age': 20,'lst': ['python', 'is', 'best'],
         'birthday': datetime.datetime.now(),'courses': [
            {
                'id': 1,
                'name': 'P',
                'fee': 5000
            },
            {
                'id': 2,
                'name': 'Django',
                'fee': 6000
            },
            {
                'id': 3,
                'name': 'my',
                'fee': 7000
            }
        ]
    }
    return render(request, 'first_app/home.html', d)

