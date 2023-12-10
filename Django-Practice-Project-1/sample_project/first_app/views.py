from django.shortcuts import render
import datetime
# Create your views here.


def home(request):
    d = {'author': 'Don', 'age': 21, 'lst': [1, 2, 3, 4, 5], 'name': "I'm Fahim Faysal", 'village': 'digram', 'birthday': datetime.datetime.now(), 'country': '', 'persons': [
         {'name': 'zed', 'age': 19},
         {'name': 'amy', 'age': 22},
         {'name': 'joe', 'age': 31},
         ], 'sizes': 123456789, 'title': 'my FIRST post'}
    return render(request, 'home.html', d)
