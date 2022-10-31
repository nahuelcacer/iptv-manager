from django.shortcuts import render
from apps.manager.tools import getDataofAPI

# Create your views here.
def Manager(request):
    data = getDataofAPI('https://iptv-org.github.io/api/streams.json')
    context = {
        "data":data
    }
    return render(request, 'manager.html', context)

